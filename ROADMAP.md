# 🗺️ Proje Yol Haritası (ROADMAP)

## Faz 0: Yazmadan Önce Anla
* AndroidManifest.xml yapısının ve "uses-permission" etiketlerinin çalışma mantığının kavranması.
* APKTool ile kapalı kutu olan APK'ların tersine mühendislikle parçalanıp okunabilir hale getirilmesi yönteminin anlaşılması.

## Faz 1: Araştırma ve Keşif
* Siber güvenlik açısından "Tehlikeli" (Dangerous) kabul edilen izinlerin (Kamera, Konum, SMS, Rehber vb.) tespit edilip veritabanı haline getirilmesi.
* Python'ın yerleşik XML kütüphanelerinin (xml.etree.ElementTree) araştırılması. (Notlar `docs/research/` içindedir).

## Faz 2: Ortam Kurulumu
* Python 3.x ortamının ayarlanması.
* APKTool ve Java gereksinimlerinin sisteme kurulması.
* Projenin Dockerize edilebilmesi için konteyner mimarisinin kurgulanması.

## Faz 3: Uygulama
1. APKTool ile APK dosyasının `d` komutuyla parçalanması.
2. `src/izin_denetici.py` dosyasının oluşturulması.
3. XML ayrıştırma (parsing) fonksiyonunun yazılması.
4. Çıkarılan izinlerin güvenlik listemizle karşılaştırılması.
5. Risk puanlama algoritmasının (Tehlikeli * 10, Normal * 1) koda dökülmesi.
6. Terminal arayüzü ve rapor formatının tasarlanması.

## Faz 4: Test ve Raporlama
* 3 farklı açık kaynaklı Android uygulaması (Hesap Makinesi, El Feneri, Not Defteri) üzerinde testlerin yapılması.
* Çıktıların `rapor1.txt`, `rapor2.txt` ve `rapor3.txt` olarak `docs/research/` altına kaydedilmesi.

## Faz 5: Teslim Kontrol Listesi
- [x] Modüler repo yapısı oluşturuldu.
- [x] ROADMAP.md ve README.md tamamlandı.
- [x] Dockerfile ve docker-compose eklendi.
- [x] 3 uygulamanın analizi belgelendi.
- [x] Keyvan Hoca Collaborator olarak eklendi.