%global packname  Rmpi
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.6_1
Release:          1
Summary:          Interface (Wrapper) to MPI (Message-Passing Interface)
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-1.tar.gz
Requires:         R-rsprng 
Requires:         R-rlecuyer 
Requires:         openmpi
BuildRequires:    R-devel
BuildRequires:    Rmath-devel
BuildRequires:    texlive-collection-latex 
BuildRequires:    R-rsprng
BuildRequires:    R-rlecuyer 
BuildRequires:    openmpi-devel

%description
Rmpi provides an interface (wrapper) to MPI APIs. It also provides
interactive R slave environment.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL --no-test-load -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

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


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.5_9-3
+ Revision: 775463
- Add proper openmpi requires.

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.5_9-2
+ Revision: 774997
- Use proper tarball.

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.5_9-1
+ Revision: 774969
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.5_8-1
+ Revision: 774725
- Import R-Rmpi
- Import R-Rmpi

