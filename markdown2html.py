#!/usr/bin/python3
"""Write a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name
Requirements:

If the number of arguments is less than 2: print in STDERR Usage:
./markdown2html.py README.md README.html and exit 1
If the Markdown file doesn't exist: print in STDER Missing <filename> and
exit 1
Otherwise, print nothing and exit 0"""

import sys
import os
import re
import hashlib

if __name__ == "__main__":

    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    markdown_file = sys.argv[1]
    output_name = sys.argv[2]

    if not os.path.isfile(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        exit(1)