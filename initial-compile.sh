#!/bin/bash

# Run this command first to grant permission
# chmod +x initial-compile.sh

pdflatex iridian-grammar.tex
biber iridian-grammar
pdflatex iridian-grammar.tex
