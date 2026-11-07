---
name: ig-reel
description: Write an Instagram Reel script from a raw idea: 5 hook options off 21 formulas, scored, then the full spoken script with retention beats marked. Use for 'write a reel', 'script this idea', 'reel about X'.
---

# /ig-reel

**Setup:** read `~/.claude/instagram/voice.md` first. If missing, ask the user to fill `templates/voice.md` or paste 3 of their captions. Never invent metrics: if a number is needed and not given, ask or write the line without it.

## Steps
1. Restate the idea in one line + the single viewer outcome.
2. Write 5 hooks from `~/.claude/instagram/references/hook-formulas.md` (different formulas; name each). Score each: `python3 ~/.claude/instagram/tools/hookscore.py "<hook>"`. Show as a table: # | formula | hook | score.
3. User picks (or take top score). Write script: HOOK (0-2s, spoken + on-screen text) | CONTEXT (2-5s) | BODY (beats, one idea each) | PAYOFF | CTA (save/share/comment, one ask).
4. Mark a retention beat (visual change, reveal, or open loop) every ~3-5s.
5. Give spoken word count; ask for target length instead of assuming one.
Rules: no filler openers; payoff promised in line one; spoken-language sentences.

**Output contract:** end with ONE copy-ready block, then ask: **Ship it, or change it?** Nothing is posted by Claude; the user posts.
