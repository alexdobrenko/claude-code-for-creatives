# Deck — Quick Dashboard View

Show me a quick overview of everything in my Creative HQ.

## Instructions

Read all my files and display a dashboard-style summary:

```
╔══════════════════════════════════════════════════════════════╗
║                      CREATIVE HQ                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                               ║
║  📋 TASKS TODAY                    📥 INBOX                   ║
║  ─────────────                     ──────                     ║
║  • [task 1]                        • [item 1]                 ║
║  • [task 2]                        • [item 2]                 ║
║                                                               ║
║  🎯 ACTIVE PROJECTS                👥 RECENT CONTACTS         ║
║  ────────────────                  ────────────────           ║
║  • Project 1 (status)              • Name - good for X        ║
║  • Project 2 (status)                                         ║
║                                                               ║
║  ⭐ RECENT WIN                                                ║
║  ───────────                                                  ║
║  [Most recent win from wins.md]                               ║
║                                                               ║
╚══════════════════════════════════════════════════════════════╝
```

## What to show

1. **Tasks Today** — Items from `tasks.md` under "Today" (max 5)
2. **Inbox** — Items from `inbox.md` that need attention (max 3)
3. **Active Projects** — Projects from `projects.md` with status "In progress" (max 3)
4. **Recent Contacts** — Last 2-3 contacts added or most relevant to current projects
5. **Recent Win** — The most recent entry from `wins.md`

Keep it to ONE SCREEN. This is a glance, not a deep dive.

If something is empty, just say "Nothing here" — don't hide the section.

After showing the dashboard, ask: "What do you want to dig into?"
