# C Dili 30 Günlük (150 Derslik) İleri Eğitim & Derleme Portalı

**C Masterclass** — Python (PyWebView) ile geliştirilmiş, masaüstü native pencere içinde çalışan, HTML/CSS/JS tabanlı bir C dili öğretim uygulaması.

## ✨ Özellikler

- 📘 **150 Derslik Müfredat** — 30 gün × 5 alt ders, başlangıçtan ileri seviyeye
- 🧠 **1500 Quiz Sorusu** — Her gün 50 çoktan seçmeli soru
- 💻 **Entegre C Derleyicisi** — GCC/Clang/MSVC otomatik tespit, derleme ve çalıştırma
- 🔍 **Canlı RAM Inspector** — Stack & Heap bellek haritası görselleştirmesi
- 🔬 **Statik Kod Analizi** — Bellek sızıntısı, buffer overflow ve güvenlik uyarıları
- ⚡ **Hazır Algoritma Şablonları** — QuickSort, LinkedList, BinarySearch ve daha fazlası
- 📚 **C Standart Kütüphane Rehberi** — Hızlı referans kartları
- 🏆 **Başarım Sistemi** — İlerlemeye bağlı dinamik rozetler ve sertifika
- 💾 **Kalıcı İlerleme** — Tamamlanan dersler ve kod taslakları otomatik kaydedilir

## 🚀 Kurulum

### Gereksinimler

- Python 3.9+
- GCC, Clang veya MSVC derleyicisi (C kodlarını derlemek için)
  - Windows: [MSYS2 MinGW-w64](https://www.msys2.org/) önerilir
  - Linux/Mac: `gcc` genellikle önceden yüklüdür

### Python Bağımlılıkları

```bash
pip install -r requirements.txt
```

### Çalıştırma

```bash
python app.py
```

### Tek Dosya EXE Olarak Paketleme

```bash
python build_exe.py
# veya
build.bat
```

Oluşan `dist/C_Egitim_Uygulamasi.exe` dosyası taşınabilir bir masaüstü uygulamasıdır.

## 📁 Proje Yapısı

```
c-notlari/
├── app.py              # Ana uygulama giriş noktası (PyWebView)
├── compiler.py         # GCC/Clang derleyici motoru
├── storage.py          # Kullanıcı ilerlemesi JSON depolama
├── test_engine.py      # Entegrasyon testleri
├── build_exe.py        # PyInstaller paketleme betiği
├── build.bat           # Windows build scripti
├── requirements.txt    # Python bağımlılıkları
├── data/
│   ├── lessons_data.py     # 150 ders müfredatı
│   ├── quizzes_data.py     # 1500 quiz sorusu
│   ├── cheatsheet_data.py  # C kütüphane referans kartları
│   └── snippets_data.py    # Hazır algoritma şablonları
└── web/
    ├── index.html      # UI düzeni (3 panelli IDE)
    ├── styles.css      # Windows 11 Fluent Dark teması
    └── app.js          # Frontend mantığı
```

## ⌨️ Kısayollar

| Kısayol | İşlev |
|---|---|
| `F5` / `F9` / `F10` | Kodu derle ve çalıştır |
| `Ctrl+S` | Kod taslağını kaydet |
| `Ctrl+/` | Yorum satırı aç/kapa |
| `Ctrl+D` | Satırı kopyala |
| `Ctrl+E` | Satırı sil |
| `Ctrl+Shift+↑/↓` | Satırı taşı |
| `Tab` / `Shift+Tab` | Girinti ekle/kaldır |

## 📝 Lisans

Bu proje kişisel eğitim amaçlıdır.
