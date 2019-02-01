
import MeCab
from pprint import pprint
import pickle
import gensim
from gensim import corpora, models, similarities


output_words = []
output_words2 = []

m = MeCab.Tagger()

#text_reading
fi = open('line.txt','r', encoding='utf-8')
text = fi.read()
fi.close
keywords = m.parse(text)

#noun_extraction
for row in keywords.split("\n"):
    word = row.split("\t")[0]
    if word == "EOS":
        break
    else:
        pos = row.split("\t")[1].split(",")[0]
        if pos == "noun":
            output_words.append(word)
    #output_words2.append([output_words])
    
#mecab_print
print output_words

#mecab_writing

f2 = open('result.txt','w')
for x in output_words2:
    f2.write(str(x) + "\n")
f2.close()

file2 = f2.read()
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
raw  = file2
tokens = tokenizer.tokenize(raw)

print tokens

#make_dictionary
#dictionary = corpora.Dictionary()



