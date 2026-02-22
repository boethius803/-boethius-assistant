# AI Email Generator SaaS
## Built with Chutes.ai

*Start Date: 2026-02-22*

---

## What It Does
AI-powered tool that generates professional emails in seconds using Chutes.ai (DeepSeek-R1 model)

---

## Tech Stack

| Component | Tool |
|-----------|------|
| Builder | Bubble.io (no-code) |
| AI | Chutes.ai (DeepSeek-R1) |
| Hosting | Bubble (free) |
| Domain | Namecheap ($12/yr) |

---

## MVP Features

### Input Fields
- **Recipient name** — Who you're emailing
- **Purpose** — Sales, follow-up, intro, support, other
- **Tone** — Professional, friendly, casual, urgent
- **Key points** — What to include

### Output
- AI-generated email (via Chutes.ai)
- Copy button
- Regenerate button
- Save to history

---

## Revenue Model

| Tier | Price | Features |
|------|-------|----------|
| Free | $0 | 5 emails/month |
| Pro | $9/mo | Unlimited |
| Business | $29/mo | Team + templates |

---

## Chutes.ai Integration

```javascript
// API Call to Chutes.ai
URL: https://(chutes.ai/v1/chat/completions
Headers:
  - Authorization: Bearer YOUR_API_KEY
  - Content-Type: application/json
Body:
{
  "model": "deepseek-ai/DeepSeek-R1-0528-TEE",
  "messages": [
    {"role": "user", "content": "Write a [tone] email for [purpose]. Recipient: [name]. Key points: [points]"}
  ]
}
```

---

## To Do This Week

- [ ] Sign up Bubble.io
- [ ] Get Chutes.ai API key
- [ ] Build input form in Bubble
- [ ] Connect Chutes.ai API
- [ ] Test generation

---

*Paused - focusing on trading*
