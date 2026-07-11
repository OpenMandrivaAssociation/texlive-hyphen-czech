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
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Czech in T1/EC and UTF-8 encodings. Original
patterns 'czhyphen' are still distributed in the 'csplain' package and
loaded with ISO Latin 2 encoding (IL2).

