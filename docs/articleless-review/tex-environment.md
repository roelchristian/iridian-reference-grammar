# Isolated TeX dependencies for Iridian full-PDF validation

Date: 2026-11-08. No repository sources or system configuration changed.

Activate before running repository targets:

```sh
source /tmp/iridian-tex/env.sh
make doctor
make check
```

The existing TeX Live installation supplies LuaLaTeX and latexmk. Missing genuine dependencies were extracted under `/tmp/iridian-tex/root` from Debian trixie packages, using `dpkg-deb -x`, without installing them system-wide:

- Biber 2.20-2 (`biber_2.20-2_all.deb`)
- TeX Live BibTeX Extra 2024.20250309-2 (BibLaTeX 3.20)
- TeX Live Humanities 2024.20250309-2 (ExPex)
- TeX Live LuaTeX 2024.20250309-2 (luaotfload, missing from the base installation)
- TeX Live Plain Generic 2024.20250309-2 (tracklang, missing from the base installation)
- Biber's dependency closure as recorded in `downloads/biber-dependencies.json` (119 packages, about 15 MB compressed).

Packages came from `https://deb.debian.org/debian/`; package-index metadata came from trixie/main amd64 `Packages.xz`.

Required fonts:

- Genuine LibertinusSerif OTFs from upstream Libertinus 7.051, https://github.com/alerque/libertinus/releases/download/v7.051/Libertinus-7.051.zip
- Genuine Source Sans Pro OTFs from Adobe upstream tag `2.045R-ro/1.095R-it`, https://github.com/adobe-fonts/source-sans/tree/2.045R-ro/1.095R-it/OTF
- Upstream names the Source Sans Pro Regular Italic file `SourceSansPro-It.otf`; a local filename alias `SourceSansPro-RegularIt.otf -> SourceSansPro-It.otf` satisfies the repository's TeX-distribution filename contract. The underlying font is the genuine required face, not an alternate font.

`make doctor` passes all 25 package checks and all eight exact font-file checks. `biber --version` reports 2.20. Full build and diagnostic acceptance are separate and recorded in `/tmp/articleless-full-build.log`.

The download scripts `download.py`, `deps.py`, and package manifest preserve download sources. `env.sh` prepends only local executables, local TeX-tree and Perl/shared-library search paths. System binaries and existing TeX installation remain unchanged.

The first complete compile exposed missing `luaotfload-main.lua` and `tracklang.sty`, which `make doctor` does not currently diagnose; these were supplied by the additional genuine TeX Live packages above. Forced rerun flag `-g` was used once after failed preamble initialization so latexmk would not reuse the cached failed invocation.
