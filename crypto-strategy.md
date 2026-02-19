# Crypto Paper Trading System - Boethius v1
## Based on Jesse Livermore's Methods

## Goal
Paper trade top 100 crypto coins, track performance over time.

## Core Livermore Philosophy
1. **Trade with the trend** — never fight the market
2. **Wait for the pivotal point** — breakout from consolidation
3. **Let the market confirm** — pyramiding (add to winners)
4. **Cut losses quickly** — never let a loss grow
5. **Let profits run** — big money in waiting
6. **Trade leading stocks** — strongest in strongest sectors
7. **Cash is a position** — when in doubt, stay out
8. **Ignore tips** — only price action matters

## Rules

### 1. Portfolio
- Start with $10,000 virtual USD
- Max 5 positions at once
- Max 20% per coin
- Hold 50% cash (dry powder)

### 2. Entry Signals (Livermore Breakout + Momentum)

**Must have:**
- **Breakout:** Price breaks above recent range (high of last 5+ days)
- **Volume:** Volume > 1.5x average (confirms move)

**Plus 1+ of:**
- Weekly momentum >5% (trend alignment)
- Daily green (delta.day > 1.0)
- Volume spike 2x average
- Strong coin (top 50 by market cap)

**Livermore Phases to Watch:**
1. **Accumulation** — price ranging/sideways, low volatility
2. **Breakout** — price escapes range with volume (ENTRY)
3. **Advance** — trend continues
4. **Test** — pullback to breakout level (secondary entry or hold)
5. **Climax** — parabolic move, take profit zone

**Wait for breakout confirmation — don't chase extended prices!**

### 3. Exit Signals (Livermore + Momentum)

**Take Profit - LET PROFITS RUN:**
1. **Climax** — parabolic extension, volume spikes → EXIT MOSTLY
2. **Trailing stop** — let it run, exit when:
   - Price drops 5% from peak (lock in gains)
   - Lower high forms (trend reversing)
   - Daily closes below breakout level
3. **+15%** — conservative baseline (don't exit here unless needed)

**Stop Loss:**
- **-5%** hard stop → EXIT IMMEDIATELY

**NEVER:**
- Average down (Livermore's #1 rule)
- Take small profits on big moves
- Hold through clear reversal signals

**Key Livermore Exit Patterns:**
- Lower high after advance = trend reversing → EXIT
- Volume dries up on advance = exhaustion → EXIT
- Wide-range decline days = distribution starting → EXIT
- Test failed (rally to lower high) → EXIT

### 4. Position Sizing - Dynamic (Livermore Pyramiding)

**Base unit:** 10% of portfolio

**Livermore Pyramiding:**
- Initial position: 10%
- Add 2nd tranche (10%) when price moves +5% in your favor
- Add 3rd tranche (10%) when price moves +10% in your favor
- NEVER add if trade goes against you (never average down!)

**Win/Loss Scaling:**
| Result | Next Position Size |
|--------|-------------------|
| WIN (+15%+) | +50% (scale up) |
| WIN (5-15%) | +25% |
| WIN (<5%) | Same (10%) |
| LOSE | -50% (scale down) |

**Rules:**
- Never exceed 20% per coin
- Minimum position: 5% of portfolio
- Maximum: 5 positions max

**Example:**
- Start: $10,000 → 10% = $1,000 position
- Win +20%: portfolio = $10,200 → next = $1,500
- Win +20%: portfolio = $11,700 → next = $2,000 (max)
- Lose -5%: portfolio = $11,265 → next = $1,000 (min step)

### 5. Risk Management

- **Max 5 open positions** at any time
- **Max 2% risk per trade**
- **Max 10% total portfolio risk** (all positions combined)
- Never trade more than 50% portfolio at once
- Hold 50% in USD (dry powder)
- Rebalance weekly

### 6. Livermore Psychological Rules

- **Cash is a position** — when unsure, stay out
- **Never trade emotionally** — after loss, stress, or euphoria → step back
- **Be patient** — most money made in waiting
- **When in doubt, get out** — flatten and re-evaluate
- **Learn from losses** — every loss is tuition
- **Ignore tips** — only price action matters

---

## Livermore's Recording System (Simplified)

### The Six Columns
| Column | Phase | Action |
|--------|-------|--------|
| Secondary Rally | Small bounce in downtrend | Ignore |
| Natural Rally | Normal up move | Watch |
| **Upward Trend** | **Confirmed uptrend** | **BUY** |
| **Downward Trend** | **Confirmed downtrend** | **SHORT/SELL** |
| Natural Reaction | Normal pullback | Watch |
| Secondary Reaction | Small dip in uptrend | Ignore |

### The 6-Point Threshold (Adapted for Crypto)
- Use % moves: ~5-10% price move shifts columns
- For crypto: require 2 coins in same sector to confirm = Key
- When price shifts from Downward → Upward Trend column = BUY signal
- When price shifts from Upward → Downward Trend column = SELL signal

### Simplified Tracking
| Phase | Action |
|-------|--------|
| Accumulation | Watch, don't trade |
| Breakout | ENTER (small) |
| Advance | ADD (pyramid) |
| Test hold | HOLD / ADD |
| Climax | EXIT |
| Decline | CASH / WAIT |

---

## Scoring
- Track: ROI %, win rate, total trades
- Weekly report to user

## Coins to Watch
Top 100 by market cap. Focus on:
- BTC, ETH (foundation)
- 3-5 altcoins with good volume

---

## Next Steps
1. Get live prices (need API or manual input)
2. User approves trades
3. I execute & track in `trades/`
