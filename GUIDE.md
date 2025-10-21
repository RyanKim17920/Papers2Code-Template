# Implementation Guide

Quick tips for implementing your paper.

## First Steps

1. **Add dependencies** to `requirements.txt`
2. **Implement your model** in `src/model.py`
3. **Add your data** to the `data/` directory
4. **Document as you go** in this README

## Recommended Tools

- **[uv](https://github.com/astral-sh/uv)** - Faster package management
- **[wandb](https://wandb.ai)** - Experiment tracking (optional)
- **[pytorch](https://pytorch.org)** - Most common for paper implementations

## Project Organization

```
src/           # Your implementation code
tests/         # Tests (optional but recommended)
data/          # Your datasets (gitignored)
checkpoints/   # Model saves (gitignored)
results/       # Outputs (gitignored)
```

## Common Workflow

```bash
# 1. Setup
uv venv
source .venv/bin/activate
uv pip install torch numpy  # Add what you need

# 2. Implement
# Edit src/model.py with your architecture

# 3. Test it works
# Verify forward pass, architecture is correct

# 4. (Optional) Train
# Only if computationally feasible!
# python train.py

# 5. Document what you did in README
```

## Tips

- **Read the paper multiple times** - Don't rush implementation
- **Start simple** - Get basic version working first
- **Architecture is valuable** - Even without training!
- **Be honest about scope** - "Architecture only" is perfectly fine
- **Document what you did** - Clear is better than comprehensive
- **Ask for help** - Papers2Code community is here

## Best Practices (Optional)

See `BEST_PRACTICES.md` for optional guidelines on:
- Writing helpful documentation
- Sharing results transparently
- Common pitfalls to avoid

**Remember:** These are suggestions, not requirements. You're helping the community by implementing the paper - do what makes sense for you!

## Need More Structure?

Add as you need:
- `src/train.py` - Training script
- `src/data.py` - Data loading
- `src/utils.py` - Helper functions
- `configs/` - Configuration files
- `scripts/` - Utility scripts

---

Good luck with your implementation! 🚀
