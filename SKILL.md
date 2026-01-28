# Starter Skill — Build Your Creative HQ

This skill helps you create your first personalized Claude Code skill through a simple Q&A.

## When to Use
Run `/starter` when someone has just installed Claude Code and wants to create their first skill.

## What to Do

Walk them through these questions conversationally. After they answer, generate a personalized skill file for them.

### Questions to Ask

1. **"What's your name?"**

2. **"What do you create? (writer, designer, musician, maker, etc.)"**

3. **"What are you working on right now? Any projects, ideas, or things you're trying to figure out?"**

4. **"What's one annoying thing in your workflow you wish was easier?"**

5. **"How do you like to work? Any preferences Claude should know about?"**
   - Examples: "I like short answers" / "I work in markdown" / "I hate corporate speak"

### After They Answer

Generate a skill file called `my-hq` with this structure:

```markdown
# [Name]'s Creative HQ

## Who I Am
[Their name], [what they create]

## What I'm Working On
[Their current projects/ideas]

## Pain Points
[The annoying thing they mentioned]

## How I Like to Work
[Their preferences]

## Quick Commands
When I say...
- "status" → Remind me what I'm working on and what's next
- "ideas" → Help me brainstorm based on my projects
- "stuck" → Help me get unstuck on [their pain point area]
```

### Then Tell Them

1. Save this to `~/.claude/skills/my-hq/SKILL.md`
2. Now when you start Claude Code, it knows who you are
3. You can run `/my-hq` anytime to load this context
4. **You just built your first skill.**

### Wrap Up

Ask: "Want to try it? Type `/my-hq` and ask Claude something about your project."
