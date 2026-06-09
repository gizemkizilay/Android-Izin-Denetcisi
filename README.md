<div align="center">
  <a href="https://istinye.edu.tr">
    <img src="docs/research/istinye-university-logo.png" alt="İstinye Üniversitesi" width="180"/>
  </a>

  # AndroidManifest İzin Denetçisi Aracı

  ![GitHub](https://img.shields.io/badge/GitHub-Private-red?style=flat-square&logo=github)
  ![Dil](https://img.shields.io/badge/Dil-Python-blue?style=flat-square)
  ![Durum](https://img.shields.io/badge/Durum-Tamamlandı-brightgreen?style=flat-square)
  ![Ders](https://img.shields.io/badge/Ders-BGT210-purple?style=flat-square)
</div>

### Danışman Bilgisi
| Ad Soyad | GitHub | E-posta | LinkedIn | Web Sitesi |
| :--- | :--- | :--- | :--- | :--- |
| Keyvan Arasteh | [@keyvanarasteh](https://github.com/keyvanarasteh) | keyvan.arasteh@istinye.edu.tr | [keyvanarasteh](https://linkedin.com/in/keyvanarasteh) | [qline.tech](https://qline.tech) |

### Öğrenci Bilgisi
| Ad Soyad | Öğrenci No |
| :--- | :--- |
| Gizem Kızılay | 242****015 |

### Ders Bilgileri
| Ders Adı | Ders Kodu | Kredi | Ön Koşullar | Dönem |
| :--- | :--- | :--- | :--- | :--- |
| Tersine Mühendislik | BGT210 | 3 AKTS | Temel Programlama, İşletim Sistemleri | 2025-2026 Bahar |

---

## 🚀 Proje Özeti (Project Overview)
Bu proje, Tersine Mühendislik final projesi kapsamında geliştirilmiş bir Android güvenlik analiz aracıdır. Herhangi bir APK dosyasını APKTool ile parçaladıktan sonra, uygulamanın `AndroidManifest.xml` dosyasını ayrıştırır ve barındırdığı izinleri "Normal" ve "Tehlikeli" olarak sınıflandırıp bir Risk Puanı hesaplar. Bu sayede bir mobil uygulamanın cihazda ne kadar derin yetkilere sahip olduğu saniyeler içinde raporlanabilir.

---

## 📂 Repo Yapısı (Repository Structure)
Projenin dosya ve klasör hiyerarşisi aşağıdaki gibidir:

```text
android-izin-denetcisi/
├── README.md                  # Ana belgeleme
├── ROADMAP.md                 # Proje yol haritası ve geliştirme fazları
├── .env.example               # Ortam değişkenleri şablonu
├── .gitignore                 # Git dışlama kuralları
├── Dockerfile                 # Konteyner derleme tanımı
├── docker-compose.yml         # Konteyner orkestrasyonu
├── docs/
│   ├── modules/
│   │   └── izin_analizi.md    # İzin Analiz modülünün teknik dokümantasyonu
│   ├── research/
│   │   ├── rapor1.txt         # 1. Örnek uygulamanın risk raporu
│   │   ├── rapor2.txt         # 2. Örnek uygulamanın risk raporu
│   │   └── rapor3.txt         # 3. Örnek uygulamanın risk raporu
│   └── references/
│       └── kaynaklar.md       # Projede kullanılan kaynaklar ve linkler
└── src/
    └── izin_denetici.py       # Ana Python kaynak kodu (Analiz Motoru)
