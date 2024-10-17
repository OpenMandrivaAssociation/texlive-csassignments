Name:		texlive-csassignments
Version:	63992
Release:	2
Summary:	A wrapper for article with macros and customizations for computer science assignments
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/csassignments
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csassignments.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csassignments.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csassignments.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class wraps the default article and extends it for a
homogeneous look of hand-in assignments at university (RWTH
Aachen University, Computer Science Department), specifically
in the field of computer science, but easily extensible to
other fields. It provides macros for structuring exercises,
aggregating points, and displaying a grading table, as well as
several macros for easier math mode usage.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/csassignments
%{_texmfdistdir}/tex/latex/csassignments
%doc %{_texmfdistdir}/doc/latex/csassignments

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
