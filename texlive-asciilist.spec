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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The asciilist provides the environments AsciiList and AsciiDocList,
which enable quickly typesetting nested lists in LaTeX without having to
type individual item macros or opening/closing list environments. The
package provides auxiliary functionality for loading such lists from
files and provides macros for configuring the use of the list
environments and the appearance of the typeset results.

