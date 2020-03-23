cd src
git clone git@gitlab.inria.fr:aevol/aevol.git
cd aevol
git checkout aevol_6
rm -rf examples
rm -rf .git
cd ../
tar -zcvf aevol.tar.gz aevol/
rm -rf aevol/