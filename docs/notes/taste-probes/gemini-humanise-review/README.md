# Gemini 3.1 Pro — humanise review pack

**Blocked in cloud:** this VM has neither `agy` nor `GEMINI_API_KEY` / `GOOGLE_API_KEY`.
Per charter, the drafting agent must **not** fake an independent Gemini review.

## What’s ready

- `paragraphs/case*.md` — one file per P7-revised example (Cases 1, 3–10)
- `PROMPT.md` — humanise brief (econ register / P7 intention; **not** detector score)
- `run_gemini_humanise.py` — calls `gemini-3.1-pro-preview` when a key is set
- `out/` — empty until a run succeeds

## Run (your machine or after exporting a key here)

```bash
export GEMINI_API_KEY='…'   # or GOOGLE_API_KEY
cd /path/to/writing-with-ai
uv run --with google-genai python docs/notes/taste-probes/gemini-humanise-review/run_gemini_humanise.py
```

Or with Antigravity, for each file:

```bash
agy -p "$(cat docs/notes/taste-probes/gemini-humanise-review/PROMPT.md)
Review @docs/notes/taste-probes/gemini-humanise-review/paragraphs/CASE.md." \
  --add-dir docs/notes/taste-probes/gemini-humanise-review
```

Paste outputs into `out/` or reply in chat; we will synthesize kills into P7.
