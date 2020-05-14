#!/bin/bash

# Run this command first to grant permission
# chmod +x initial-compile.sh

xelatex iridian-grammar.tex
biber iridian-grammar
xelatex iridian-grammar.tex
