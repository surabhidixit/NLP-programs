#for creating plural to singular
#its better than stemming
#provides group of words together
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("better",pos="a"))
print(lemmatizer.lemmatize("run",pos="v"))
print(lemmatizer.lemmatize("doing",pos="v"))
print(lemmatizer.lemmatize("saw",pos="v"))
print(lemmatizer.lemmatize("would",pos="v"))