# dawn-validator
gas bang ................................
## perlu diingat wahai tuan2 jika semuanya sudah terinstal dan ada error seperti ini 
❌ Gagal Kirim Pesan Ke Telegram: 404 - {"ok":false,"error_code":404,"description":"Not Found"}
## ini gpp masih masuk pontnya, karena gagal diatas karena tuan tidak mendapati notif di telegram saja bukan point
## tapi jika tuan sudah mengisi token bot tele dan chat id nya maka status nya akan seperti ini
✅   Pesan Dikirim Ke Telegram.
dan tuan akan mendapati notif di telegram "example@gmail.com mendapatkan 20572 poin."
# paham tuan sampai sini ?, kalau sudah paham gas lanjut
# Dawn Validator klaim otomatis
## cara dapet token bot telegram dan chat id bisa liat tutor youtube tuan tuan ku seklaian  

Skrip ini digunakan untuk otomatisasi klaim poin pada Dawn Validator. Skrip ini mengambil poin dari beberapa akun secara bersamaan dan mengirimkan pemberitahuan ke Telegram.

## Fitur

- Mengambil poin dari akun Dawn Validator
- Mengirimkan pemberitahuan ke Telegram tentang poin yang didapat
- Penanganan kesalahan yang baik

## Prerequisites

- Python 3.x
- `pip` untuk menginstal dependensi

## Instalasi

1. Clone repositori ini:

   ```bash
   git clone https://github.com/bactiar291/dawn-validator.git
   cd dawn-validator
   ```
## Buat dan aktifkan virtual environment (opsional tetapi disarankan):

```bash
python -m venv venv
source venv/bin/activate
```
## Instal dependensi:

```bash
pip install -r requirements.txt
```

## jalankan dengan perintah ini 
```bash 
python3 dawnvalid.py
```
## Buat file .env dan revisi sesuka hati tuan :)
TELEGRAM_BOT_TOKEN=<YOUR_TELEGRAM_BOT_TOKEN>
TELEGRAM_CHAT_ID=<YOUR_TELEGRAM_CHAT_ID>
ACCOUNT_1_EMAIL=<ACCOUNT_EMAIL>
ACCOUNT_1_TOKEN=<ACCOUNT_TOKEN>
ACCOUNT_DELAY=15
RESTART_DELAY=60
Gantilah <YOUR_TELEGRAM_BOT_TOKEN>, <YOUR_TELEGRAM_CHAT_ID>, <ACCOUNT_EMAIL>, dan <ACCOUNT_TOKEN> dengan informasi yang sesuai.

Menjalankan Skrip
Setelah semua pengaturan selesai, Anda dapat menjalankan skrip dengan:

bash
python your_script_name.py


Kontribusi
Silakan buat pull request jika Anda ingin berkontribusi pada proyek ini. Semua kontribusi sangat dihargai!

Lisensi
Distribusi ini dilisensikan di bawah MIT License. Lihat LICENSE untuk informasi lebih lanjut.
Bactiar 291
