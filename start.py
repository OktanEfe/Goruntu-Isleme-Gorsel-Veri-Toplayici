from selenium import webdriver
import os
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_images(query, num_images, save_path):
    # Set up the web driver (make sure to download the appropriate driver for your browser)
    driver = webdriver.Chrome()

    try:
        # Kaydetme dizinini mevcut dizinde oluştur
        save_path = os.path.join(os.getcwd(), save_path)
        os.makedirs(save_path, exist_ok=True)

        # Google Görseller arama URL'si oluştur
        search_url = f"https://www.google.com/search?q={query}&tbm=isch"

        # Google Görseller arama sayfasını aç
        driver.get(search_url)

        # Daha fazla görüntü yüklemek için aşağı kaydır
        for _ in range(num_images // 50):
            driver.execute_script("window.scrollBy(0,10000)")

        # Görüntülerin yüklenmesini bekleyin
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "img.Q4LuWd")))

        # Görüntü öğelerini al   Not: 10 tane fotoğraftan 6 tanesi başarılı şekilde indiriliyor kalanlar en altta yazılan hatayı veriyor.
        img_elements = driver.find_elements(By.CSS_SELECTOR, "img.Q4LuWd")

        # Loop through the first num_images images
        for i, img_element in enumerate(img_elements[:num_images]):
            try:
                # Her bir görüntüyü açmak için üzerine tıkla
                img_element.click()

                # Açılan görüntünün yüklenmesini bekle
                WebDriverWait(driver,4).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img.sFlh5c.pT0Scc.iPVvYb')))

                # Açılan görüntünün URL'sini al
                img_url_element = driver.find_element(By.CSS_SELECTOR, 'img.sFlh5c.pT0Scc.iPVvYb')
                img_url = img_url_element.get_attribute("src")

                # Fotoğrafı İndir
                img_name = f"{query}_{i+1}.jpg"
                img_path = os.path.join(save_path, img_name)
                response = requests.get(img_url, stream=True)
                with open(img_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)
                print(f"Image {i+1} downloaded successfully")

            except Exception as e:
                print(f"Failed to download image {i+1}: {e}")

    finally:
        # Tarayıcıyı Kapat
        driver.quit()

# Kullanım
query = "Normal Brain MRI"
num_images = 400
save_path = "normal_brain_mri"
scrape_images(query, num_images, save_path)

# Hata araştırılacak...
# Tahminin bulduğu fotoğrafların png,webp,ico gibi başka dosya formatlarında olduğu ve bunları .jpg olarak kayıt ederken hata aldığı 
# Farklı css türleri nasıl kayıt edilecek kaç farklı css türü var araştırılacak

'''
Failed to download image 10: Message: 
Stacktrace:
        GetHandleVerifier [0x00007FF653007062+63090]
        (No symbol) [0x00007FF652F72CB2]
        (No symbol) [0x00007FF652E0EC65]
        (No symbol) [0x00007FF652E5499D]
        (No symbol) [0x00007FF652E54ADC]
        (No symbol) [0x00007FF652E95B37]
        (No symbol) [0x00007FF652E7701F]
        (No symbol) [0x00007FF652E93412]
        (No symbol) [0x00007FF652E76D83]
        (No symbol) [0x00007FF652E483A8]
        (No symbol) [0x00007FF652E49441]
        GetHandleVerifier [0x00007FF6534025CD+4238301]
        GetHandleVerifier [0x00007FF65343F72D+4488509]
        GetHandleVerifier [0x00007FF653437A0F+4456479]
        GetHandleVerifier [0x00007FF6530E05A6+953270]
        (No symbol) [0x00007FF652F7E57F]
        (No symbol) [0x00007FF652F79254]
        (No symbol) [0x00007FF652F7938B]
        (No symbol) [0x00007FF652F69BC4]
        BaseThreadInitThunk [0x00007FFA30A7257D+29]
        RtlUserThreadStart [0x00007FFA32BEAA58+40]
'''