%global packname  Rmpi
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.5_8
Release:          1
Summary:          Interface (Wrapper) to MPI (Message-Passing Interface)
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              None
Source0:          http://cran.r-project.org/src/contrib/Archive/Rmpi/Rmpi_0.5-8.tar.gz
Requires:         R-rsprng R-rlecuyer 
BuildRequires:    R-devel texlive-collection-latex 
BuildRequires:    R-rsprng R-rlecuyer 
BuildRequires:    openmpi
BuildRequires:    openmpi-devel

%description
Rmpi provides an interface (wrapper) to MPI APIs. It also provides
interactive R slave environment.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R*
%{rlibdir}/%{packname}/c*
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/s*
