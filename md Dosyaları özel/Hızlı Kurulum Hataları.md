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

- **Uncaught SyntaxError: Export 'import_react3' is not defined in module**
  - Çözüm:  
    - node_modules, .vite, dist, package-lock.json dosyalarını silip tekrar yükle:
      ```
      rm -rf node_modules .vite dist package-lock.json
      npm install
      npm run dev -- --host --port 4173
      ```
    - Sadece kendi yazdığın kaynak dosyaları (App.tsx, main.tsx, components klasörü) yeni projeye kopyala, derlenmiş veya gereksiz dosya taşımamaya dikkat et.
    - Hâlâ hata devam ederse, sıfırdan yeni bir Vite projesi oluşturup sadece kaynak kodunu taşı.
    - Sıfırdan oluşturulan projede hata yoksa, eski projede bozuk veya uyumsuz bir dosya vardır.

---

## 3. Genel İpuçları

- **Backend ve frontend’i ayrı terminallerde başlat.**
- **Codespaces’te localhost yerine .github.dev adresini kullan.**
- **PORTS panelinde ilgili portun “Public” olduğundan emin ol.**
- **Her değişiklik sonrası terminalde hata olup olmadığını kontrol et.**
- **node_modules, .vite, dist gibi klasörleri asla kopyalama veya repoya ekleme.**
- **Sadece kaynak kodunu (src klasörü ve package.json) taşı.**

---

> **Not:** Codespaces veya tarayıcıyı kapatırsan bu konuşma geçmişi kaybolur.  
> Bu rehberi repoya ekleyerek her zaman erişebilirsin.