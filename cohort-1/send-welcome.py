#!/usr/bin/env python3
"""
Send welcome email to Code for Creatives Cohort 1 buyers via Resend
"""

import requests

# Resend API Configuration
API_KEY = "re_CeXNMRgg_JbWK5Qzc2sed1XLBVXRnoqa1"
BASE_URL = "https://api.resend.com"

# Cohort 1 buyers
BUYERS = [
    "antoinemestrallet@gmail.com",
    "nikita.s.petrov@gmail.com",
    "meghnamann@gmail.com",
    "alex@goodword.com",
    "chrisdantonio3@gmail.com"
]

# Email content
EMAIL_SUBJECT = "You're in — next steps"
FROM_EMAIL = "Alex Dobrenko <alex@botharetrue.com>"

EMAIL_BODY_HTML = """
<p>Hey —</p>

<p>You're one of 5 people in the first Code for Creatives cohort. Thank you for trusting me with this.</p>

<p><strong>Quick survey (2 min):</strong> <a href="https://claude-cohort-survey.netlify.app/">https://claude-cohort-survey.netlify.app/</a></p>

<p>This helps me understand where you're starting from and what you want to build. Please fill it out before our first call.</p>

<p><strong>What happens next:</strong></p>
<ul>
<li>I'm finalizing dates for our 4 group calls (you'll get a calendar invite soon)</li>
<li>First call will be the week of Jan 27</li>
<li>Between now and then, get Claude Code installed if you haven't — I'll send simple instructions</li>
</ul>

<p><strong>What to expect:</strong></p>
<ul>
<li>4 group calls over 4 weeks</li>
<li>We'll build your Creative HQ together</li>
<li>You'll learn from seeing what everyone else is building too</li>
<li>Lifetime access to whatever course comes out of this</li>
</ul>

<p>If you have questions or want to say hi, just reply.</p>

<p>— Alex</p>
"""


def send_email(to_email):
    """Send email via Resend API"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "from": FROM_EMAIL,
        "to": [to_email],
        "subject": EMAIL_SUBJECT,
        "html": EMAIL_BODY_HTML
    }

    response = requests.post(f"{BASE_URL}/emails", headers=headers, json=data)
    return response.status_code == 200, response.json()


def main():
    print("📧 Code for Creatives — Cohort 1 Welcome Email")
    print("=" * 50)
    print(f"\nFrom: {FROM_EMAIL}")
    print(f"Subject: {EMAIL_SUBJECT}")
    print(f"\nRecipients ({len(BUYERS)} people):")
    for email in BUYERS:
        print(f"  • {email}")

    print("\n" + "-" * 50)
    print("Survey link: https://claude-cohort-survey.netlify.app/")
    print("-" * 50)

    # Confirm
    print(f"\n⚠️  Ready to send to {len(BUYERS)} people")
    confirm = input("Type 'SEND' to confirm: ")

    if confirm != "SEND":
        print("Aborted.")
        return

    # Send emails
    print("\n📤 Sending emails...")
    for email in BUYERS:
        success, response = send_email(email)
        status = "✓" if success else "✗"
        print(f"  {status} {email}")
        if not success:
            print(f"      Error: {response}")

    print("\n" + "=" * 50)
    print("✅ Done!")
    print("=" * 50)


if __name__ == "__main__":
    main()
