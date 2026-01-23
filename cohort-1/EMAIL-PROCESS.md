# Email Process — Code for Creatives

## The Flow

1. **Tell Claude what email you want to send** (audience, subject, content)
2. **Claude creates/updates the Resend audience** via API
3. **Claude creates the broadcast** via API
4. **You preview + send in Resend dashboard** → https://resend.com/broadcasts

## Key Details

- **Verified domain:** `hi.botharetrue.com`
- **From address:** `Alex Dobrenko <alex@hi.botharetrue.com>`
- **API key:** stored in send-welcome.py (or ask Claude to use it)

## Example Prompts

"Send a welcome email to cohort 1 with the survey link"

"Create an email to the waitlist announcing the next cohort"

"Send a reminder to cohort 1 about tomorrow's call"

## Audiences Created

| Audience | ID | Purpose |
|----------|-----|---------|
| Cohort 1 Buyers | c45f757d-05cd-4054-be33-6872cedc8de6 | 5 people who bought first cohort |

## Notes

- Resend rate limit: 2 requests/second (add delays when adding many contacts)
- Broadcasts appear in dashboard as drafts until you hit send
- Can preview before sending
