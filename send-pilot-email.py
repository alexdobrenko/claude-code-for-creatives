#!/usr/bin/env python3
"""
Send the Code for Creatives pilot email via Loops
"""

import requests
import csv
import time

# API Configuration
API_KEY = "f81f185e5d12a09b7b08081e30ad8b07"
BASE_URL = "https://app.loops.so/api"

# Email content
EMAIL_SUBJECT = "I'm taking 5 people through this"
EMAIL_FROM = "Alex Dobrenko"

EMAIL_BODY_HTML = """
<p>Hey —</p>

<p>You signed up for Code for Creatives. I've been doing 1:1 calls and something clicked.</p>

<p>Here's what I've built for myself with Claude Code:</p>

<ul>
<li>A blog that publishes with one keystroke — write in Obsidian, hit a shortcut, it's live</li>
<li>An invoicing tool for client work</li>
<li>An email drip campaign for a zine — 57 emails, custom timing, no ConvertKit needed</li>
<li>A "Chief of Staff" command that reads all my projects and tells me what to focus on</li>
<li>Voice-to-markdown transcription that turns rambling into organized notes</li>
<li>A chatbot intake form (the one you signed up through)</li>
</ul>

<p>I showed this to <a href="https://pmillerd.com">Paul Millerd</a> last week. He watched me publish a blog post in 3 seconds and said:</p>

<p><strong>"Oh my God. This changes everything."</strong></p>

<p>So I'm running a pilot cohort: <strong>5 creatives, 4 weeks, 4 group calls.</strong></p>

<p>We'll build your Creative HQ together — and you'll learn from seeing what everyone else is building too.</p>

<p>By the end you'll have:</p>
<ul>
<li>Claude Code as your creative command center</li>
<li>A publishing flow from your notes → your own site</li>
<li>Custom tools for YOUR workflows</li>
<li>A system that grows with you</li>
</ul>

<p>5 spots. $500. And you'll get lifetime access to the course I'm building from this — you're helping me figure out what to teach.</p>

<p>If you're interested, just reply to this email.</p>

<p>— Alex</p>
"""

EMAIL_BODY_TEXT = """Hey —

You signed up for Code for Creatives. I've been doing 1:1 calls and something clicked.

Here's what I've built for myself with Claude Code:

- A blog that publishes with one keystroke — write in Obsidian, hit a shortcut, it's live
- An invoicing tool for client work
- An email drip campaign for a zine — 57 emails, custom timing, no ConvertKit needed
- A "Chief of Staff" command that reads all my projects and tells me what to focus on
- Voice-to-markdown transcription that turns rambling into organized notes
- A chatbot intake form (the one you signed up through)

I showed this to Paul Millerd (https://pmillerd.com) last week. He watched me publish a blog post in 3 seconds and said:

"Oh my God. This changes everything."

So I'm running a pilot cohort: 5 creatives, 4 weeks, 4 group calls.

We'll build your Creative HQ together — and you'll learn from seeing what everyone else is building too.

By the end you'll have:
- Claude Code as your creative command center
- A publishing flow from your notes → your own site
- Custom tools for YOUR workflows
- A system that grows with you

5 spots. $500. And you'll get lifetime access to the course I'm building from this — you're helping me figure out what to teach.

If you're interested, just reply to this email.

— Alex
"""


def load_emails_from_csv(filepath):
    """Load and dedupe emails from Tally CSV export"""
    emails = set()

    with open(filepath, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            email = row.get("What's ur email ", "").strip().lower()
            # Basic validation
            if email and "@" in email and "." in email:
                # Fix common typos
                if email.endswith(".con"):
                    email = email[:-4] + ".com"
                if email.endswith(".co") and not email.endswith(".co.uk"):
                    # Check if it's a typo (gmail.co -> gmail.com)
                    if "gmail.co" in email or "yahoo.co" in email:
                        email = email + "m"
                emails.add(email)

    return list(emails)


def add_contact_to_loops(email, user_group="CodeForCreatives"):
    """Add contact to Loops with user group"""
    endpoint = f"{BASE_URL}/v1/contacts/update"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "email": email,
        "userGroup": user_group,
        "source": "Code for Creatives Waitlist"
    }

    try:
        response = requests.post(endpoint, headers=headers, json=data)
        return response.status_code == 200
    except:
        return False


def send_transactional_email(email):
    """Send transactional email via Loops"""
    endpoint = f"{BASE_URL}/v1/transactional"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "transactionalId": "cm5sfzfwt00gxti8o39hytlh6",  # You'll need to create this in Loops
        "email": email,
        "dataVariables": {}
    }

    try:
        response = requests.post(endpoint, headers=headers, json=data)
        return response.status_code == 200, response.text
    except Exception as e:
        return False, str(e)


def main():
    csv_path = "/Users/sash/Downloads/Claude Code for creatives _Submissions_2026-01-11.csv"

    print("📧 Code for Creatives - Pilot Email Sender")
    print("=" * 50)

    # Load emails
    emails = load_emails_from_csv(csv_path)
    print(f"\n✓ Loaded {len(emails)} unique emails from CSV")

    # Show preview
    print("\n📋 Email preview:")
    print("-" * 50)
    print(f"Subject: {EMAIL_SUBJECT}")
    print("-" * 50)
    print(EMAIL_BODY_TEXT[:500] + "...")
    print("-" * 50)

    # Confirm
    print(f"\n⚠️  About to send to {len(emails)} people")
    confirm = input("Type 'SEND' to confirm: ")

    if confirm != "SEND":
        print("Aborted.")
        return

    # First, add all contacts to Loops
    print("\n📥 Adding contacts to Loops...")
    for email in emails:
        success = add_contact_to_loops(email)
        status = "✓" if success else "✗"
        print(f"  {status} {email}")
        time.sleep(0.1)  # Rate limiting

    print("\n" + "=" * 50)
    print("✅ Contacts added to Loops under 'CodeForCreatives' group")
    print("\n👉 NEXT STEP:")
    print("   Go to Loops dashboard → Create a campaign → Target 'CodeForCreatives' group")
    print("   Or create a transactional template and update the ID in this script")
    print("=" * 50)


if __name__ == "__main__":
    main()
