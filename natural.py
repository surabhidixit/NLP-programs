from nltk.tokenize import sent_tokenize, word_tokenize
example_text = "Hello Ms. Surabhi, how are you doing today? The weather is great and I have no idea about this thing."
#print(sent_tokenize(example_text))
print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print i

