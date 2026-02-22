# Crypto Trading Strategy

**Active Strategy:** Combined SMC + Sniper (strategy-combined.md)

---

## Strategy Reference

All trading follows the **Combined SMC + Sniper Strategy** documented in:
- `trades/strategy-combined.md` — Full strategy guide
- `trades/strategy-sniper-ipa.html` — Visual HTML version

---

## Quick Rules (From Combined Strategy)

### Core Filters
- HTF structure confirmed (Daily/4H)
- Pattern recognized (QM, Fakeout, Stop Hunt, etc.)
- 2+ confluences required
- R:R ≥ 1:2

### Risk Management
- Max 1-2% risk per trade
- Max 5% open risk total
- Daily loss limit: 3% → STOP TRADING

### Trade Management
- +1R: Move to BE, take 30-50% partial
- +2R: Take 25% more, trail to +1R
- +3R: Close or trail tight

---

## Pre-Trade Checklist

Run through `trades/strategy-combined.md` checklist before every entry:
- [ ] HTF structure identified
- [ ] Trade aligned with HTF bias
- [ ] Recognized pattern present
- [ ] 2+ confluences
- [ ] Stop loss defined
- [ ] R:R ≥ 1:2
- [ ] Position size ≤ 2% risk
- [ ] No revenge trading
- [ ] Clear mind

---

## Active Deploy Scan

See: `trades/smc-scan-top50.md` for current setups

---

*Previous momentum-only strategy deprecated. Now using combined SMC + Sniper approach.*
