# Binance Trading Bot
Bot trading sederhana menggunakan Python dan library `ccxt`.

## Fitur
- Menggunakan strategi **Moving Average Crossover** (Golden Cross / Death Cross).
- Terintegrasi dengan Binance Spot Market.
- Konfigurasi parameter mudah lewat `config.py`.

## Cara Install
1. Install Python.
2. Install library yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   ```

## Cara Konfigurasi
1. Edit file `config.py`.
2. Masukkan **API KEY** dan **API SECRET** dari akun Binance Anda.
3. Atur Symbol (misal `BTC/USDT`) dan parameter lainnya.

## Cara Menjalankan
```bash
python main.py
```

> **DISCLAIMER:** Trading cryptocurrency berisiko tinggi. Bot ini hanya contoh edukasi. Gunakan dengan risiko Anda sendiri.
