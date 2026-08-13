%global tl_name hyphen-czech
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Czech hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-czech
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-czech.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Czech in T1/EC and UTF-8 encodings. Original
patterns 'czhyphen' are still distributed in the 'csplain' package and
loaded with ISO Latin 2 encoding (IL2).


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-czech:
czech loadhyph-cs.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-czech:
\addlanguage{czech}{loadhyph-cs.tex}{}{2}{3}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-czech:
['czech'] = {
	loader = 'loadhyph-cs.tex',
	lefthyphenmin = 2,
	righthyphenmin = 3,
	synonyms = {  },
	patterns = 'hyph-cs.pat.txt',
	hyphenation = 'hyph-cs.hyp.txt',
},
TL_HYPHEN_EOF
