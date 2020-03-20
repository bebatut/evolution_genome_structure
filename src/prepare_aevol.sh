cd src
git clone git@gitlab.inria.fr:beslon/aevol_ltisee.git
cd aevol_ltisee
git checkout tags/v1.0.1
aclocal
automake
autoconf
./configure
make
