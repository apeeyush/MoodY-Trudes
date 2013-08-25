echo `python fb.py` > update.txt
sleep 1
python inputvector.py > test
java -cp /home/peeyush/libsvm-3.17.src/libsvm-3.17/java/libsvm.jar svm_predict -b 1 test model out
echo `python make_vector.py` > test.txt
scp test.txt rishav@hackyourworld.org:public_html/test.txt
