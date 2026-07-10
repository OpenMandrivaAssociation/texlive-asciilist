%global tl_name asciilist
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2b
Release:	%{tl_revision}.1
Summary:	Environments AsciiList and AsciiDocList for prototyping nested lists in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/asciilist
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asciilist.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asciilist.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asciilist.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The asciilist provides the environments AsciiList and AsciiDocList,
which enable quickly typesetting nested lists in LaTeX without having to
type individual item macros or opening/closing list environments. The
package provides auxiliary functionality for loading such lists from
files and provides macros for configuring the use of the list
environments and the appearance of the typeset results.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/asciilist
%dir %{_datadir}/texmf-dist/source/latex/asciilist
%dir %{_datadir}/texmf-dist/tex/latex/asciilist
%doc %{_datadir}/texmf-dist/doc/latex/asciilist/AsciiDocList.example
%doc %{_datadir}/texmf-dist/doc/latex/asciilist/AsciiList.example
%doc %{_datadir}/texmf-dist/doc/latex/asciilist/README.md
%doc %{_datadir}/texmf-dist/doc/latex/asciilist/asciilist.pdf
%doc %{_datadir}/texmf-dist/source/latex/asciilist/asciilist.dtx
%doc %{_datadir}/texmf-dist/source/latex/asciilist/asciilist.ins
%{_datadir}/texmf-dist/tex/latex/asciilist/asciilist.sty
