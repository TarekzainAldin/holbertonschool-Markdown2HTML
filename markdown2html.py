#!/usr/bin/python3
"""
markdown2html.py
A script to convert a Markdown file to an HTML file without using external
libraries.
Usage:
    ./markdown2html.py input_file.md output_file.html
"""
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
