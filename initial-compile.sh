#!/bin/bash

# Run this command first to grant permission
# chmod +x initial-compile.sh

lualatex iridian-grammar.tex
biber iridian-grammar
makeglossaries iridian-grammar
lualatex iridian-grammar.tex
lualatex iridian-grammar.tex # Run a third time to allow expex to gather tags

