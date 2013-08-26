import sys
import re
import os
from os import listdir
from os.path import isfile, join, isdir
from stemming.porter2 import stem
import nltk
from nltk.tag import pos_tag

wordsd_final = {}
wordsd={}		## Dictionary for storing word list and count of body
pos_list=['JJ','JJR','JJS','NNP','NNPS','VB','VB*','RB','RBR']

f=open("infile","rU")
wordsl=[]
for line in f :
    wordsl=wordsl+[w for w in re.split('\W',line.lower()) if w]
tag=pos_tag(wordsl)

##tag is a tupule as it has been pos-tagged

for tup in tag:
    if tup[-1] not in pos_list:
        wordsl.remove(tup[0])

for elements in wordsl:
    element=stem(elements)
    if element in wordsd:
        wordsd[element]+=1
    else:
        wordsd[element]=1
f.close()

for element in wordsd:
	if wordsd[element]>2 and len(element)>1:
		wordsd_final[element] = wordsd[element]


fw = open('data.txt','w')
for element in wordsd_final:
    fw.write('"')
    fw.write(element)
    fw.write('"')
    fw.write(', ')
fw.close()

fw = open('workfile.csv', 'w')
fw.write("Emotion,")
for elements in wordsd_final:
    fw.write(elements)
    fw.write(',')
fw.write('\n')

i=0
f=open("infile","rU")
for line in f:
    wordsd_temp={}
    wordsl=[]
    wordsl=wordsl+[w for w in re.split('\W',line.lower()) if w]
    for elements in wordsl:
        element=stem(elements)
        print element
        print '\n'
        if element in wordsd_final:
            if element in wordsd_temp:
                wordsd_temp[element]+=1
            else:
                wordsd_temp[element]=1
    if (i<3520) :
        fw.write('1')
    elif (i<4752) :
        fw.write('2')
    elif (i<5022) :
        fw.write('3')
    elif (i<5077) :
        fw.write('4')
    i+=1
    for word in wordsd_final:
        if word in wordsd_temp:
            fw.write(',')
            fw.write(str(wordsd_temp[word]))
        else:
            fw.write(',0')
    fw.write('\n')
fw.close()
f.close()
