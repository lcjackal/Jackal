# Hızlı Kurulum Hataları ve Çözümleri

## 1. Backend (FastAPI) Hataları

- **ModuleNotFoundError: No module named 'fastapi'**
  - Çözüm:  
    ```
    pip install fastapi uvicorn
    ```

- **ImportError: cannot import name ...**
  - Çözüm:  
    İlgili fonksiyonları dosyada tanımlı hale getir.

- **Internal Server Error (500)**
  - Çözüm:  
    Veritabanı ve tabloları oluşturmak için:
    ```python
    # backend/db_init.py
    from backend.db import init_db

    if __name__ == "__main__":
        init_db()
        print("Veritabanı ve tablolar oluşturuldu.")
    ```
    Terminalde:
    ```
    python3 -m backend.db_init
    ```

- **404 Not Found (ana dizin)**
  - Çözüm:  
    Ana dizinde endpoint yok, `/docs` veya ilgili endpointleri kullan.

---

## 2. Frontend (Vite/React) Hataları

- **Sayfa boş veya 404**
  - Çözüm:  
    - Vite’ı şu şekilde başlat:
      ```
      npm run dev -- --host
      ```
    - Terminalde çıkan portu PORTS panelinde “Public” yap.
    - Tarayıcıda çıkan `.github.dev` adresini kullan.

- **[plugin:vite:import-analysis] Failed to resolve import ...**
  - Çözüm:  
    Eksik component dosyalarını oluştur ve doğru isimle kaydet.

- **JSX/React kod hatası**
  - Çözüm:  
    Kodları JSX kurallarına uygun şekilde düzenle.

- **PORTS panelinde port görünmüyor veya “Public” yapılamıyor**
  - Çözüm:  
    - Farklı bir portta başlatmayı dene:
      ```
      npm run dev -- --host --port 4173
      ```
    - PORTS panelini yenile, portu “Public” yap.
    - Sorun devam ederse Codespaces’i yeniden başlat.

---

## 3. Genel İpuçları

- **Backend ve frontend’i ayrı terminallerde başlat.**
- **Codespaces’te localhost yerine .github.dev adresini kullan.**
- **PORTS panelinde ilgili portun “Public” olduğundan emin ol.**
- **Her değişiklik sonrası terminalde hata olup olmadığını kontrol et.**

---

> **Not:** Codespaces veya tarayıcıyı kapatırsan bu konuşma geçmişi kaybolur.  
> Bu rehberi repoya ekleyerek her zaman erişebilirsin.
