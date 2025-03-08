#!/bin/bash
set -e

REPO_NAME="static_site_generator"

echo "Building site for GitHub Pages with basepath: /$REPO_NAME/"

python3 src/main.py "/$REPO_NAME/"

echo "Build complete! Site is in the 'docs' directory."
