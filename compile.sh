#!/bin/bash

# Run this command first to grant permission
# chmod +x compile.sh

# Do not run this file if auxiliary files have just been cleaned up.
# Instead run initial-compile.sh first.

xelatex iridian-grammar.tex
