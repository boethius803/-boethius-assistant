#!/bin/bash
# P/L Update Script - Run every 2 hours

# Read current prices and calculate P/L
# This is a placeholder - would need actual price fetching

MESSAGE="📊 P/L Update - $(date '+%H:%M UTC')

Open Positions:
| Coin | P/L |
|------|-----|
| ZEC | -1.50% |
| DOGE | +0.54% |
| TAO | 0% |
| LINK | 0% |

Total: -$9.60"

# Send via OpenClaw message
echo "$MESSAGE"
