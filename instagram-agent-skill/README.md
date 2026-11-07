# The Instagram agent skill
Eleven Claude skills that run an Instagram account. Free, MIT, no signup, no API key, nothing to connect.
Nothing posts. These skills write; you post. Every skill ends with a copy-ready block and one question: **ship it, or change it?**

## Install
Claude Code:
```
git clone <this repo> && cd instagram-agent-skill && ./install.sh
```
Copies skills to `~/.claude/skills/`, tools + references to `~/.claude/instagram/`, and seeds `voice.md`.
Project-local: copy the same folders into `.claude/skills/`. No Claude Code: paste any single SKILL.md at the top of a chat (you lose the Python tools).
Then fill in `voice.md` or say: "write my voice.md from these 3 captions".

## The eleven
| skill | does |
|---|---|
| /ig-reel | Reel script off 21 hook formulas; hook scored before you film |
| /ig-hook | Rewrite + score only the first 2 seconds, 5 options |
| /ig-caption | Caption linted for fold truncation, length, hashtags, CTA |
| /ig-carousel | Slide-by-slide carousel, one idea per slide, save-worthy last slide |
| /ig-cover | Cover text + caption first line linted as ONE pairing (no duplicate message) |
| /ig-edit | Edit decision list from your transcript: cuts, captions, b-roll beats |
| /ig-retention | Reads your Insights retention points, finds where viewers leave |
| /ig-comments | Triage comments, draft replies in your voice |
| /ig-research | Ranks niche posts by multiple of each creator's own median, names the formula |
| /ig-stories | Story sequence with sticker/poll beats |
| /ig-audit | Whole account → ONE fix, not twenty |

## Tools (stdlib Python, no installs)
`hookscore.py` `caption.py` `deadair.py` `retention.py` `outlier.py` `swipe.py`
- hookscore is a heuristic, not a predictor.
- Platform limits live in `tools/limits.json`. Instagram changes them; verify before trusting.
- Nothing invents a number. If a skill needs a figure you haven't given, it asks.
- Posting is not automated: Instagram's API doesn't allow unattended personal-account posting, and unattended posting is the wrong design anyway.

MIT.
