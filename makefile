filename=iridian-grammar
AUX_EXTS = aux out idx ilg ind log lot lof maf mtc mtc0 xml toc ent lg dvi idv 4ct 4tc acn acr alg bbl bcf blg lpz lzo lzs ist

all:
	lualatex ${filename}
	biber ${filename}
	makeglossaries ${filename}
	lualatex ${filename}
	lualatex ${filename}

quick:
	lualatex ${filename}

once: quick-build clean

bib:
	biber ${filename}

glossaries:
	makeglossaries ${filename}

update-bib:
	lualatex ${filename}
	biber ${filename}
	lualatex ${filename}

update-glo:
	lualatex ${filename}
	biber ${filename}
	makeglossaries ${filename}
	lualatex ${filename}

read:
	if [ ! -f $(filename) ]; then \
		echo "Error: $(filename) does not exist"; \
		exit 1; \
	fi
	
	if [ "$(shell uname)" = "Darwin" ]; then \
		open $(filename); \
	elif [ "$(shell uname)" = "Linux" ]; then \
		xdg-open $(filename); \
	fi

clean:
	for ext in $(AUX_EXTS); do \
		find . -name "*.$$ext" -exec rm {} \; ; \
	done