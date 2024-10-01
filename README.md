# Api Wilayah Indonesia & Kode Pos Indonesia

Aplikasi Api Wilayah Indonesia & Kode Pos Indonesia yang berfungsi sebagai API untuk mendapatkan kode pos berdasarkan pembagian wilayah administratif seperti provinsi, kabupaten, kecamatan, dan desa di Indonesia. Proyek ini menggunakan data CSV untuk wilayah dan diintegrasikan dengan frontend sederhana menggunakan template Jinja2.

## Fitur

- Mendapatkan data provinsi, kabupaten, kecamatan, dan desa di Indonesia.
- Secara otomatis mendapatkan kode pos berdasarkan desa yang dipilih.
- Arsitektur berbasis API dengan FastAPI.
- Dideploy di Vercel menggunakan serverless architecture.

## Daftar Isi

- [Instalasi](#instalasi)
- [Data CSV](#data-csv)
- [Endpoint API](#endpoint-api)
- [Deploy](#deploy)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)

## Instalasi

Untuk menjalankan proyek ini secara lokal:

1. Clone repository ini:

   ```bash
   git clone https://github.com/bukanekosoed/Api-Wilayah-Indonesia.git

2. Masuk ke direktori proyek:
   
   ```bash
   cd reponame
   
4. Buat environment virtual dan aktifkan:
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # Pada Windows gunakan `venv\Scripts\activate`
   
6. Install semua dependensi:
   
   ```bash
   pip install -r requirements.txt
   
8. Jalankan server FastAPI:
   
   ```bash
   uvicorn main:app --reload
   
10. Buka browser Anda dan akses ```http://127.0.0.1:8000``` untuk melihat API.

## Data CSV
Proyek ini menggunakan beberapa file CSV yang menyimpan data wilayah Indonesia:

- ```provinsi.csv```: Data provinsi
- ```kabupaten.csv```: Data kabupaten.
- ```kecamatan.csv```: Data kecamatan.
- ```desa.csv```: Data desa.
- ```kodepos.csv```: Data kode pos.
Pastikan semua file ini diletakkan pada direktori yang tepat (misalnya ```data/```).

## Endpoint API
Berikut adalah beberapa endpoint utama yang tersedia:

- ```/provinsi``` : Mendapatkan semua provinsi atau filter berdasarkan kode atau nama.
- ```/kabupaten?kode_provinsi={kode_provinsi}``` : Mendapatkan daftar kabupaten berdasarkan kode provinsi.
- ```/kecamatan?kode_kabupaten={kode_kabupaten}``` : Mendapatkan daftar kecamatan berdasarkan kode kabupaten.
- ```/desa?kode_kecamatan={kode_kecamatan}``` : Mendapatkan daftar desa berdasarkan kode kecamatan.
- ```/kodepos?kode_desa={kode_desa}``` : Mendapatkan kode pos untuk desa tertentu.


Setiap endpoint mengembalikan data dalam format JSON.

## Deploy
Proyek ini dideploy menggunakan Vercel. Untuk melakukan deploy proyek Anda sendiri:
1. Install Vercel CLI.
2. Pastikan struktur proyek Anda seperti berikut:
   
   ```bash
       /project-root
        ├── main.py
        ├── templates/
        ├── data/
        ├── vercel.json
        ├── requirements.txt

4. Pastikan file ```vercel.json``` Anda terlihat seperti ini:
   
   ```json
     {
      "builds": [
        {
          "src": "main.py",
          "use": "@vercel/python"
        }
      ],
      "routes": [
        {
          "src": "/(.*)",
          "dest": "main.py"
        }
      ]
    }

6. Lakukan deploy proyek Anda:

     ```bash
         vercel --prod
   
  Vercel akan melakukan build dan deploy proyek FastAPI Anda.

  ## Kontribusi
  Jika Anda ingin berkontribusi, silakan fork repository ini dan gunakan branch fitur. Pull request sangat diterima.
  - Fork repository ini
  - Buat branch fitur (```git checkout -b fitur-branch```)
  - Commit perubahan Anda (```git commit -am 'Menambahkan fitur baru'```)
  - Push ke branch (```git push origin fitur-branch```)
  - Buat Pull Request

## Lisensi
Proyek ini dilisensikan di bawah MIT License - lihat file LICENSE untuk detail lebih lanjut.

```markdown
    
### Penjelasan:

- **Instalasi**: Langkah-langkah untuk menjalankan proyek secara lokal dengan menggunakan environment virtual.
- **Data CSV**: Menjelaskan file CSV yang diperlukan untuk menyimpan data wilayah Indonesia.
- **Endpoint API**: Menyediakan daftar endpoint yang tersedia di API FastAPI.
- **Deploy**: Langkah-langkah untuk melakukan deploy proyek di Vercel.
- **Kontribusi**: Panduan bagi siapa saja yang ingin berkontribusi dalam proyek.
- **Lisensi**: Menyebutkan lisensi yang digunakan, dalam hal ini MIT License.



