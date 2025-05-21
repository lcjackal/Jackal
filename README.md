# Kripto Analiz Platformu – Kolay Kurulum ve Kullanım Kılavuzu

## Gereksinimler
- [Docker](https://www.docker.com/products/docker-desktop/) (ve Docker Compose)
- (Alternatif: Python 3.10+, `nodejs` ve `npm` – detaylar aşağıda)

## 1. Tek Tıkla Kurulum (Otomatik – Tavsiye Edilen Yöntem)

**Adım 1:** Tüm dosyaları aynı klasöre çıkarın  
**Adım 2:** Terminal açın, klasöre girin

```sh
chmod +x install.sh
./install.sh
```
Bu script her şeyi otomatik kurar ve başlatır.

**Adım 3:** Tarayıcıdan arayüze girin  
```
http://localhost:3000
```

---

## 2. Manuel Kurulum (İsteğe Bağlı)

### Backend (API) için:
```sh
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend için:
```sh
cd frontend
npm install
npm run dev
```

### Arka Plan Görevleri (Opsiyonel – Alarm ve Otomasyon için)
```sh
cd backend
celery -A app.worker.celery_worker.celery_app worker --beat --loglevel=info
```

---

## 3. Testler & Kendi Kendini Test Etme

Otomatik testler için:

```sh
cd backend
pytest
```
veya
```sh
./run_tests.sh
```

---

## 4. Sık Karşılaşılan Sorunlar & Notlar

- API veya ön yüz başlamazsa, portların başka servis tarafından kullanılmadığından emin olun
- `.env` dosyalarını örneklere göre güncelleyin (gerekirse)
- Docker ile ilgili sorunlarda, `docker ps` ve `docker logs` ile kontrol edebilirsiniz

---

## 5. Geliştirici Notları

- Tüm kodlar sade, modüler ve anlaşılırdır
- Ekstra bir kod bilgisi gerekmez
- Takıldığınız yerde bu dökümantasyonu takip edebilirsiniz

---