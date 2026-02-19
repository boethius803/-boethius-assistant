# HEARTBEAT.md - Tiered Monitoring

## Tier 1: Critical (Every Heartbeat)
- Read memory/YYYY-MM-DD.md (today + yesterday)
- Check calendar for events < 2 hours
- Check for urgent messages/DMs

## Tier 2: Daily Rotation (Pick 2-3 per heartbeat)
- Moltbook DM check
- Twitter/mentions check
- System resource check
- Memory file updates

## Tier 3: Weekly (Sunday)
- Review MEMORY.md for staleness
- Archive old daily memory files
- Update documentation

## Night Mode (11pm - 8am UTC)
- Skip heartbeat checks
- Only critical: emergency messages

---

## Principles (from Moltbook patterns)
- More checks ≠ better awareness
- Context bloat kills performance
- Cron for timing, heartbeat for context
