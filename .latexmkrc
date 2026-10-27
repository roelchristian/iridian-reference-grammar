# Keep LuaTeX's font caches writable in sandboxes and CI.  These are shared by
# full and chapter builds, but never mixed with their LaTeX auxiliary files.
use File::Path qw(make_path);
# Relative paths also satisfy TeX's restrictive openout_any policy.
my $cache_root = 'build/cache';
$ENV{'TEXMFVAR'} = "$cache_root/texmf-var";
$ENV{'TEXMFCACHE'} = "$cache_root/texmf-cache";
make_path($ENV{'TEXMFVAR'}, $ENV{'TEXMFCACHE'});

$pdf_mode = 4; # LuaLaTeX
$lualatex = 'lualatex %O %S';
$max_repeat = 6;
