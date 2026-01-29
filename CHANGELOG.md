# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2026-01-30

### Added
- Initial release with 7 vendor-specific keyword files (ChatGPT, Claude, Copilot, Gemini, Grok, Perplexity)
- Consolidated `keywords.md` (human-readable) and `keywords.yml` (machine-friendly) outputs
- `combined_keywords.json` and `combined_keywords.yml` with vendor metadata
- Metadata headers in vendor files (vendor, version, source, tags)
- Python compile script (`scripts/compile_keywords.py`) to generate combined outputs
- GitHub Actions CI workflow (Super-Linter validation, pytest)
- GitHub Actions release workflow for automated releases
- Contributing guidelines and PR/issue templates
- MIT license

### Vendors included
- ChatGPT (V0 and Reliability/Control versions)
- Claude (V4)
- Copilot (V1)
- Gemini (V3)
- Grok (V5)
- Perplexity (V2)

