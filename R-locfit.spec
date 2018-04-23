#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-locfit
Version  : 1.5.9.1
Release  : 6
URL      : https://cran.r-project.org/src/contrib/locfit_1.5-9.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/locfit_1.5-9.1.tar.gz
Summary  : Local Regression, Likelihood and Density Estimation.
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-locfit-lib
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-locfit package.
Group: Libraries

%description lib
lib components for the R-locfit package.


%prep
%setup -q -c -n locfit

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523314387

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523314387
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library locfit
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library locfit
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library locfit
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library locfit|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/locfit/DESCRIPTION
/usr/lib64/R/library/locfit/INDEX
/usr/lib64/R/library/locfit/Meta/Rd.rds
/usr/lib64/R/library/locfit/Meta/data.rds
/usr/lib64/R/library/locfit/Meta/features.rds
/usr/lib64/R/library/locfit/Meta/hsearch.rds
/usr/lib64/R/library/locfit/Meta/links.rds
/usr/lib64/R/library/locfit/Meta/nsInfo.rds
/usr/lib64/R/library/locfit/Meta/package.rds
/usr/lib64/R/library/locfit/NAMESPACE
/usr/lib64/R/library/locfit/NEWS
/usr/lib64/R/library/locfit/R/locfit
/usr/lib64/R/library/locfit/R/locfit.rdb
/usr/lib64/R/library/locfit/R/locfit.rdx
/usr/lib64/R/library/locfit/data/ais.rda
/usr/lib64/R/library/locfit/data/bad.rda
/usr/lib64/R/library/locfit/data/border.rda
/usr/lib64/R/library/locfit/data/chemdiab.tab.gz
/usr/lib64/R/library/locfit/data/claw54.rda
/usr/lib64/R/library/locfit/data/cldem.tab.gz
/usr/lib64/R/library/locfit/data/cltest.rda
/usr/lib64/R/library/locfit/data/cltrain.rda
/usr/lib64/R/library/locfit/data/co2.rda
/usr/lib64/R/library/locfit/data/diab.tab.gz
/usr/lib64/R/library/locfit/data/ethanol.rda
/usr/lib64/R/library/locfit/data/geyser.rda
/usr/lib64/R/library/locfit/data/geyser.round.tab.gz
/usr/lib64/R/library/locfit/data/heart.rda
/usr/lib64/R/library/locfit/data/insect.tab.gz
/usr/lib64/R/library/locfit/data/iris.rda
/usr/lib64/R/library/locfit/data/kangaroo.rda
/usr/lib64/R/library/locfit/data/livmet.rda
/usr/lib64/R/library/locfit/data/mcyc.tab.gz
/usr/lib64/R/library/locfit/data/mine.rda
/usr/lib64/R/library/locfit/data/mmsamp.tab.gz
/usr/lib64/R/library/locfit/data/morths.rda
/usr/lib64/R/library/locfit/data/penny.tab.gz
/usr/lib64/R/library/locfit/data/spencer.rda
/usr/lib64/R/library/locfit/data/stamp.rda
/usr/lib64/R/library/locfit/data/trimod.tab.gz
/usr/lib64/R/library/locfit/help/AnIndex
/usr/lib64/R/library/locfit/help/aliases.rds
/usr/lib64/R/library/locfit/help/locfit.rdb
/usr/lib64/R/library/locfit/help/locfit.rdx
/usr/lib64/R/library/locfit/help/paths.rds
/usr/lib64/R/library/locfit/html/00Index.html
/usr/lib64/R/library/locfit/html/R.css
/usr/lib64/R/library/locfit/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/locfit/libs/locfit.so
/usr/lib64/R/library/locfit/libs/locfit.so.avx2
/usr/lib64/R/library/locfit/libs/locfit.so.avx512
