# Data Directory

Add your datasets here. Large files are gitignored by default.

## Using uv for dependency management

We recommend using [uv](https://github.com/astral-sh/uv) for faster, more reliable Python package management:

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment
uv venv

# Activate it
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt
```
