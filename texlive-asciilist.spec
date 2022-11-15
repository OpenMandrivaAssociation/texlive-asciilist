Name:		texlive-asciilist
Version:	49060
Release:	1
Summary:	Environments AsciiList and AsciiDocList for prototyping nested lists in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/asciilist
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asciilist.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asciilist.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asciilist.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The asciilist provides the environments AsciiList and
AsciiDocList, which enable quickly typesetting nested lists in
LaTeX without having to type individual item macros or
opening/closing list environments. The package provides
auxiliary functionality for loading such lists from files and
provides macros for configuring the use of the list
environments and the appearance of the typeset results.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/asciilist
%{_texmfdistdir}/tex/latex/asciilist
%doc %{_texmfdistdir}/doc/latex/asciilist

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
