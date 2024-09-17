import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer




nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
print(stopwords.words('french'))
stop_words_fr = stopwords.words('french')
stop_words_gr = stopwords.words('german')
stop_words_en = stopwords.words('english')
stop_words = stop_words_fr + stop_words_gr + stop_words_en
print(stop_words)

lemmatizer = WordNetLemmatizer()

text = "ceci est un essai"

words = nltk.word_tokenize(text, language='french')
print(lemmatizer.lemmatize(words))

