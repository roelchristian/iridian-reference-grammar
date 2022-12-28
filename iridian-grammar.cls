\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{iridian-grammar}[2022/12/19 v1.0.0 Custom class for Iridian Grammar]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{scrbook}}
\ProcessOptions\relax

% Load the scrbook class as the base class
\LoadClass[11pt]{scrbook}
\areaset[0.50in]{4.5in}{8in}

% Page layout
\RequirePackage[paperwidth=6in,paperheight=9in]{geometry}
\geometry {
    verbose,
    tmargin  =1.1in,
    bmargin  =1.1in,
    lmargin  =0.7in,
    rmargin  =0.7in,
}

% General font and typography
\RequirePackage{microtype}
\RequirePackage{float}
\doublehyphendemerits=1000000000
\widowpenalty=10000
\clubpenalty=10000
\brokenpenalty=10000
\RequirePackage{fontspec}
\defaultfontfeatures{Ligatures=TeX}
\setmainfont{Linux Libertine O}
\setsansfont{Linux Biolinum O}
\newfontfamily\cyrtext[Scale=1]{Linux Libertine O}

% Examples and glosses
\RequirePackage{expex}
\gathertags

% Third level examples in expex
% http://tex.stackexchange.com/a/77941
\def\beginsubsub{%
\par
\begingroup
\advance\leftskip by 2em
\def\b##1{\par\leavevmode\llap{\hbox to 2em{##1\hfil}}\ignorespaces}}
\def\endsubsub{\par\endgroup}

% Language support
\RequirePackage[russian,english]{babel}
\RequirePackage[german=guillemets]{csquotes}

% Tables and figures
\RequirePackage{graphics}
\RequirePackage{graphicx}
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage[justification=raggedright,labelfont=sc,font={sf,footnotesize},labelsep=quad]{caption}
\captionsetup{justification=raggedright,singlelinecheck=false}
\RequirePackage{longtable}
\RequirePackage{minitoc}
\RequirePackage{afterpage}
\RequirePackage{fancyhdr}
\RequirePackage{textcase}
\RequirePackage{tabularray}
\UseTblrLibrary{booktabs}
\SetTblrInner{rowsep=6pt}
\RequirePackage{gensymb}
\RequirePackage{titlesec}
\RequirePackage{etoolbox}
\RequirePackage{multirow}
\RequirePackage[shortlabels]{enumitem}
\RequirePackage{metalogo}

\setlist[enumerate]{leftmargin=*}
\setlist[itemize]{leftmargin=*}

%% to draw linguistic trees
\RequirePackage{tikz}
\RequirePackage[linguistics]{forest}
\usetikzlibrary{positioning}
\usetikzlibrary{tikzmark}
\forestset{
sn edges/.style={for tree={parent anchor=south, child anchor=north}}}

%% Indexing and Cross-referencing
\RequirePackage{imakeidx}
\RequirePackage[font=footnotesize]{idxlayout}
\RequirePackage{hyperref}
\makeatletter\let\Title\@title\makeatother
\hypersetup{
  hidelinks,
  unicode,
  pdftitle={\Title}
}

\RequirePackage{url}
\urlstyle{same}

% Redefine \emptyset to \varnothing
\let\oldemptyset\emptyset
\let\emptyset\varnothing

% fancy footnotes
\RequirePackage[norule,splitrule]{footmisc}

\RequirePackage[authordate,backend=biber]{biblatex-chicago}
\DeclareFieldFormat[article]{title}{\mkbibquote{#1}} % make article titles in quotes
\DeclareFieldFormat[thesis]{title}{\mkbibemph{#1}} % make theses italics
\addbibresource{./bib/bibliography.bib}
\setlength\bibitemsep{0.4\itemsep}
\renewcommand*{\bibfont}{\small}

\renewcommand*{\postnotedelim}{\addcolon\addspace}
\DeclareFieldFormat{postnote}{#1}
\DeclareFieldFormat{multipostnote}{#1}

\makeindex
\setcounter{secnumdepth}{2}
\setcounter{tocdepth}{2}

%% Set block quotes to font size \small

\expandafter\def\expandafter\quote\expandafter{\quote\small}

%% Formatting of linguistic glosses

\lingset{everygla=\it,everyglb=\footnotesize,everyglft=\footnotesize,aboveexskip=5pt,aboveglftskip=0pt,belowexskip=5pt}


% Possessive citations like "Doe's (1992)"
% From C Becker
% https://tex.stackexchange.com/a/307461
\DeclareNameFormat{labelname:poss}{% Based on labelname from biblatex.def
  \nameparts{#1}% Not needed if using Biblatex 3.4
  \ifcase\value{uniquename}%
    \usebibmacro{name:family}{\namepartfamily}{\namepartgiven}{\namepartprefix}{\namepartsuffix}%
  \or
    \ifuseprefix
      {\usebibmacro{name:first-last}{\namepartfamily}{\namepartgiveni}{\namepartprefix}{\namepartsuffixi}}
      {\usebibmacro{name:first-last}{\namepartfamily}{\namepartgiveni}{\namepartprefixi}{\namepartsuffixi}}%
  \or
    \usebibmacro{name:first-last}{\namepartfamily}{\namepartgiven}{\namepartprefix}{\namepartsuffix}%
  \fi
  \usebibmacro{name:andothers}%
  \ifnumequal{\value{listcount}}{\value{liststop}}{'s}{}}
\DeclareFieldFormat{shorthand:poss}{%
  \ifnameundef{labelname}{#1's}{#1}}
\DeclareFieldFormat{citetitle:poss}{\mkbibemph{#1}'s}
\DeclareFieldFormat{label:poss}{#1's}
\newrobustcmd*{\posscitealias}{%
  \AtNextCite{%
    \DeclareNameAlias{labelname}{labelname:poss}%
    \DeclareFieldAlias{shorthand}{shorthand:poss}%
    \DeclareFieldAlias{citetitle}{citetitle:poss}%
    \DeclareFieldAlias{label}{label:poss}}}
\newrobustcmd*{\posscite}{%
  \posscitealias%
  \textcite}
\newrobustcmd*{\Posscite}{\bibsentence\posscite}
\newrobustcmd*{\posscites}{%
  \posscitealias%
  \textcites}

%%Formatting of section headings

\makeatletter
\def\thickhrulefill{\leavevmode \leaders \hrule height 1ex \hfill \kern \z@}
\def\@makechapterhead#1{%
	\vspace*{10\p@}%
	{\parindent \z@ \centering \reset@font
		{\Large \sffamily\scshape  \thechapter}
		\par
		\vspace*{1\p@}%
		\interlinepenalty\@M
		\setlength{\arrayrulewidth}{2pt}
		\par\noindent
		\rule{24pt}{2pt}
		\\
		\begin{tabular}{@{\qquad}c@{\qquad}}

			\\
			{\LARGE \sffamily\scshape  \MakeLowercase{#1}\par\nobreak} \\
			\\

		\end{tabular}
		\vskip 90\p@
}}
\def\@makeschapterhead#1{%
	\vspace*{\p@}%
	{\parindent \z@ \centering \reset@font
		{\Large \sffamily \scshape  \vphantom{\thechapter}}
		\par\nobreak
		\vspace*{15\p@}%
		\interlinepenalty\@M
		\setlength{\arrayrulewidth}{2pt}
		\par\noindent
		\rule{24pt}{2pt}
		\\
		\begin{tabular}{@{\qquad}c@{\qquad}}

			\\
			{\LARGE \sffamily \scshape \MakeLowercase{#1}\par\nobreak} \\
			\\

		\end{tabular}
		\vskip 80\p@
}}


%% Formatting of sections
\titleformat{\section}
{}{\thesection}{1em}{\large}
\titlespacing*{\section}
{0pt}{3ex plus 1ex minus .2ex}{4pt}

%% Formatting of subsections
\titleformat{\subsection}[hang]
{\small\sffamily}{\thesubsection}{1em}{\small\sffamily}
\titlespacing*{\subsection}
{0pt}{3ex plus 1ex minus .2ex}{4pt}



%% Formatting of subsubsections
\titleformat{\subsubsection}
{\small}{\thesubsubsection}{1em}{\small}

\titleformat{\paragraph}[runin]{\bfseries\normalsize}{\theparagraph}{2em}{}

\RequirePackage{titletoc}

%% Formatting of page headers

\renewcommand{\chapterpagestyle}{empty}%The first page in each chapter won't have any heading or footer, especially no page number
\pagestyle{fancy}
\renewcommand{\chaptermark}[1]{\markboth{#1}{}}
\renewcommand{\sectionmark}[1]{\markright{#1}}
\renewcommand{\headrulewidth}{0pt}
\fancyhf{}
\fancyhead[RE]{{{\scshape\small\MakeLowercase{\leftmark}}}\hfill{\small\thepage}}
\fancyhead[LO]{{\small\thepage}\hfill{\scshape\small\MakeLowercase{\rightmark}}}
\cfoot{}


% Glosses in footnotes
\newcounter{fnexno}
\setcounter{fnexno}{1}
\definelingstyle{fnex}{
% exno=\footnotesize\roman{fnexno}\stepcounter{fnexno},
  exno=\roman{fnexno}\stepcounter{fnexno},
  everyex=\footnotesize,
  numoffset=\footnotemargin,
  aboveexskip=2ex,
  belowglpreambleskip=-1ex,
  interpartskip=0.5ex,
  aboveglftskip=-1ex,
  belowexskip=0ex,
}

% Restart numbering each chapter
\pretocmd{\chapter}{\excnt=1}{}{}

\endinput




