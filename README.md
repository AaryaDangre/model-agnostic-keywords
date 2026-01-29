# model-agnostic-keywords

[![CI](https://github.com/AaryaDangre/model-agnostic-keywords/workflows/CI/badge.svg)](https://github.com/AaryaDangre/model-agnostic-keywords/actions)

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

Releases
- Releases are created automatically when you push a git tag matching `v*` (e.g., `v0.1.0`).
- Each release includes compiled JSON/YAML and markdown outputs.
- See [CHANGELOG.md](CHANGELOG.md) for version history.

How to create a release:
```bash
git tag v0.2.0
git push origin v0.2.0
```

Contributing
- Add or update vendor files under `prompt-keywords/` and open a PR.
- Keep each keyword on its own line and add a short `source:` note when adding new items.
- Run `python -m scripts.compile_keywords` before committing vendor changes.

License
- MIT — see `prompt-keywords/LICENSE`.

Contact
- Repository: https://github.com/AaryaDangre/model-agnostic-keywords
