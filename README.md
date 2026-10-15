# Ca · SSA-Nyala — Streamlit

Aplikasi pembelajaran tentang gangguan analisis Ca pada Spektrofotometri Serapan Atom-Nyala (FAAS), dibungkus agar bisa dijalankan melalui Streamlit Community Cloud.

## Isi repository

- `app.py` — aplikasi Streamlit yang menampilkan HTML.
- `Analisis_Ca_SSA-Nyala-4.html` — antarmuka dan logika interaktif asli.
- `requirements.txt` — dependensi Python.

## Cara menjalankan di komputer

1. Instal Python jika belum ada.
2. Buka terminal/CMD pada folder project.
3. (Opsional) Buat virtual environment:
   ```bash
   python -m venv .venv
   ```
4. Aktifkan environment:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
5. Instal dependensi:
   ```bash
   pip install -r requirements.txt
   ```
6. Jalankan:
   ```bash
   streamlit run app.py
   ```

## Cara upload ke GitHub dari browser HP/komputer

1. Masuk ke https://github.com dan login.
2. Tekan **+** → **New repository**.
3. Beri nama, misalnya `ca-ssa-nyala`, pilih **Public** (atau Private jika diperlukan), lalu buat repository.
4. Tekan **Add file** → **Upload files**.
5. Ekstrak ZIP project ini terlebih dahulu, lalu upload ketiga file berikut ke root repository:
   - `app.py`
   - `Analisis_Ca_SSA-Nyala-4.html`
   - `requirements.txt`
   (Boleh ikut upload `README.md`.)
6. Tekan **Commit changes**.

## Cara deploy ke Streamlit Community Cloud

1. Buka https://share.streamlit.io/ dan login dengan akun GitHub.
2. Tekan **Create app** / **Deploy an app**.
3. Pilih repository yang baru dibuat, branch `main`, dan file utama `app.py`.
4. Tekan **Deploy** dan tunggu proses instalasi selesai.
5. Setelah berhasil, Streamlit akan memberi URL aplikasi.

## Catatan penting

- `app.py` membaca HTML dari file yang berada satu folder dengannya. Jangan mengganti nama file HTML kecuali nama di `app.py` ikut diubah.
- Tampilan dan interaksi utama tetap berasal dari HTML asli. Karena itu, beberapa elemen 3D, grafik, atau skrip yang bergantung pada browser mungkin berperilaku sedikit berbeda di iframe Streamlit.
- Data yang disimpan oleh HTML menggunakan penyimpanan browser, sehingga perilakunya dapat berbeda antarperamban atau sesi.
- Konten ilmiah dalam aplikasi adalah bahan pembelajaran; cocokkan dengan SOP dan manual instrumen sebelum digunakan sebagai hasil analisis resmi.
