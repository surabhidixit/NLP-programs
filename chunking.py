
#we are trying to find words which are related to a given subject in a sentence
#we chunk into noun phrases
#descriptive group of words surrounding the noun
# we can only group things together as a chunk which are related to each other
#we make use of regular expressions regex
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
#punktsentencetokenizer is a unsupervised ml sentence tokenizer
#it can be trained although its pretrained
sample_text=state_union.raw("2006-GWBush.txt")
train_text=state_union.raw("2005-GWBush.txt")
#training the Punkt.. on sample text we can use a different text 
#to train
custom_sent_tokenizer=PunktSentenceTokenizer(train_text)

tokenized=custom_sent_tokenizer.tokenize(sample_text)
#a chunk gram is created 'r' here is optional and chunk is the name its looking #for it could be any other name too, RB is the part of speech we need ,can be
#any other too RB. means any character(this is reg expn syntax refer to this means any form of adverb and 0 or 1 of those
#NOW WE PARSE THE CHUNK
def process_content():
    try:
        for i in tokenized:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            chunkGram= r"""Chunk: {<RB.?>*<VB.?>*<NPP><NN>?}"""
            chunkParser= nltk.RegexpParser(chunkGram)
            chunked= chunkParser.parse(tagged)
            print(chunked)
            chunked.draw()
    except Exception as e:
        print(str(e))
process_content()
