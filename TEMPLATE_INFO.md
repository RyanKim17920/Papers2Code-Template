# Template Information

This template auto-populates with paper information when you create a repository from Papers2Code.

## What Gets Auto-Filled

The following placeholders are replaced automatically:

- `{{PAPER_TITLE}}` - Paper title
- `{{AUTHORS_LIST}}` - Formatted author list  
- `{{PAPER_ABSTRACT}}` - Full abstract
- `{{ARXIV_URL}}` - Link to arXiv
- `{{PDF_URL}}` - Link to PDF
- `{{PAPERS2CODE_URL}}` - Link to Papers2Code page
- `{{CITATION_BIBTEX}}` - BibTeX citation
- `{{GITHUB_USERNAME}}` - Your GitHub username
- `{{REPO_NAME}}` - Generated repository name

## Files Affected

- `README.md` - Main documentation
- `setup.py` - Package configuration
- `src/__init__.py` - Package info
- `src/model.py` - Model file header

## Simple Replacement Logic

```python
# Backend implementation example
replacements = {
    '{{PAPER_TITLE}}': paper.title,
    '{{AUTHORS_LIST}}': '\n'.join(f'- {a}' for a in paper.authors),
    '{{PAPER_ABSTRACT}}': paper.abstract,
    '{{ARXIV_URL}}': paper.arxiv_url,
    '{{PDF_URL}}': paper.pdf_url,
    '{{PAPERS2CODE_URL}}': f'https://papers2code.com/papers/{paper.id}',
    '{{CITATION_BIBTEX}}': paper.bibtex,
    '{{GITHUB_USERNAME}}': user.github_username,
    '{{REPO_NAME}}': paper.title.lower().replace(' ', '-')[:100],
}

for file in ['README.md', 'setup.py', 'src/__init__.py', 'src/model.py']:
    content = read_file(file)
    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)
    write_file(file, content)
```

That's it! Keep it simple.
