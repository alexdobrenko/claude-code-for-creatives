# The Vomit Pipeline: How I Publish Blog Posts in 3 Seconds

I showed someone my blog publishing workflow last week. He watched me write something in Obsidian, run a command, and see it live on my site.

His response: "Oh my God. This changes everything."

And I'm sitting there like... it's just a bash script? But okay.

Here's how it works.

---

## The Problem

I used to hate publishing.

Write something → copy it → paste it into WordPress or Substack or whatever → format it → add images → click buttons → wait → publish → realize there's a typo → go back → fix it → republish → hate myself.

The friction killed me. I'd write something, feel good about it, then lose all momentum in the publishing step. Half my drafts died there.

So I built something dumb and simple that removes all of it.

---

## The Setup

![The Vomit Pipeline](/images/publishing-flow-diagram.svg)

**The pieces:**

1. **Obsidian** — where I write everything. Just a folder of markdown files.

2. **A vault folder** — a specific folder that syncs to my blog. Anything I put here can be published.

3. **Stop markers** — this is the trick. I can write `## original` or `## draft` or `## private` anywhere in a post, and everything *below* that line stays private. Only the stuff above gets published.

4. **sync.sh** — one script that does everything: converts Obsidian formatting to Hugo formatting, copies images, builds the site.

5. **Hugo** — a static site generator. Fast, simple, just turns markdown into HTML.

6. **Netlify** — hosts the site. When I push to git, it auto-deploys.

---

## The Workflow

**Writing:**
- I write in Obsidian like normal
- When something feels ready, I drop it in the vault folder
- If I want to keep drafts/notes at the bottom, I add `## draft` and keep writing below it

**Publishing:**
```bash
./sync.sh
git add . && git commit -m "new post" && git push
```

That's it. Two commands. Site is live.

---

## The Stop Markers Thing

This is my favorite part.

I write messy. I have notes at the bottom of posts. Earlier drafts. Links I want to remember. Stuff that's not ready.

Instead of cleaning all that up before publishing, I just add:

```
## draft
```

And everything below that line is invisible to the sync script. It only publishes what's above the marker.

So my file can look like:

```markdown
# My Post Title

The actual post content goes here.
Blah blah blah this is the good stuff.

## draft

ok so this part sucks, need to rewrite

maybe add something about X?

old version:
[terrible first draft]
```

And only the top part gets published. The rest stays in my file but never sees the light of day.

This lets me keep everything in one place without worrying about accidentally publishing garbage.

---

## What the Script Actually Does

Here's the basic flow:

1. **Find all markdown files** in the vault folder
2. **Strip existing front matter** (the metadata at the top of posts)
3. **Look for stop markers** — if it finds `## original`, `## draft`, `## private`, or `## stop`, it only keeps content above that line
4. **Convert Obsidian image links** — `![[image.png]]` becomes `![Image](/images/image.png)`
5. **Add Hugo front matter** — title, date, tags, etc.
6. **Copy all images** to the static folder
7. **Build the Hugo site**

The whole thing runs in like 2 seconds.

---

## Problems I Hit

**Front matter hell.** Hugo is picky about front matter format. I spent way too long figuring out that it wanted TOML (`+++`) not YAML (`---`). Built a separate script just to convert old posts.

**Image paths.** Obsidian uses `![[image.png]]` but Hugo wants `![alt](/images/image.png)`. The script handles this now but I broke it multiple times.

**Special characters in filenames.** I name files like a psychopath. Asterisks, quotes, colons. The script had to learn to handle my chaos.

**The "it works on my machine" problem.** Hardcoded paths everywhere. If you want to use this, you'll need to change the paths to match your setup.

---

## Why This Matters

It's not about saving 5 minutes.

It's about removing the gap between "I wrote something" and "it's published."

When publishing is frictionless, I publish more. I don't overthink. I don't let things rot in drafts. I just... put stuff out there.

The writing stays where I want it (Obsidian). The site stays where I want it (my own domain). And the publishing happens in the terminal where I'm already working.

No copy-pasting. No clicking through UIs. No context-switching.

Write. Command. Live.

---

## The Code

If you want to build something like this, here's the sync script. It's not pretty but it works.

```bash
#!/bin/bash

VAULT_DIR="/path/to/your/vault"
BLOG_DIR="/path/to/your/hugo/blog"
POSTS_DIR="$BLOG_DIR/content/posts"
STATIC_DIR="$BLOG_DIR/static/images"

# Process each markdown file
find "$VAULT_DIR" -name "*.md" | while read -r file; do
    content=$(cat "$file")

    # Check for stop markers and extract publishable content
    if echo "$content" | grep -q "## original\|## draft\|## private\|## stop"; then
        stop_line=$(echo "$content" | grep -n "## original\|## draft\|## private\|## stop" | head -1 | cut -d: -f1)
        content=$(echo "$content" | head -n $((stop_line - 1)))
    fi

    # Convert Obsidian images to Hugo format
    content=$(echo "$content" | sed 's/!\[\[\([^]]*\)\]\]/![Image](\/images\/\1)/g')

    # Add front matter and save
    # ... rest of the processing
done

# Copy images
find "$VAULT_DIR" -type f \( -name "*.png" -o -name "*.jpg" \) -exec cp {} "$STATIC_DIR/" \;

# Build
hugo
```

---

## What I'd Do Differently

If I were starting over:

1. **Use a keyboard shortcut** instead of typing commands. I should really just bind this to a hotkey.

2. **Auto-commit on sync.** Why am I typing git commands? The script should just do it.

3. **Better image handling.** Right now it copies ALL images every time. Should probably be smarter about that.

4. **RSS to Substack.** I want my blog to be home base but also push to Substack automatically. Haven't figured this out yet.

---

## The Point

You don't need a fancy CMS. You don't need to learn a new editor. You don't need to change how you write.

You just need a script that takes your files and puts them somewhere.

That's it. That's the whole trick.

Write where you want. Publish with a command. Own your stuff.

The vomit pipeline isn't pretty. But it works. And it gets out of my way.

Which is all I really wanted.
