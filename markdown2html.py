#!/usr/bin/env python3
import sys
import os

# Check if the correct number of arguments is provided
if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    sys.exit(1)

# Get the input and output file names from the arguments
markdown_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the Markdown file exists
if not os.path.exists(markdown_file):
    sys.stderr.write(f"Missing {markdown_file}\n")
    sys.exit(1)

# If everything is okay, exit with no output
sys.exit(0)
