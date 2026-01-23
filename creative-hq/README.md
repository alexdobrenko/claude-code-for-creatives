# Creative HQ

Your creative operations in one folder. Text files + AI = a system that actually works.

## What's Here

```
creative-hq/
├── CLAUDE.md      ← Context about you (fill this in first)
├── tasks.md       ← What you're working on
├── ideas.md       ← Brain dump inbox
├── inbox.md       ← Things that need attention (Chief of Staff reviews this)
├── projects.md    ← Your active projects
├── contacts.md    ← People who can help
├── wins.md        ← Things that worked
└── .claude/commands/
    ├── chief-of-staff.md → /chief-of-staff (the big one)
    ├── daily.md          → /daily
    ├── brain-dump.md     → /brain-dump
    ├── who-can-help.md   → /who-can-help
    └── win.md            → /win
```

## Setup (5 minutes)

1. [Install Claude Code](https://claude.ai/download) ($20/month)
2. Download this folder
3. Open `CLAUDE.md` and fill in your info
4. Open terminal, navigate here: `cd path/to/creative-hq`
5. Run `./start.sh` (or `./start-simple.sh` if you don't want tmux)
6. Try `/deck` to see your dashboard

### Two ways to launch

**Option A: Dashboard Mode** (recommended)
```bash
./start.sh
```
Opens a split-screen view: Claude on the left, your tasks and inbox live-updating on the right. Uses tmux.

**Option B: Simple Mode**
```bash
./start-simple.sh
```
Opens your folder in your editor + starts Claude. No fancy layout.

## How to Use It

### Daily workflow

1. **Morning:** Run `/daily` — get your focus for the day
2. **Throughout the day:** Dump thoughts into `ideas.md` (voice notes, random ideas, whatever)
3. **When you have time:** Run `/brain-dump` to sort your ideas into the right files
4. **When something works:** Run `/win` to capture why

### The commands

| Command | What it does |
|---------|--------------|
| `/deck` | Quick visual dashboard — see everything at a glance |
| `/chief-of-staff` | Full briefing on your creative work — what needs attention, what's going well, what you might be avoiding |
| `/daily` | "What should I focus on today?" |
| `/brain-dump` | Sort messy thoughts into the right files |
| `/who-can-help` | Find people in your network for what you need |
| `/win` | Record something that worked |

**Start with `/deck`** to see the lay of the land. **Use `/chief-of-staff`** when you want a real briefing with recommendations.

### Or just talk

You don't have to use commands. Just open Claude and say what's on your mind:

- "Help me figure out what to do with this project"
- "I need to write an email to [person], here's the context..."
- "I'm stuck on [thing], what should I try?"

Claude reads your files and has context about your work.

## The Philosophy

**Everything in text files.** No apps to learn. No databases to manage. Just folders and markdown.

**AI does the routing.** Don't organize your thoughts — dump them in `ideas.md` and let Claude sort them later.

**Capture what works.** The `wins.md` file is your secret weapon. Most people forget what worked. You won't.

**Keep it small.** 3-5 active projects max. One folder. A few files. Simple beats complex.

---

Made with [Code for Creatives](https://botharetrue.com/code-for-creatives)
