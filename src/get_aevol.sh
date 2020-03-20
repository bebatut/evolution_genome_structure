cd src
git clone git@gitlab.inria.fr:beslon/aevol_ltisee.git
cd aevol_ltisee
git checkout tags/v1.0.1
rm -rf examples
rm -rf .git
cd ../
tar -zcvf aevol_ltisee.tar.gz aevol_ltisee/
rm -rf aevol_ltisee/