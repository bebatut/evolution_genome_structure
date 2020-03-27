cd src
tar -zxvf aevol.tar.gz
cd aevol
aclocal
automake
autoconf
./configure --without-x
make
