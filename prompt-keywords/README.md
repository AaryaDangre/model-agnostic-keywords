# Prompt Keywords — Model-Agnostic

This repository contains a consolidated, deduplicated set of model-agnostic prompting keywords and short guidance to help create, optimize, and maintain prompts across multiple LLMs.

Files
- `keywords.md` — human-readable categorized keyword list.
- `keywords.yml` — machine-friendly YAML listing of keywords by category.
- `LICENSE` — MIT license.
- `.gitignore` — small default ignore file.
 - `Model Agnostic Prompting Keywords_*.txt` — vendor-specific keyword files (one per vendor)

Usage
- Refer to `keywords.md` when building or refining prompts.
- Import `keywords.yml` into scripts or tools that generate prompts automatically.

Vendor files
- The repository keeps vendor-specific files named `Model Agnostic Prompting Keywords_<VENDOR>_<VERSION>.txt`.
- Current vendor files included:
	- `Model Agnostic Prompting Keywords_ChatGPT_V0.txt`
	- `Model Agnostic Prompting Keywords_ChatGPT_Reliability_and_control_keywords.txt`
	- `Model Agnostic Prompting Keywords_Claude_V4.txt`
	- `Model Agnostic Prompting Keywords_Copilot_V1.txt`
	- `Model Agnostic Prompting Keywords_Gemini_V3.txt`
	- `Model Agnostic Prompting Keywords_Grok_V5.txt`
	- `Model Agnostic Prompting Keywords_Perplexity_V2.txt`

How to push to GitHub
1. Create an empty repository on GitHub (or provide an existing remote URL).
2. From this workspace root run (or allow me to run):

```powershell
git init
git add "prompt-keywords"
git commit -m "chore: add prompt keywords and docs"
git remote add origin <YOUR_GITHUB_REMOTE_URL>
git branch -M main
git push -u origin main
```

If you want, I can run these steps for you — you will be prompted to authenticate when pushing.

Contributing
- Open an issue or PR in the repo. Keep keywords single-line and add a short `source:` note when adding new items.

License: MIT
