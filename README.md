# model-agnostic-keywords

Consolidated, vendor-labelled prompting keywords and short guidance for building and optimizing prompts across multiple LLMs.

Contents
- `prompt-keywords/` — primary folder containing:
  - `keywords.md` — human-readable, categorized keyword list.
  - `keywords.yml` — machine-friendly YAML list.
  - `Model Agnostic Prompting Keywords_<VENDOR>_<VERSION>.txt` — vendor-specific keyword files (one file per vendor).

Quick start
1. Clone the repo:

```bash
git clone https://github.com/AaryaDangre/model-agnostic-keywords.git
cd model-agnostic-keywords
```

2. Inspect keywords:

```bash
less prompt-keywords/keywords.md
```

Usage
- Use `prompt-keywords/keywords.yml` for programmatic imports.
- Use vendor files when you need model-specific phrasing or examples.

Contributing
- Add or update vendor files under `prompt-keywords/` and open a PR.
- Keep each keyword on its own line and add a short `source:` note when adding new items.

License
- MIT — see `prompt-keywords/LICENSE`.

Contact
- Repository: https://github.com/AaryaDangre/model-agnostic-keywords
