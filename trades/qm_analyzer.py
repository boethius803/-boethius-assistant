#!/usr/bin/env python3
"""
QM Analyzer - Kraken API
"""
import urllib.request, json
import pandas as pd
from datetime import datetime

PAIRS = {
    'BTC': 'XXBTZUSD', 'ETH': 'XETHZUSD', 'XMR': 'XXMRZUSD',
    'SOL': 'SOLUSD', 'AVAX': 'AVAXUSD', 'DOT': 'DOTUSD',
    'LINK': 'LINKUSD', 'ADA': 'ADAUSD', 'UNI': 'UNIUSD',
    'LTC': 'XLTCZUSD', 'BCH': 'XBCHZUSD', 'XRP': 'XXRPZUSD',
    'DOGE': 'XDGUSD'
}

TIMEFRAMES = {'15m': '15', '30m': '30', '1h': '60', '2h': '120', '4h': '240', '1d': '1440'}

def get_ohlc(symbol, timeframe='240', count=50):
    pair = PAIRS.get(symbol)
    if not pair:
        return None
    url = f'https://api.kraken.com/0/public/OHLC?pair={pair}&interval={timeframe}&count={count}'
    try:
        data = json.loads(urllib.request.urlopen(url).read())
        result = data['result']
        candles = result.get(pair) or list(result.values())[1]
        df = pd.DataFrame(candles[1:], columns=['time', 'open', 'high', 'low', 'vwap', 'volume', 'count', 'tradecount'])
        df['time'] = pd.to_datetime(df['time'], unit='s')
        for c in ['open', 'high', 'low', 'close']:
            df[c] = pd.to_numeric(df[c])
        return df.set_index('time')
    except Exception as e:
        print(f"Error {symbol}: {e}")
        return None

def find_swings(df, window=3):
    swings = []
    for i in range(window, len(df) - window):
        curr_high = df.iloc[i]['high']
        curr_low = df.iloc[i]['low']
        prev_highs = [df.iloc[j]['high'] for j in range(i-window, i+window+1) if j != i]
        prev_lows = [df.iloc[j]['low'] for j in range(i-window, i+window+1) if j != i]
        if curr_high > max(prev_highs):
            swings.append({'time': df.index[i], 'type': 'SH', 'price': curr_high})
        if curr_low < min(prev_lows):
            swings.append({'time': df.index[i], 'type': 'SL', 'price': curr_low})
    return swings

def analyze_structure(swings):
    if len(swings) < 4:
        return "⚪ UNCLEAR", None
    recent = swings[-8:]
    shs = [s['price'] for s in recent if s['type'] == 'SH']
    sls = [s['price'] for s in recent if s['type'] == 'SL']
    if len(shs) >= 2 and len(sls) >= 2:
        if shs[-1] > shs[-2] and sls[-1] > sls[-2]:
            return "🟢 BULLISH (HH+HL)", (shs, sls)
        elif shs[-1] < shs[-2] and sls[-1] < sls[-2]:
            return "🔴 BEARISH (LH+LL)", (shs, sls)
    return "⚪ MIXED", (shs, sls)

def scan(symbols, timeframe='240'):
    print(f"\n{'='*60}")
    print(f"QM SCAN - {timeframe} timeframe")
    print(f"{'='*60}\n")
    results = []
    for sym in symbols:
        df = get_ohlc(sym, timeframe, 50)
        if df is None:
            continue
        swings = find_swings(df)
        struct, (shs, sls) = analyze_structure(swings)
        price = df.iloc[-1]['close']
        print(f"{sym:6} | ${price:>10.2f} | {struct}")
        results.append({'symbol': sym, 'price': price, 'structure': struct, 'shs': shs, 'sls': sls})
    return results

if __name__ == "__main__":
    coins = list(PAIRS.keys())
    scan(coins, '240')
