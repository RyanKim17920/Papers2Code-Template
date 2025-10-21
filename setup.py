from setuptools import setup, find_packages

setup(
    name="{{REPO_NAME}}",
    version="0.1.0",
    author="{{GITHUB_USERNAME}}",
    description="Implementation of {{PAPER_TITLE}}",
    url="https://github.com/{{GITHUB_USERNAME}}/{{REPO_NAME}}",
    packages=find_packages(),
    python_requires=">=3.8",
)
