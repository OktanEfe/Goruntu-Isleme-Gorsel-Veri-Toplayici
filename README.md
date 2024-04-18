# Görüntü İşleme ve Makine Öğrenmesi için Google Görsel Veri Toplayıcı

Bu Python betiği, verilen bir arama terimini kullanarak Google Görseller'den belirtilen sayıda görüntüyü toplamak için Selenium'u kullanır. İstenen görüntü sayısını ve kaydetme dizinini belirleyebilirsiniz. Betik ayrıca yüklenen görüntülerin kaydedilmesini ve hataların yönetilmesini sağlar.

## Kullanım

- `query`: Arama terimi
- `num_images`: İstenen görüntü sayısı
- `save_path`: Görüntülerin kaydedileceği dizin

Örneğin:


query = "Alzheimer Brain MRI"

num_images = 400

save_path = "alzheimer_brain_mri"

scrape_images(query, num_images, save_path)

## Gereksinimler

selenium kütüphanesi

requests kütüphanesi


## Kurulum Adımları

  Chrome Tarayıcısını Güncelle: chromedriver.exe'yi kullanmak için Chrome tarayıcısını en son sürüme güncellemeniz önemlidir.

  Chromedriver Sürümünü Belirleme: Kullandığınız Chrome tarayıcı sürümüne uygun olan chromedriver sürümünü belirlemelisiniz. Chrome tarayıcınızın sürümünü öğrenmek için tarayıcınızı açın ve "chrome://settings/help" adresine gidin.

  Chromedriver İndirme: Belirlediğiniz Chrome sürümüne uygun chromedriver'ı Chromedriver İndirme Sayfasından indirebilirsiniz.

  Chromedriver'ı Sisteme Ekleme: İndirdiğiniz chromedriver.exe dosyasını bir klasöre çıkartın. Daha sonra, chromedriver.exe dosyasının yolunu belirtmek için PATH değişkenini ayarlamanız gerekir. Bu, Windows için şu şekilde yapılabilir:
  Arama çubuğuna "Environment Variables" yazın ve "Edit the system environment variables" seçeneğini seçin.
  Açılan pencerede "Environment Variables..." düğmesine tıklayın.
  Alt pencerede "System variables" bölümünde "Path" öğesini seçin ve "Edit..." düğmesine tıklayın.
  Yeni bir pencerede "New" düğmesine tıklayın ve chromedriver.exe dosyasının yolunu ekleyin.

  Kurulumu Kontrol Etme: Terminal veya komut istemi açarak chromedriver --version komutunu çalıştırın. Bu komut, yüklediğiniz chromedriver sürümünü göstermelidir.

Bu adımları takip ettikten sonra chromedriver.exe'yi kullanarak Selenium ile Chrome tarayıcısını kontrol edebilirsiniz.
