# Praktikum Kecerdasan Buatan - Pertemuan 2 (Logika Fuzzy)

Repositori ini dbuat untuk memenuhi tugas Praktikum Kecerdasan Buatan pada pertemuan ke-2. Di dalam modul ini, diberikan contoh pengaplikasian Logika Fuzzy (Fuzzy Logic) menggunakan bahasa pemrograman Python dengan bantuan *library* `scikit-fuzzy`.

## Tugas Dari Mas Asprak

**TUGAS PRAKTIKUM – LOGIKA FUZZY 1 (KIPAS ANGIN)**

Buatlah sebuah sistem logika fuzzy menggunakan bahasa pemrograman Python dengan library SciKit-Fuzzy untuk menentukan kecepatan kipas angin berdasarkan kondisi lingkungan.

**Ketentuan:**
- Sistem harus memiliki:
  - **2 variabel input (antecedent):**
    - Suhu (rentang 0–40 °C)
    - Kelembapan (rentang 0–100 %)
  - **1 variabel output (consequent):**
    - Kecepatan kipas (rentang 0–100)
- Setiap variabel harus memiliki minimal 3 himpunan fuzzy.
- Gunakan minimal 3 aturan fuzzy (IF–THEN).

## Daftar Program / File

Dalam repositori ini terdapat tiga *script* utama:

1. **`tugas.py` (Sistem Kontrol Kecepatan Kipas Angin)** 
   Program ini mensimulasikan sistem kontrol kecepatan kipas angin secara otomatis berdasarkan dua variabel input:
   - **Suhu** (Dingin, Normal, Panas)
   - **Kelembapan** (Kering, Lembab, Basah)
   - **Output:** Kecepatan putaran kipas angin (Lambat, Sedang, Cepat).
   Program ini juga menampilkan visualisasi grafik (plot) dari derajat keanggotaan dan hasil sistem kontrolnya menggunakan matplotlib.

2. **`produksi.py` (Sistem Keputusan Jumlah Produksi Barang)** 
   Program ini mencontohkan penerapan logika fuzzy untuk menentukan rekomendasi jumlah tingkat produksi barang di pabrik berdasarkan:
   - **Biaya Produksi** (Rendah, Standar, Tinggi)
   - **Permintaan Pasar** (Turun, Biasa, Naik)
   - **Output:** Keputusan banyaknya produksi barang (Berkurang, Normal, Bertambah).

3. **`restoran.py` (Sistem Evaluasi Nilai Restoran)** 
   Program ini menerapkan logika fuzzy untuk menentukan evaluasi penilaian kinerja sebuah restoran berdasarkan:
   - **Rasa Makanan** (Tidak Enak, Sedang, Enak)
   - **Kualitas Pelayanan** (Ketus, Biasa, Ramah)
   - **Output:** Nilai Akhir Restoran (Buruk, Cukup, Baik).
   Program ini juga akan memunculkan grafik visualisasi penilaian menggunakan matplotlib.

## Persyaratan Sistem (Prerequisite)

Pastikan modul *library* Python di bawah ini sudah terinstal di komputer / *environment* virtual kamu sebelum menjalankan kode:

- `numpy`
- `scikit-fuzzy`
- `matplotlib` (untuk menampilkan grafik visualisasi pada file `tugas.py` dan `restoran.py`)

Kamu dapat menginstalnya secara sekaligus melalui terminal dengan perintah:
```bash
pip install numpy scikit-fuzzy matplotlib
```

## Cara Menjalankan Program

Buka terminal pada direktori ini, lalu jalankan program dengan mengetikkan:

```bash
python tugas.py
# atau
python produksi.py
# atau
python restoran.py
```
