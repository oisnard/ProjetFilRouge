import pandas as pd
import re
from bs4 import BeautifulSoup
import lxml
from unidecode import unidecode


from langdetect import detect_langs

import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

stop_words_fr = list(stopwords.words('french'))
stop_words_gr = list(stopwords.words('german'))
stop_words_en = list(stopwords.words('english'))

stop_words = stop_words_fr + stop_words_gr + stop_words_en

add_stop_words = ['les', 'pour', 'avec', 'des', 'ainsi', 'non', 'oui', 'etc', 'merci', 'bien', 'assez', 'lors', 'sans', 'plus', 'etre',
                  'tout', 'comme', 'tres']



lemmatizer = WordNetLemmatizer()

def remove_special_char(sentence):
    """ replace special characters (with space) disturbing language identification"""
    return re.sub(r'[^a-za-Z0-9]+', ' ', sentence)

def remove_html_tags(text):
    """ remove html tags of the input text"""
    if pd.notna(text):
        soup = BeautifulSoup(text, 'html.parser')
        return soup.getText()
    return ""

def remove_accent(text):
    """ replace the accents with standard characters fint the input text"""
    return unidecode(text)


def clean_text(text):
    """
    Remove html tags
    Replace the accents
    Remove special characters
    Return lower cases
    """
    if pd.isna(text):
        return str('')
    soup = BeautifulSoup(text, 'html.parser')
    tmp = soup.getText()
    tmp = unidecode(tmp)
    tmp = re.sub(r'[^a-zA-Z0-9]+', ' ', tmp)
    return tmp.lower()



def identify_language_langdetect(sentence):
    result = detect_langs(sentence)
    lan=[]
    for lang in result:
        lan.append([lang.lang, lang.prob])
    return lan[0][0], lan[0][1], len(lan)




def text_to_tokens(text):
    """ Process input to provide a list of tokens
    """
    if pd.isna(text):
        return str('')
    soup = BeautifulSoup(text, 'html.parser')
    text_tmp = soup.getText()
    text_tmp = unidecode(text_tmp)
    text_tmp = re.sub(r'[^a-zA-Z]+', ' ', text_tmp)
    text_tmp = text_tmp.lower()

    list_words = word_tokenize(text_tmp)
    tokens = []
    for word in list_words:
 #       if word.isdigit():  # Number are not kept
 #           continue
        if len(word)<=2:    # Short words are not kept
            continue
        if word in stop_words: # Stop words are not kept
            continue
        token = lemmatizer.lemmatize(word)
        if (word not in tokens):
            tokens.append(token)
   
    return tokens
    
