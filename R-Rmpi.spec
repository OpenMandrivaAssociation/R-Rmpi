%global packname Rmpi
%global rlibdir  %{_libdir}/R/library

Name:		R-%{packname}
Version:	0.6.3
Release:	3
Summary:	Interface (Wrapper) to MPI (Message-Passing Interface)
Group:		Sciences/Mathematics
License:	GPLv2+
Url:		http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:	http://cran.r-project.org/src/contrib/Rmpi_0.6-3.tar.gz
BuildRequires:	openmpi
BuildRequires:	R-rlecuyer
BuildRequires:	R-rsprng
BuildRequires:	texlive-collection-latex
BuildRequires:	pkgconfig(libR)
BuildRequires:	pkgconfig(libRmath)
BuildRequires:	pkgconfig(ompi)
Requires:	openmpi
Requires:	R-rlecuyer
Requires:	R-rsprng

%description
Rmpi provides an interface (wrapper) to MPI APIs. It also provides
interactive R slave environment.

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/MacR64slaves.sh
%{rlibdir}/%{packname}/R*
%{rlibdir}/%{packname}/c*
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/s*

#----------------------------------------------------------------------------

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL --no-test-load -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

