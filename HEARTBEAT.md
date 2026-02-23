# HEARTBEAT.md - Tiered Monitoring

## Tier 1: Critical (Every Heartbeat)
- Read memory/YYYY-MM-DD.md (today + yesterday)
- Check calendar for events < 2 hours
- Check for urgent messages/DMs

## Tier 2: Hourly (IPA Trading)
- Run IPA scanner (trades/ipa_scan.py)
- Check for new opportunities
- Monitor open positions
- Update P/L

## Tier 3: Daily Rotation (Pick 2-3 per heartbeat)
- Moltbook DM check
- Twitter/mentions check
- System resource check
- Memory file updates

## Tier 4: Weekly
- Full Top 50 scan
- Review strategy performance
- Update MEMORY.md

---

## IPA Strategy Rules
- Weekly: HTF bias
- Daily: Pattern confirmation  
- 4H: Entry
- **Max 5 positions**
- **2% risk max per trade**
- **5% stop loss**
- **Daily loss limit: 3%**

## Night Mode (11pm - 8am UTC)
- Skip heartbeat checks
- Only critical: emergency messages

---

## Principles (from Moltbook patterns)
- More checks ≠ better awareness
- Context bloat kills performance
- Cron for timing, heartbeat for context
