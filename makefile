filename=iridian-grammar.tex

pdf: ps
	ps2pdf ${filename}.ps

pdf-print: ps
	ps2pdf -dColorConversionStrategy=/LeaveColorUnchanged -dPDFSETTINGS=/printer ${filename}.ps

text: html
	html2text -width 100 -style pretty ${filename}/${filename}.html | sed -n '/./,$$p' | head -n-2 >${filename}.txt

html:
	@#latex2html -split +0 -info "" -no_navigation ${filename}
	htlatex ${filename}

all:
	lualatex ${filename}
	biber ${filename}
	makeglossaries ${filename}
	lualatex ${filename}
	lualatex ${filename}
	lualatex ${filename}

quick:
	lualatex ${filename}

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
	evince ${filename}.pdf &

aread:
	acroread ${filename}.pdf

clean:
	find . -type f -name '*.aux' -exec rm {} +
	find . -type f -name '*.out' -exec rm {} +
	find . -type f -name '*.idx' -exec rm {} +
	find . -type f -name '*.ilg' -exec rm {} +
	find . -type f -name '*.ind' -exec rm {} +
	find . -type f -name '*.log' -exec rm {} +
	find . -type f -name '*.lot' -exec rm {} +
	find . -type f -name '*.lof' -exec rm {} +
	find . -type f -name '*.maf' -exec rm {} +
	find . -type f -name '*.mtc' -exec rm {} +
	find . -type f -name '*.mtc0' -exec rm {} +
	find . -type f -name '*.xml' -exec rm {} +
	find . -type f -name '*.toc' -exec rm {} +
	find . -type f -name '*.ent' -exec rm {} +
	find . -type f -name '*.lg' -exec rm {} +
	find . -type f -name '*.dvi' -exec rm {} +

	echo "Done cleaning up the working directory."
