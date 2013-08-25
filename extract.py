import nltk
from nltk.tag import pos_tag

wordsd_final = {}
wordsd={}       ## Dictionary for storing word list and count of body
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
    if len(element)>1:
        wordsd_final[element] = wordsd[element]
