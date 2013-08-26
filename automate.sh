`python fb.py` > update.txt
wait 15
python inputvector.py > test
java -cp /home/peeyush/libsvm-3.17.src/libsvm-3.17/java/libsvm.jar svm_predict -b 1 test model out
tail -1 out | awk '{print $1}' > test.txt
cp prediction.txt rishav@hackyourworld.org:public_html/test.txt
