import ccxt
import pandas as pd
import config
import time

class BinanceBot:
    def __init__(self):
        # Inisialisasi koneksi ke Binance
        self.exchange = ccxt.binance({
            'apiKey': config.API_KEY,
            'secret': config.API_SECRET,
            'enableRateLimit': True,
        })
        
    def fetch_data(self, symbol, timeframe, limit=100):
        """Mengambil data candle (OHLCV) dari Binance"""
        try:
            bars = self.exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
            df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            return df
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    def calculate_indicators(self, df):
        """Menghitung indikator teknikal (Contoh: Moving Average)"""
        df['short_ma'] = df['close'].rolling(window=config.MA_SHORT_WINDOW).mean()
        df['long_ma'] = df['close'].rolling(window=config.MA_LONG_WINDOW).mean()
        return df

    def get_balance(self, currency='USDT'):
        """Mengecek saldo"""
        try:
            balance = self.exchange.fetch_balance()
            return balance['total'][currency]
        except Exception as e:
            print(f"Error fetching balance: {e}")
            return 0

    def place_buy_order(self, symbol, amount_usdt):
        """Melakukan order beli market"""
        try:
            # Hitung jumlah koin yang bisa dibeli dengan amount_usdt
            price = self.exchange.fetch_ticker(symbol)['last']
            amount = amount_usdt / price
            
            # Eksekusi Order
            order = self.exchange.create_market_buy_order(symbol, amount)
            print(f"[BUY] Berhasil membeli {symbol}: {order}")
            return order
        except Exception as e:
            print(f"[ERROR] Gagal Buy: {e}")
            return None

    def place_sell_order(self, symbol):
        """Melakukan order jual market (jual semua aset simbol tsb)"""
        try:
            # Ambil saldo koin yang dimiliki (misal BTC)
            currency = symbol.split('/')[0]
            balance = self.get_balance(currency)
            
            if balance > 0:
                order = self.exchange.create_market_sell_order(symbol, balance)
                print(f"[SELL] Berhasil menjual {symbol}: {order}")
                return order
            else:
                print(f"[INFO] Saldo {currency} kosong, tidak bisa jual.")
        except Exception as e:
            print(f"[ERROR] Gagal Sell: {e}")
            return None

    def run_strategy(self):
        """Jalankan logika trading sekali putaran"""
        print(f"--- Menganalisis Pasar {config.SYMBOL} ---")
        df = self.fetch_data(config.SYMBOL, config.TIMEFRAME)
        
        if df is not None:
            df = self.calculate_indicators(df)
            last_row = df.iloc[-1]
            prev_row = df.iloc[-2]

            print(f"Harga saat ini: {last_row['close']}")
            print(f"MA Short ({config.MA_SHORT_WINDOW}): {last_row['short_ma']}")
            print(f"MA Long ({config.MA_LONG_WINDOW}): {last_row['long_ma']}")

            # Logika Crossover Sederhana (Golden Cross & Death Cross)
            
            # Cek Sinyal BUY (Golden Cross: Short MA memotong ke atas Long MA)
            if prev_row['short_ma'] < prev_row['long_ma'] and last_row['short_ma'] > last_row['long_ma']:
                print(">> SIGNAL BUY TERDETEKSI! <<")
                # self.place_buy_order(config.SYMBOL, config.INVESTMENT_AMOUNT) # Uncomment untuk live trade
                print("(Simulasi) Order Buy dikirim.")

            # Cek Sinyal SELL (Death Cross: Short MA memotong ke bawah Long MA)
            elif prev_row['short_ma'] > prev_row['long_ma'] and last_row['short_ma'] < last_row['long_ma']:
                print(">> SIGNAL SELL TERDETEKSI! <<")
                # self.place_sell_order(config.SYMBOL) # Uncomment untuk live trade
                print("(Simulasi) Order Sell dikirim.")
            
            else:
                print("Tidak ada sinyal trading saat ini.")
