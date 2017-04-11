#stemmer means stemming words like riding ride which have the same meaning
#we use porterstemmer for this 
#the output will have python 
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps=PorterStemmer()
example_words=["python","pythoner","pythoning","pythoned","pythonly"]
new_text="It is very important to be pythonly with python. All pythoners have pythoned poorly at least once."
words=word_tokenize(new_text)
for w in words:
    print(ps.stem(w))
