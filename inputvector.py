import sys
import re
import os
from os import listdir
from os.path import isfile, join, isdir
from stemming.porter2 import stem
import nltk
from nltk.tag import pos_tag

wordsd_final=["all", "keep", "celebr", "emili", "sleep", "asian", "go", "follow", "hate", "privat", "sorri", "young", "send", "smile", "song", "far", "ical", "worst", "fall","veri", "appar", "exact", "cool", "tri", "magic", "die", "soooo", "quick", "enjoy", "work", "sigh", "direct", "past", "everytim", "second", "blue", "repli", "abl",     "current", "new", "ever", "public", "full", "never", "french", "let", "trent_reznor", "miser", "wait", "great", "insan", "tire", "ahead",
"anymor", "smoke", "pick",    "healthi", "extrem", "weird", "guilti", "tweet", "love", "joshwhite78", "extra", "win", "emot", "put", "instal", "txt", "use", "doubl", "visit", "next", "few", "live", "call", "gorgeous", "angri", "tell", "more", "flat", "almost", "relax", "babi", "sore", "holi", "actual", "glad", "ride", "pretend", "fli", "wors", "obvious","whatev", "learn", "meet", "aliv", "fabul", "give", "share", "high", "crazi", "want", "david", "everywher", "huge", "twitpic",
"end", "quot", "rather", "write","alway", "hot", "answer", "disappoint", "updat", "product", "watch", "earlier", "wrong", "mad", "beauti", "such", "welcom", "short", "favorit", "caus", "danni", "so",  "talk", "cute", "help", "over", "sooo", "soon", "cold", "still", "perfect", "thank", "alli", "better", "lt", "therefor", "ly", "then", "good", "nation", "break","tonit", "instead", "not", "now", "billi", "pregnant", "drop", "oliv", "mean", "hard", "yeah", "realli", "2day",
"happen", "special", "god", "re", "nite", "drink","free", "argh", "believ", "ask", "molli", "ate", "miss", "honest", "turn", "think", "first", "origin", "pleas", "major", "feel", "onc", "alreadi", "fast", "spanish","horribl", "fantast", "differ", "top", "sometim", "least", "too", "white", "final", "listen", "especi", "juli", "haven", "jump", "kind", "silli", "mcfli", "terribl",   "mind", "mine", "sad", "tonight", "say", "nick_cart", "have", "veryy", "breakfast", "sat", "also", "take",
"green", "singl", "even", "begin", "sure", "normal", "most", "regular", "don", "later", "upset", "drive", "hospit", "inde", "clean", "usual", "wow", "awesom", "ridicul", "show", "tommcfli", "bring", "bright", "rough", "find", "absolut", "onli", "pretti", "nervous", "hope", "forev", "busi", "black", "local", "offici", "unhappi", "do", "get", "stop", "cannot", "sunni", "lucki", "truli","anniversari", "bad", "stupid", "cri", "fair", "see", "asleep", "close", "best",
"wonder", "away", "rlli", "figur", "awak", "import", "15th", "joy", "entir", "here",   "key", "come", "last", "ill", "alon", "quiet", "ili", "mani", "whole", "wear", "sweet", "boat", "late", "due", "much", "damn", "interest", "basic", "alyssa_milano",    "sooooo", "wake", "togeth", "chill", "play", "look", "will", "near", "fun", "howev", "earli", "ve", "readi", "dannymcfli", "worri", "ive", "cant", "sudden", "im",      "rid", "sever", "belli", "open", "pay", "make", "same", "funni",
"itali", "complet", "evry1", "finish", "http", "social", "hang", "jealous", "feelin", "recent",        "overcast", "well", "tho", "english", "spend", "latest", "itouch", "just", "less", "laptop", "kill", "sleepi", "yet", "europ", "shaunjumpnow", "josh", "littl", "add",  "soooooo", "els", "real", "sonic", "rememb", "mayb", "read", "big", "ladi", "gonna", "dark", "know", "amp", "like", "incred", "lose", "right", "old", "often",          "twitter", "back", "b4", "home", "surpris",
"total", "chocol", "definit", "leav", "be", "run", "quit", "super", "central", "oh", "unfortun", "plus", "own", "every1",   "2nite", "elementari", "soo", "weather", "meeee", "there", "long", "happi", "start", "low", "forward", "music", "buy", "north", "enough", "hear", "true", "eat",        "nanda_marinho", "possibl", "wish", "up", "ur", "certain", "pic", "doesn", "general", "as", "aw", "probabl", "again", "googl", "no", "other", "sick", "nice", "poor",   "finali", "stay", "goin",
"ago","longer", "hungri", "serious", "bl3ss", "hello"]
f = open("update.txt","rU")
wordsl=[]
wordsd_temp={}
for line in f :
    start = line.find("u'message': u'" )+ 14
    end = line.find("', u'actor_id':")
    linei = line[start:end]
    wordsl=wordsl+[w for w in re.split('\W',linei.lower()) if w]
for elements in wordsl:
    element=stem(elements)
    if element in wordsd_final:
        if element in wordsd_temp:
            wordsd_temp[element]+=1
        else:
            wordsd_temp[element]=1
string=""
string+="1.0"
for i in range(len(wordsd_final)) :
    if wordsd_final[i] in wordsd_temp:
        string+=" "
        string+=str(i+2)
        string+=":"
        string+=str(wordsd_temp[wordsd_final[i]])
        string+='.0'
print string
