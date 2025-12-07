import time
import schedule
from bot import BinanceBot
import config

def job():
    try:
        my_bot = BinanceBot()
        my_bot.run_strategy()
    except Exception as e:
        print(f"Terjadi kesalahan utama: {e}")

if __name__ == "__main__":
    print("=== Binance Trading Bot Started ===")
    print(f"Target Symbol: {config.SYMBOL}")
    print("Menunggu jadwal eksekusi selanjutnya...")
    
    # Jalankan sekali saat startup untuk pengecekan
    job()

    # Jadwal pengecekan setiap 1 menit (sesuaikan dengan kebutuhan)
    schedule.every(10).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)