# Papers2Code Template

A clean, minimal template for implementing academic papers.

## 📁 Structure

```
Papers2Code-Template/
├── README.md              # Auto-populated with paper info
├── requirements.txt       # Add your dependencies here
├── setup.py              # Basic package setup
├── .gitignore            # Ignores data, models, logs
├── .env.example          # Environment variables template
├── LICENSE               # MIT License
├── 📘 ABOUT.md            # Template overview (maintainers)
├── 📗 GUIDE.md            # Quick implementation guide (users)
├── 📙 TEMPLATE_INFO.md    # Placeholder documentation (maintainers)
├── 📕 BEST_PRACTICES.md   # Optional guidelines (users)
├── src/
│   ├── __init__.py       # Package info
│   └── model.py          # Your model implementation goes here
├── tests/
│   └── __init__.py       # Your tests go here
└── data/
    ├── .gitkeep
    └── README.md         # Data directory info + uv setup guide
```

## ✨ Features

- **Auto-populates** with paper title, authors, abstract, and citations
- **Minimal boilerplate** - just the essentials
- **Clean gitignore** - excludes data, models, and logs
- **uv-ready** - Recommended for faster dependency management
- **Simple structure** - Easy to understand and modify

## 🚀 What Users Get

When a repository is created from this template:

1. **README.md** populated with:
   - Paper title and authors
   - Abstract
   - Links (arXiv, PDF, Papers2Code)
   - BibTeX citation
   - Getting started instructions

2. **Clean starting point**:
   - Empty `src/model.py` ready for implementation
   - Empty `requirements.txt` for dependencies
   - Organized directories for code, tests, and data

3. **Ready to code**:
   ```bash
   uv venv && source .venv/bin/activate
   uv pip install -r requirements.txt
   # Start implementing!
   ```

## 📝 Placeholders

The following are automatically replaced:
- `{{PAPER_TITLE}}`
- `{{AUTHORS_LIST}}`
- `{{PAPER_ABSTRACT}}`
- `{{ARXIV_URL}}`
- `{{PDF_URL}}`
- `{{PAPERS2CODE_URL}}`
- `{{CITATION_BIBTEX}}`
- `{{GITHUB_USERNAME}}`
- `{{REPO_NAME}}`

See `TEMPLATE_INFO.md` for implementation details.

## 🎯 Philosophy

**Keep it simple.** This template provides just enough structure to get started without overwhelming users with boilerplate code they'll need to delete or modify. Users can add complexity as needed for their specific paper implementation.

**Encourage, don't enforce.** `BEST_PRACTICES.md` provides optional guidelines inspired by NeurIPS code release recommendations, but users are free to implement however they want.

## 📦 Dependencies

None by default! Users add what they need to `requirements.txt`.

Common starting point:
```txt
torch>=2.0.0
numpy>=1.24.0
```

## 🔧 Maintenance

To update this template:
1. Keep it minimal - resist adding too much
2. Test placeholder replacement
3. Ensure .gitignore covers common cases
4. Update TEMPLATE_INFO.md if adding new placeholders

---

**Less is more.** A simple, clean starting point is better than an overwhelming scaffold.
