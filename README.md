# model-agnostic-keywords

[![CI](https://github.com/AaryaDangre/model-agnostic-keywords/workflows/CI/badge.svg)](https://github.com/AaryaDangre/model-agnostic-keywords/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A consolidated, vendor-labeled library of prompting keywords and techniques that work across multiple AI language models (ChatGPT, Claude, Copilot, Gemini, Grok, Perplexity).

## Overview

This repository provides a curated collection of model-agnostic prompting keywords to help developers, researchers, and AI practitioners build more effective prompts. Whether you're working with ChatGPT, Claude, Gemini, or any other LLM, these keywords provide a consistent vocabulary for crafting better prompts.

## Contents

- **`prompt-keywords/keywords.md`** — Human-readable, categorized keyword list organized by purpose
- **`prompt-keywords/keywords.yml`** — Machine-friendly YAML format for programmatic use
- **`prompt-keywords/combined_keywords.json`** — Compiled JSON with all vendor keywords and metadata
- **Vendor-specific files** — Individual keyword collections for ChatGPT, Claude, Copilot, Gemini, Grok, and Perplexity

## Quick Start
1. Clone the repo:

```bash
git clone https://github.com/AaryaDangre/model-agnostic-keywords.git
cd model-agnostic-keywords
```

2. Inspect keywords:

```bash
less prompt-keywords/keywords.md
```

## Usage

### For Humans
Browse [prompt-keywords/keywords.md](prompt-keywords/keywords.md) when crafting prompts. Keywords are organized into categories like:
- Role & Persona
- Reasoning & Chain-of-Thought
- Output Formatting
- Quality & Verification
- And more...

### For Developers
Import `prompt-keywords/keywords.yml` or `prompt-keywords/combined_keywords.json` for programmatic prompt generation.

### Vendor-Specific Guidance
Check vendor files in `prompt-keywords/` when you need model-specific examples or phrasing optimized for a particular LLM.

## Features

✅ **Model-agnostic** — Keywords work across ChatGPT, Claude, Gemini, Grok, Perplexity, and Copilot
✅ **Categorized** — Organized by purpose (reasoning, formatting, quality control, etc.)
✅ **Metadata included** — Each vendor file includes source, version, and tags
✅ **Machine-readable** — JSON/YAML formats for automation
✅ **CI/CD ready** — Automated validation and releases via GitHub Actions

## Releases
- Releases are created automatically when you push a git tag matching `v*` (e.g., `v0.1.0`).
- Each release includes compiled JSON/YAML and markdown outputs.
- See [CHANGELOG.md](CHANGELOG.md) for version history.

How to create a release:
```bash
git tag v0.2.0
git push origin v0.2.0
```

## Contributing

Contributions welcome! To add or update keywords:

1. Add keywords to vendor-specific files in `prompt-keywords/`
2. Include a short `source:` comment for new keywords
3. Run the compile script: `python -m scripts.compile_keywords`
4. Open a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## License

MIT License - see [prompt-keywords/LICENSE](prompt-keywords/LICENSE) for details.

## Supported AI Models

- ChatGPT (OpenAI)
- Claude (Anthropic)
- GitHub Copilot
- Gemini (Google)
- Grok (X.AI)
- Perplexity AI

---

**Repository**: https://github.com/AaryaDangre/model-agnostic-keywords  
**Issues**: https://github.com/AaryaDangre/model-agnostic-keywords/issues
