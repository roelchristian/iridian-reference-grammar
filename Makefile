MAIN     := grammar
CHAPTERS := \
	01-overview \
	02-phonology \
	03-verbs \
	04-nouns \
	05-function-words \
	06-simple-sentence \
	07-complex-sentences \
	08-discourse \
	09-derivational \
	10-semantics \
	11-spoken-colloquial

LATEXMK  := latexmk
LMKFLAGS := -lualatex -interaction=nonstopmode -halt-on-error

# ── primary targets ──────────────────────────────────────────────────────────

.PHONY: all watch clean list help $(addprefix ch-, $(CHAPTERS))

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex $(wildcard chapters/*.tex)
	$(LATEXMK) $(LMKFLAGS) $(MAIN)

watch:
	$(LATEXMK) $(LMKFLAGS) -pvc $(MAIN)

# ── per-chapter partial builds ───────────────────────────────────────────────
# Usage: make ch-04-nouns   or   make ch-nouns   or   make ch-04

define CHAPTER_RULE
.PHONY: ch-$(1) ch-$(shell echo $(1) | sed 's/^[0-9]*-//') ch-$(shell echo $(1) | grep -o '^[0-9]*')
ch-$(1) ch-$(shell echo $(1) | sed 's/^[0-9]*-//') ch-$(shell echo $(1) | grep -o '^[0-9]*'):
	$(LATEXMK) $(LMKFLAGS) \
		-pretex='\includeonly{chapters/$(1)}' \
		-usepretex \
		$(MAIN)
endef

$(foreach ch,$(CHAPTERS),$(eval $(call CHAPTER_RULE,$(ch))))

# Per-chapter watch: make watch-04-nouns / watch-nouns / watch-04
define WATCH_RULE
.PHONY: watch-$(1) watch-$(shell echo $(1) | sed 's/^[0-9]*-//') watch-$(shell echo $(1) | grep -o '^[0-9]*')
watch-$(1) watch-$(shell echo $(1) | sed 's/^[0-9]*-//') watch-$(shell echo $(1) | grep -o '^[0-9]*'):
	$(LATEXMK) $(LMKFLAGS) -pvc \
		-pretex='\includeonly{chapters/$(1)}' \
		-usepretex \
		$(MAIN)
endef

$(foreach ch,$(CHAPTERS),$(eval $(call WATCH_RULE,$(ch))))

# ── clean ────────────────────────────────────────────────────────────────────

clean:
	$(LATEXMK) -C $(MAIN)
	@echo "Removing auxiliary files..."
	@find . -name ".git" -prune -o -type f \( \
		-name "*.aux" -o -name "*.log" -o -name "*.toc" -o -name "*.lof" -o \
		-name "*.lot" -o -name "*.out" -o -name "*.bbl" -o -name "*.blg" -o \
		-name "*.bcf" -o -name "*.run.xml" -o -name "*.idx" -o -name "*.ind" -o \
		-name "*.ilg" -o -name "*.fls" -o -name "*.fdb_latexmk" -o \
		-name "*.synctex" -o -name "*.synctex.gz" -o -name "*.nav" -o \
		-name "*.snm" -o -name "*.vrb" -o -name "*.glg" -o -name "*.gls" -o \
		-name "*.glo" -o -name "*.acn" -o -name "*.acr" -o -name "*.alg" -o \
		-name "*.xdy" -o -name "*.ptc" -o -name "*.mtc" -o -name "*.maf" -o \
		-name "*.thm" \
	\) -print0 | xargs -0 rm -vf

# ── informational ────────────────────────────────────────────────────────────

list:
	@echo "Available chapters:"
	@$(foreach ch,$(CHAPTERS),echo "  $(ch)";)

help:
	@echo "Targets:"
	@echo "  all                   Full build (default)"
	@echo "  watch                 Continuous rebuild of full document"
	@echo "  ch-<chapter>          Partial build — single chapter"
	@echo "  watch-<chapter>       Continuous rebuild — single chapter"
	@echo "  clean                 Remove all generated files"
	@echo "  list                  List available chapters"
	@echo ""
	@echo "Chapter can be the full name, slug (no number), or number alone:"
	@echo "  make ch-04-nouns   make ch-nouns   make ch-04"
