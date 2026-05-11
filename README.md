## 🌐 IP TRACKING V2

Instrumen pelacakan IP tingkat lanjut yang menyajikan data intelijen akurat dalam format yang bersih dan terstruktur. Cocok digunakan oleh analis keamanan, penyelidik digital, atau developer yang ingin memvalidasi lalu lintas jaringan.

---

## 🚀 Fitur
* **Deep Metadata Extraction:** Mendapatkan lebih dari 20 parameter data dari satu alamat IP.
* **Network & ASN Tracking:** Mengetahui organisasi/ISP di balik alamat IP.
* **Geolocation Precision:** Koordinat latitude, longitude, hingga kode pos target.
* **Auto-Self Trace:** Melacak IP publik milik sendiri secara otomatis jika input dikosongkan.

---

## 🛠️ Instalasi

## 1. Environment
Pastikan Python 3 sudah terinstal di sistem Anda (Windows/Linux/Termux).

## Clone
```
git clone https://github.com/123tool/Ip-Tracking-V2.git
```
## Folder
```
cd Ip-Tracking-V2
```
## Library
```
pip install requests
```
a. Windows
```
pip install requests phonenumbers pywifi
```
b. Linux (Ubuntu / Kali Linux)
```
sudo pip3 install requests phonenumbers pywifi
```
c. Termux
```
pkg install python
pip install requests phonenumbers pywifi
```
## Jalankan
```
python main.py
```

1. Input Target :
   Masukkan alamat IP target (Contoh: 8.8.8.8).
2. Self Trace :
   Langsung tekan ENTER jika ingin melacak detail IP Anda sendiri.
3. Analisis Data :
   Hasil intelijen akan ditampilkan seketika dalam format yang mudah dibaca.
4. Catatan :
   Data yang dihasilkan bergantung pada database publik API. Keakuratan lokasi geografis bisa bervariasi tergantung pada kebijakan privasi ISP target. Gunakan dengan bijak untuk tujuan keamanan digital.
