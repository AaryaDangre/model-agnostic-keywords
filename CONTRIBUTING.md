# Contributing

Thanks for contributing. Please follow these guidelines when adding or updating keywords.

Guidelines
- Add vendor-specific files to `prompt-keywords/` using the filename pattern:
  `Model Agnostic Prompting Keywords_<VENDOR>_<VERSION>.txt`
- Keep one keyword or instruction per line.
- When adding keywords, include a short `source:` comment on the line above or beside the keyword.
- Run the compile script to regenerate combined outputs before opening a PR:

```bash
python -m scripts.compile_keywords
```

- The repository uses GitHub Actions (Super-Linter) to validate Markdown and YAML. Fix any lint issues reported by CI.

Thank you — maintain clarity and small PRs help review.
