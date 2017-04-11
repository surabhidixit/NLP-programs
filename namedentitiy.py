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
def process_context():
    try:
        for i in tokenized[5:]:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            namedEnt=nltk.ne_chunk(tagged,binary=True)
            namedEnt.draw()

    except Exception as e:
        print(str(e))


process_context()
