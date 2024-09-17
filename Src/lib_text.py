import pandas as pd
import re
from bs4 import BeautifulSoup
import lxml
from unidecode import unidecode


from langdetect import detect_langs


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




