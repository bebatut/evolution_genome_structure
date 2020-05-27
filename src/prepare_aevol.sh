cd src
tar -zxvf aevol.tar.gz
cd aevol
sed -i -e 's/with-omp OFF/with-omp ON/g' CMakeLists.txt
cmake .
make
