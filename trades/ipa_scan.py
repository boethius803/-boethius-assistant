#!/usr/bin/env python3
"""
IPA Scanner - Runs hourly
Scans top coins for QM patterns and signals
"""
import urllib.request, json

PAIRS = {'XMR': 'XMRUSD', 'BCH': 'BCHUSD', 'SOL': 'SOLUSD', 'AVAX': 'AVAXUSD', 'LINK': 'LINKUSD', 'DOGE': 'DOGEUSD', 'ETH': 'ETHUSD', 'BTC': 'XXBTZUSD', 'ADA': 'ADAUSD', 'DOT': 'DOTUSD', 'UNI': 'UNIUSD', 'LTC': 'LTCUSD', 'XRP': 'XRPUSD'}

def get_price(sym):
    pair = PAIRS.get(sym)
    url = f'https://api.kraken.com/0/public/Ticker?pair={pair}'
    data = json.loads(urllib.request.urlopen(url).read())
    return float(list(data['result'].values())[0]['c'][0])

def scan_tf(tf, interval):
    def get_data(symbol):
        pair = PAIRS.get(symbol)
        url = f'https://api.kraken.com/0/public/OHLC?pair={pair}&interval={interval}&count=50'
        data = json.loads(urllib.request.urlopen(url).read())
        return list(data['result'].values())[0]
    
    def find_swings(candles, window=3):
        swings = []
        for i in range(window, len(candles) - window):
            high, low = float(candles[i][2]), float(candles[i][3])
            prev_highs = [float(candles[j][2]) for j in range(max(0,i-window), min(len(candles),i+window+1)) if j != i]
            prev_lows = [float(candles[j][3]) for j in range(max(0,i-window), min(len(candles),i+window+1)) if j != i]
            if high > max(prev_highs): swings.append(('SH', high))
            if low < min(prev_lows): swings.append(('SL', low))
        return swings
    
    def analyze(swings):
        recent = swings[-8:]
        shs = [s[1] for s in recent if s[0] == 'SH']
        sls = [s[1] for s in recent if s[0] == 'SL']
        if len(shs) >= 2 and len(sls) >= 2:
            if shs[-1] > shs[-2] and sls[-1] > sls[-2]: return "BULLISH"
            if shs[-1] < shs[-2] and sls[-1] < sls[-2]: return "BEARISH"
        return "MIXED"
    
    results = {}
    for sym in PAIRS.keys():
        try:
            data = get_data(sym)
            swings = find_swings(data[1:])
            results[sym] = analyze(swings)
        except:
            results[sym] = "ERROR"
    return results

# Scan all timeframes
weekly = scan_tf("W", "10080")
daily = scan_tf("D", "1440")
h4 = scan_tf("4H", "240")

print("=== IPA HOURLY SCAN ===")
print(f"{'Coin':<6} | {'Weekly':<8} | {'Daily':<8} | {'4H':<8}")
print("-" * 40)
for sym in PAIRS.keys():
    print(f"{sym:<6} | {weekly.get(sym, 'ERR'):<8} | {daily.get(sym, 'ERR'):<8} | {h4.get(sym, 'ERR'):<8}")

# Find opportunities
print("\n=== OPPORTUNITIES ===")
for sym in PAIRS.keys():
    w, d, h = weekly.get(sym), daily.get(sym), h4.get(sym)
    # Bullish on all 3
    if w == d == h == "BULLISH":
        print(f"🟢 {sym}: BULLISH ALL TFs")
    # Bullish weekly + daily
    elif w == d == "BULLISH":
        print(f"🟡 {sym}: BULLISH W+D")
    # Bearish on all 3
    elif w == d == h == "BEARISH":
        print(f"🔴 {sym}: BEARISH ALL TFs")
