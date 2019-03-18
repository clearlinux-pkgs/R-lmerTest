#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lmerTest
Version  : 3.1.0
Release  : 9
URL      : https://cran.r-project.org/src/contrib/lmerTest_3.1-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lmerTest_3.1-0.tar.gz
Summary  : Tests in Linear Mixed Effects Models
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-gtable
Requires: R-lazyeval
Requires: R-minqa
Requires: R-munsell
Requires: R-nloptr
Requires: R-pbkrtest
Requires: R-plyr
Requires: R-scales
Requires: R-tibble
BuildRequires : R-ggplot2
BuildRequires : R-gtable
BuildRequires : R-lazyeval
BuildRequires : R-lme4
BuildRequires : R-minqa
BuildRequires : R-munsell
BuildRequires : R-nloptr
BuildRequires : R-numDeriv
BuildRequires : R-pbkrtest
BuildRequires : R-plyr
BuildRequires : R-scales
BuildRequires : R-tibble
BuildRequires : buildreq-R

%description
for lmer model fits (cf. lme4) via Satterthwaite's degrees of freedom method. A
    Kenward-Roger method is also available via the pbkrtest package. Model selection
    methods include step, drop1 and anova-like tables for random effects (ranova).
    Methods for Least-Square means (LS-means) and tests of linear contrasts of fixed
    effects are also available.

%prep
%setup -q -c -n lmerTest

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552888272

%install
export SOURCE_DATE_EPOCH=1552888272
rm -rf %{buildroot}
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lmerTest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lmerTest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lmerTest
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  lmerTest || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lmerTest/CITATION
/usr/lib64/R/library/lmerTest/DESCRIPTION
/usr/lib64/R/library/lmerTest/INDEX
/usr/lib64/R/library/lmerTest/Meta/Rd.rds
/usr/lib64/R/library/lmerTest/Meta/data.rds
/usr/lib64/R/library/lmerTest/Meta/features.rds
/usr/lib64/R/library/lmerTest/Meta/hsearch.rds
/usr/lib64/R/library/lmerTest/Meta/links.rds
/usr/lib64/R/library/lmerTest/Meta/nsInfo.rds
/usr/lib64/R/library/lmerTest/Meta/package.rds
/usr/lib64/R/library/lmerTest/NAMESPACE
/usr/lib64/R/library/lmerTest/NEWS.md
/usr/lib64/R/library/lmerTest/R/lmerTest
/usr/lib64/R/library/lmerTest/R/lmerTest.rdb
/usr/lib64/R/library/lmerTest/R/lmerTest.rdx
/usr/lib64/R/library/lmerTest/data/Rdata.rdb
/usr/lib64/R/library/lmerTest/data/Rdata.rds
/usr/lib64/R/library/lmerTest/data/Rdata.rdx
/usr/lib64/R/library/lmerTest/help/AnIndex
/usr/lib64/R/library/lmerTest/help/aliases.rds
/usr/lib64/R/library/lmerTest/help/lmerTest.rdb
/usr/lib64/R/library/lmerTest/help/lmerTest.rdx
/usr/lib64/R/library/lmerTest/help/paths.rds
/usr/lib64/R/library/lmerTest/html/00Index.html
/usr/lib64/R/library/lmerTest/html/R.css
/usr/lib64/R/library/lmerTest/testdata/legacy_fits.RData
/usr/lib64/R/library/lmerTest/testdata/potdata.RData
/usr/lib64/R/library/lmerTest/testdata/test_paper_objects.RData
/usr/lib64/R/library/lmerTest/tests/test_a_utils.R
/usr/lib64/R/library/lmerTest/tests/test_anova.R
/usr/lib64/R/library/lmerTest/tests/test_compare_sas.R
/usr/lib64/R/library/lmerTest/tests/test_contest1D.R
/usr/lib64/R/library/lmerTest/tests/test_contestMD.R
/usr/lib64/R/library/lmerTest/tests/test_drop1.R
/usr/lib64/R/library/lmerTest/tests/test_legacy.R
/usr/lib64/R/library/lmerTest/tests/test_lmer.R
/usr/lib64/R/library/lmerTest/tests/test_lmerTest_paper.R
/usr/lib64/R/library/lmerTest/tests/test_ls_means.R
/usr/lib64/R/library/lmerTest/tests/test_ranova_step.R
/usr/lib64/R/library/lmerTest/tests/test_summary.R
/usr/lib64/R/library/lmerTest/tests/test_zerovar.R
/usr/lib64/R/library/lmerTest/tests/zlmerTest_zeroDenom.R
