#!/bin/bash

# Run this command first to grant permission
# chmod +x initial-compile.sh

lualatex iridian-grammar.tex
biber iridian-grammar
makeglossaries iridian-grammar
lualatex iridian-grammar.tex
