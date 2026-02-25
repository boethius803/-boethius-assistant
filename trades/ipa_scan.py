#!/usr/bin/env python3
"""
IPA Scanner - Extended Top Coins
Uses Binance + Kraken
"""
import urllib.request, json

# Extended coin list
BINANCE = {
    'BTC': 'BTCUSDT', 'ETH': 'ETHUSDT', 'BNB': 'BNBUSDT', 'SOL': 'SOLUSDT',
    'XRP': 'XRPUSDT', 'ADA': 'ADAUSDT', 'DOGE': 'DOGEUSDT', 'LTC': 'LTCUSDT',
    'TRX': 'TRXUSDT', 'DOT': 'DOTUSDT', 'LINK': 'LINKUSDT', 'AVAX': 'AVAXUSDT',
    'UNI': 'UNIUSDT', 'ATOM': 'ATOMUSDT', 'NEAR': 'NEARUSDT', 'APT': 'APTUSDT',
    'ARB': 'ARBUSDT', 'OP': 'OPUSDT', 'MATIC': 'MATICUSDT', 'TAO': 'TAOUSDT'
}

KRAKEN = {'XMR': 'XMRUSD', 'BCH': 'BCHUSD', 'KAS': 'KASUSD'}

def scan_binance_tf(tf, interval):
    def get_data(symbol):
        url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit=50'
        return json.loads(urllib.request.urlopen(url).read())
    
    def find_swings(candles, window=3):
        swings = []
        for i in range(window, len(candles) - window):
            high, low = float(candles[i][2]), float(candles[i][3])
            prev_h = [float(candles[j][2]) for j in range(max(0,i-window), min(len(candles),i+window+1)) if j != i]
            prev_l = [float(candles[j][3]) for j in range(max(0,i-window), min(len(candles),i+window+1)) if j != i]
            if high > max(prev_h): swings.append(('SH', high))
            if low < min(prev_l): swings.append(('SL', low))
        return swings
    
    def analyze(swings):
        recent = swings[-8:]
        shs = [s[1] for s in recent if s[0] == 'SH']
        sls = [s[1] for s in recent if s[0] == 'SL']
        if len(shs) >= 2 and len(sls) >= 2:
            if shs[-1] > shs[-2] and sls[-1] > sls[-2]: return "BULLISH"
            if shs[-1] < shs[-2] and sls[-1] < sls[-2]: return "BEARISH"
        return "MIXED"
    
    return {s: analyze(find_swings(get_data(p))) for s, p in BINANCE.items()}

def scan_kraken_tf(tf, interval):
    def get_data(symbol):
        url = f'https://api.kraken.com/0/public/OHLC?pair={symbol}&interval={interval}&count=50'
        return list(json.loads(urllib.request.urlopen(url).read())['result'].values())[0]
    
    def find_swings(candles, window=3):
        swings = []
        for i in range(window, len(candles) - window):
            high, low = float(candles[i][2]), float(candles[i][3])
            prev_h = [float(candles[j][2]) for j in range(max(0,i-window), min(len(candles),i+window+1)) if j != i]
            prev_l = [float(candles[j][3]) for j in range(max(0,i-window), min(len(candles),i+window+1)) if j != i]
            if high > max(prev_h): swings.append(('SH', high))
            if low < min(prev_l): swings.append(('SL', low))
        return swings
    
    def analyze(swings):
        recent = swings[-8:]
        shs = [s[1] for s in recent if s[0] == 'SH']
        sls = [s[1] for s in recent if s[0] == 'SL']
        if len(shs) >= 2 and len(sls) >= 2:
            if shs[-1] > shs[-2] and sls[-1] > sls[-2]: return "BULLISH"
            if shs[-1] < shs[-2] and sls[-1] < sls[-2]: return "BEARISH"
        return "MIXED"
    
    return {s: analyze(find_swings(get_data(p))) for s, p in KRAKEN.items()}

# Scan
w_b = scan_binance_tf("W", "1w")
d_b = scan_binance_tf("D", "1d")
h_b = scan_binance_tf("4H", "4h")

w_k = scan_kraken_tf("W", "10080")
d_k = scan_kraken_tf("D", "1440")
h_k = scan_kraken_tf("4H", "240")

print("=== IPA SCAN - EXTENDED ===")
print(f"{'Coin':<6} | {'Weekly':<8} | {'Daily':<8} | {'4H':<8}")
print("-" * 45)

all_coins = list(BINANCE.keys()) + list(KRAKEN.keys())
for sym in all_coins:
    w = w_b.get(sym, w_k.get(sym, 'ERR'))
    d = d_b.get(sym, d_k.get(sym, 'ERR'))
    h = h_b.get(sym, h_k.get(sym, 'ERR'))
    print(f"{sym:<6} | {w:<8} | {d:<8} | {h:<8}")

print("\n=== OPPORTUNITIES ===")
for sym in all_coins:
    w = w_b.get(sym, w_k.get(sym))
    d = d_b.get(sym, d_k.get(sym))
    h = h_b.get(sym, h_k.get(sym))
    if w == d == h == "BULLISH":
        print(f"🟢 {sym}: BULLISH ALL TFs")
    elif w == d == "BULLISH":
        print(f"🟡 {sym}: BULLISH W+D")
    elif w == "BULLISH":
        print(f"🟡 {sym}: BULLISH Weekly")
