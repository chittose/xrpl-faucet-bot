from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Konfigurasi
FAUCET_URL = "https://test.xrplexplorer.com/en/faucet"
ADDRESS = "rMeNpF2xtPMyjubLMKuGncEwvY5cirpXYJ"
AMOUNT = "100"

# Setup WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Tidak menampilkan browser
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

def claim_xrp():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        print("🚀 Membuka halaman faucet...")
        driver.get(FAUCET_URL)
        time.sleep(2)

        # Klik tab XRPL Testnet
        driver.find_element(By.XPATH, '//button[contains(text(), "XRPL Testnet")]').click()
        time.sleep(1)

        # Isi address
        address_input = driver.find_element(By.XPATH, '//input[@placeholder="Enter the XRPL address"]')
        address_input.clear()
        address_input.send_keys(ADDRESS)

        # Isi jumlah
        amount_input = driver.find_element(By.XPATH, '//input[@placeholder="Testnet XRP amount (maximum: 100 XRP)"]')
        amount_input.clear()
        amount_input.send_keys(AMOUNT)

        # Klik tombol claim
        driver.find_element(By.XPATH, '//button[contains(text(), "Get XRPL Testnet XRP")]').click()
        time.sleep(5)

        # Cek apakah sukses
        if "Submitted" in driver.page_source:
            print("✅ Claim berhasil dikirim.")
        else:
            print("❌ Gagal melakukan claim.")
    except Exception as e:
        print("⚠️ Error:", e)
    finally:
        driver.quit()

# Loop per 1 menit
while True:
    claim_xrp()
    print("⏳ Menunggu 1 menit sebelum claim berikutnya...\n")
    time.sleep(60)
