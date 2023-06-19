#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-locfit
Version  : 1.5.9.8
Release  : 53
URL      : https://cran.r-project.org/src/contrib/locfit_1.5-9.8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/locfit_1.5-9.8.tar.gz
Summary  : Local Regression, Likelihood and Density Estimation
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-locfit-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
A note about license:
Earlier versions of locfit had a license which restricted usage.
The code was re-licensed by Prof. Loader in a version sent to
Andy Liaw in 2005 from which this CRAN distribution is derived.

%package lib
Summary: lib components for the R-locfit package.
Group: Libraries

%description lib
lib components for the R-locfit package.


%prep
%setup -q -n locfit
pushd ..
cp -a locfit buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1686587885

%install
export SOURCE_DATE_EPOCH=1686587885
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/locfit/libs/locfit.so
/usr/lib64/R/library/locfit/libs/locfit.so.avx2
/usr/lib64/R/library/locfit/libs/locfit.so.avx512
