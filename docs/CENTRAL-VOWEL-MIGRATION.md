> Historical vowel-migration record. References below to anchored counterparts describe its baseline, not the present articleless nominal inventory. The vowel reform remains in force; the original record is retained verbatim.

# Central-vowel migration

This record implements the approved y/ė brief against baseline
`e84091424a701bedd56fe7e11c184f1e575a0026`. The active grammar assigns y the
single short category /ɨ/, with [ɯ̯ɨ] and [ɨi̯] under primary or secondary
lexical stress, and assigns ė the short central category /ə/. Former modern
ý spellings merge into y; their former quantity does not survive in narrow
pronunciation. The principal variety therefore has seven short vowel categories
and three long categories, with the existing /ou̯/ retained.

The [machine-readable record](central-vowel-migrations.json) gives each audited
slot's old and new full segments, reduced base, selected bound grade,
construction, consonantal information, descriptive status and baseline source
locations. These locations document the migration's inputs; revised line numbers
and pagination will differ. Historical reconstructions are identified separately
and retain their original notation. No dictionary entry is generated from an
illustration or an unspecified lexical class.

## Audited fleeting slots

Only the designated second nucleus changes quality in these mappings. Reduced
stems, case endings, independently selected quantity and consonantal grades
retain their established specifications.

| Old full form | Revised full form | Reduced material preserved | Status and selecting construction |
| --- | --- | --- | --- |
| Janek | Janėk | Jank- / Janc-; Janku, Jancí | Existing proper-name examples; full direct versus reduced case stem |
| perek | perėk | pérk- / pérc-; pérku | Lexical Class II unraised; G1 targets the first root nucleus after reduction |
| lobek | lobėk | lúbk- / lúbc-; lúbku | Lexical Class II raised; selected G3 is independent of deletion |
| obel | obėl | obl- / obľ-; oblu, oblě, obľa | Lexical Class VII; its endings select hard or soft bound stems |
| sviňek | sviňėk | svíňk- / svíňc- | Lexical Class II unraised; explicit ň preserves the soft nasal before schwa |
| tězeň | tězėň | tězn- / tězň- | Lexical Class VII; nasal grade remains constructionally selected |
| kolen | kolėn | koln-; kolnat- | Lexical noun; reduced G0 before -at-; declension and general quantity class remain unassigned |
| razeň- | razėň- | razn-; raznit | Lexical verbal Class A; purposive selection includes independently hard n |
| stólek | stólėk | stólk- | Existing productive diminutive illustration; root G1 precedes the alternating nominal suffix |
| Merek | Merėk | Merk- / Merc-; Mercí | Existing unglossed case illustration; broader class and lexical identity remain unspecified |
| berel | berėl | berl-; berla | Explicitly constructed plain-grade suffixation; no dictionary entry |
| pěštel | pěštėl | raised pištl-; pištlí | Existing unglossed raising illustration; lexical /pʲ/ survives independently |
| Marek | Marėk | Mark- / Marc-; Marku/Marka, Marcí/Markovi, Marko | Established name with its listed singular doublets; distinct from Merėk |
| uzel | uzėl | uzl-; uzla | Existing unglossed syllabification illustration; broader class remains unspecified |

The nominal alternating suffix -ek becomes -ėk only in its designated
formations. The verbal perfective -ek ~ -ik-, lexical ordinary e /ɛ/, long é,
stable endings and unresolved soft-velar spellings retain their established
values. No character-level substitution of ě is used: a genuinely soft
consonant remains explicitly represented before ė. The spelling has no general
instruction to delete a nucleus; stable-schwa probes are controls rather than
new lexical entries.

## Quantity, syllables and homophony

The plain and strong grades of a selected root y coincide at /ɨ/. G1 remains a
morphological selection, and an unchanged output does not permit a search for
an earlier lengthenable vowel. Accordingly, byl- has the same segmental shape
in singular G0 and plural G1, while case-number endings still distinguish the
listed cells: byle, bylov, bylac and their anchored counterparts. Progressive
bydlime likewise retains its Class A strong selection. The adverb býh becomes
byh, and the relative suffix -ový becomes -ovy throughout its combinations.

These changes collapse grade exponents rather than lexical identities. The
curated appendix contains no separately established pair of headwords whose
identity must be merged solely because of the removal of ý. Former schematic
phonology contrasts do not establish additional dictionary entries; their
obsolete quantity claims are removed from the contemporary treatment. Existing
names, particles, stems and constructed illustrations retain their meanings,
licensing and evidential status.

Every retained ė counts as a nucleus under the ordinary stress rules. Fleeting
slots remain excluded from grade eligibility by their morphological class,
while stable schwa is not automatically excluded merely by its quality. Primary
and nonfinal alternating secondary foot heads license moving y; a final
unpaired third syllable does not. A glide within the phonetic trajectory is
neither an additional nucleus nor a morphological palatalisation instruction,
and an independently represented lexical /j/ remains intact.

## Separately adopted repair profile

The approved profile also assigns newly inserted productive repair vowels the
value ė /ə/. This phonotactic operation supplies a nucleus after stem selection,
grade realisation and morphological assembly, before final stress assignment.
It does not reclassify existing e on the basis of a presumed historical origin.
Required retention still precedes later class-licensed consonantal repair, and
epenthesis cannot retrospectively license an otherwise unavailable reduced
stem. Soft-coronal spellings ťė, ďė, ňė and ľė, and independently soft-labial
spellings pjė, bjė, mjė and vjė, preserve the consonantal information without
making schwa an automatic PAL trigger.

## Source and validation boundaries

The maintained sources are grammar.tex, chapters/ and the included appendices
and reusable tables. The curated lexicon is edited directly; the collector
continues to extract tagged occurrences into JSON or TSV without overwriting
the appendix. Its existing NFC normalisation preserves distinct e, ė and ě
identities, including canonical uppercase Ė and decomposed dotted-e imports.

Historical reconstructions, bibliography, archive/2020/, working stubs and
dated source/review records retain earlier spellings as provenance. The active
stative paradigm report receives only the authorised spelling changes; the
scope guard retains baseline hashes and independently verifies those precise
transformations. Migration records and negative tests may explicitly mention
ý, Ý and /ɨː/ as old input; such mentions do not reintroduce a contemporary
category. The [residual source audit](central-vowel-residual-audit.json) classifies each
remaining occurrence by path and line against these roles; no contemporary
error is left unclassified.

Publication acceptance uses sequential `make check-source`, `make check`,
`make lexicon`, `make lexicon-tsv` and `git diff --check`, followed by visual
inspection of affected PDF pages. The utility tests cover quantity identity
without retargeting, stress-conditioned pronunciation, stable versus fleeting
schwa, preserved reduced forms and consonantal grades, perfective suffix
identity and Unicode round trips. Build and test results belong to the final
implementation report, rather than being assumed by this migration record.

## Completed validation

The integrated implementation passed `make check-source` and `make check`,
including all 233 utility tests and the full grammar and standalone-cover log
checks. Both logs report no missing glyphs, undefined references, fatal errors
or overfull boxes. The rebuilt grammar contains 455 PDF pages.

Visual review covered PDF pages 22–24, 36, 41–42, 48–49, 54, 56–57, 67,
71–72, 429, 431, 433 and 438, including the revised inventory, moving-vowel
diacritics, uppercase dotted e, stress probes, quantity grades, consonantal
spellings, paradigms, lexical entries and historical qualifications. No clipping,
overlapping text or broken glyphs was found.

`make lexicon` and `make lexicon-tsv` produced 1,445 distinct tagged forms.
The migrated forms retain source-occurrence provenance; the unlexicalised
pronunciation probes are excluded from extraction. `git diff --check` passed,
and the original symbolic labels were preserved. The residual audit classifies
all retained old-symbol occurrences as historical evidence, bibliographic
material or migration-test input. No commit or push was made.

The revised phonological discussion retains existing bibliography entries.
The relevant passages were checked in Bell et al.'s
[Northern Welsh description](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/196DCA35257D55166D33EA66FF372DC1/S0025100321000165a.pdf/northern_welsh.pdf),
pp. 499–500, for the high-central-vowel and schwa comparison;
[Gouskova (2012)](https://www.gouskova.com/wp-content/uploads/2016/03/gouskova_2012_nllt.pdf),
§4.1, for morpheme-level lexical exceptionality; and
[Hall (2006)](https://phonco.ucsd.edu/files/2015/04/Hall-2006.pdf), pp. 387–388,
for the distinction between epenthetic nuclei and vowel intrusion. These
comparisons support the stated analytical points; the particular Iridian
vowel values, stem assignments and stress-conditioned trajectories remain
language specifications.
