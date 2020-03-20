cd src
tar -zxvf aevol_ltisee.tar.gz
cd aevol_ltisee
aclocal
automake
autoconf
./configure
make
