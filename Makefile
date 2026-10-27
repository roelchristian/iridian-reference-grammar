.DEFAULT_GOAL := all

MAIN := grammar
CHAPTERS := 01-overview 02-phonology 03-verbs 04-nouns 05-function-words \
            06-simple-sentence 07-information-structure 08-complex-sentences \
            09-discourse 10-derivational
LATEXMK ?= latexmk
PYTHON ?= python3
LMKFLAGS ?= -lualatex -interaction=nonstopmode -halt-on-error -file-line-error
FULL_DIR := build/full

.PHONY: all watch doctor clean distclean list help

# Always ask latexmk: its recorder tracks nested inputs and config changes,
# unlike a Makefile timestamp check against only chapters/*.tex.
all: | $(FULL_DIR)
	$(LATEXMK) $(LMKFLAGS) -outdir=$(FULL_DIR) $(MAIN).tex

watch: | $(FULL_DIR)
	$(LATEXMK) $(LMKFLAGS) -pvc -outdir=$(FULL_DIR) $(MAIN).tex

$(FULL_DIR):
	mkdir -p $@/chapters $@/util

# Independent output directories prevent includeonly builds from replacing the
# full PDF or teaching latexmk that a partial document is the complete book.
define CHAPTER_RULE
.PHONY: ch-$(1) ch-$(patsubst $(word 1,$(subst -, ,$(1)))-%,%,$(1)) ch-$(word 1,$(subst -, ,$(1)))
ch-$(1) ch-$(patsubst $(word 1,$(subst -, ,$(1)))-%,%,$(1)) ch-$(word 1,$(subst -, ,$(1))):
	mkdir -p build/chapters/$(1)/chapters build/chapters/$(1)/util
	$(LATEXMK) $(LMKFLAGS) -outdir=build/chapters/$(1) \
		-pretex='\includeonly{chapters/$(1)}' -usepretex $(MAIN).tex
.PHONY: watch-$(1) watch-$(patsubst $(word 1,$(subst -, ,$(1)))-%,%,$(1)) watch-$(word 1,$(subst -, ,$(1)))
watch-$(1) watch-$(patsubst $(word 1,$(subst -, ,$(1)))-%,%,$(1)) watch-$(word 1,$(subst -, ,$(1))):
	mkdir -p build/chapters/$(1)/chapters build/chapters/$(1)/util
	$(LATEXMK) $(LMKFLAGS) -pvc -outdir=build/chapters/$(1) \
		-pretex='\includeonly{chapters/$(1)}' -usepretex $(MAIN).tex
endef
$(foreach ch,$(CHAPTERS),$(eval $(call CHAPTER_RULE,$(ch))))

# Remove only this pipeline's products, never archived or hand-written files.
# Retain expensive font caches for the next build.
clean:
	rm -rf build/full build/chapters

distclean: clean
	rm -rf build/cache

doctor:
	$(PYTHON) scripts/check-build.py --latexmk '$(LATEXMK)'

list:
	@$(foreach ch,$(CHAPTERS),echo '$(ch)';)

help:
	@echo 'make                 Build build/full/grammar.pdf (incremental)'
	@echo 'make doctor          Check the local TeX installation'
	@echo 'make check           Build, validate PDF diagnostics, run utility tests'
	@echo 'make lexicon         Collect tagged forms as build/lexicon.json'
	@echo 'make lexicon-tsv     Collect tagged forms as build/lexicon.tsv'
	@echo 'make watch           Rebuild on changes; Ctrl-C stops watching'
	@echo 'make ch-nouns        Build a chapter in build/chapters/04-nouns/'
	@echo 'make watch-nouns     Watch a chapter (also accepts 04 or 04-nouns)'
	@echo 'make clean           Remove full and chapter build products'
	@echo 'make distclean       Also remove the shared LuaTeX font caches'
	@echo 'make list            List chapter names'

.PHONY: lexicon lexicon-tsv
lexicon:
	mkdir -p build
	$(PYTHON) util/collect_lexicon.py --format json --output build/lexicon.json

lexicon-tsv:
	mkdir -p build
	$(PYTHON) util/collect_lexicon.py --format tsv --output build/lexicon.tsv

.PHONY: check
check: all
	$(PYTHON) scripts/check-log.py $(FULL_DIR)/$(MAIN).log
	$(PYTHON) -m unittest discover -s util/tests -v
