🤖 MemeDecoder AI — Yapay Zeka Destekli Meme Analiz Platformu

MemeDecoder AI, internet geyiklerini (meme) yapay zeka yardımıyla analiz eden, üzerindeki metinleri Türkçeye çeviren ve esprinin arkasındaki mizahı/kültürel bağlamı açıklayan Flask tabanlı bir web uygulamasıdır.

Kodland Python Pro mezuniyet projesi kapsamında nesne yönelimli programlama (OOP) ve modüler mimari prensiplerine uygun olarak geliştirilmiştir.

🛠️ Teknolojiler ve Kütüphaneler

Backend: Python 3.11+, Flask

Yapay Zeka (AI): Google GenAI SDK (gemini-3.8-flash)

Arayüz (Frontend): HTML5, CSS3

Güvenlik & Yapılandırma: python-dotenv, werkzeug, .gitignore

Kod Standartları: PEP 8 / Flake8 Uyumlu

📁 Proje Yapısı

meme_decoder/
│
├── services/
│   ├── __init__.py         # Servis paketi başlatıcı
│   └── ai_service.py       # Gemini API işlemlerini yöneten OOP sınıfı
│
├── static/
│   └── uploads/            # Kullanıcı tarafından yüklenen geçici görseller
│
├── templates/
│   ├── index.html          # Görsel yükleme arayüzü
│   └── result.html         # AI analiz ve çeviri sonuç ekranı
│
├── .env                    # Gizli API anahtarı (Git'e yüklenmez)
├── .gitignore              # Hassas ve geçici dosyaların engelleme listesi
├── app.py                  # Flask ana uygulama ve yönlendirme (Routing)
└── requirements.txt        # Proje bağımlılıkları listesi


🚀 Kurulum ve Çalıştırma

1. Projeyi Kopyalayın (Clone)

git clone https://github.com/kullanici-adi/meme-decoder-ai.git
cd meme-decoder-ai


2. Bağımlılıkları Yükleyin

Proje için gerekli kütüphaneleri yüklemek için terminale şu komutu yazın:

pip install flask google-genai python-dotenv werkzeug


3. .env Dosyasını Oluşturun

Proje kök dizininde .env adında bir dosya oluşturun ve Google AI Studio'dan aldığınız API anahtarını ekleyin:

GEMINI_API_KEY=senin_gemini_api_anahtarin


4. Uygulamayı Başlatın

python app.py


Uygulama çalıştıktan sonra tarayıcınızda http://127.0.0.1:5000 adresine giderek uygulamayı test edebilirsiniz.

🔒 Güvenlik

API anahtarının yetkisiz kişilerin eline geçmesini önlemek amacıyla .env dosyası ve yüklenen geçici görseller (static/uploads/) .gitignore dosyasına eklenmiştir.

Yüklenen dosya isimleri werkzeug.utils.secure_filename fonksiyonu ile güvenli hale getirilmektedir.

👨‍💻 Yazar

Geliştirici: DERİN GİRGİN

Proje Türü: final