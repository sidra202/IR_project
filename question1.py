import re
import nltk
import string
import inflect
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

def deleteSigns(s):
    s = s.replace('.I','')
    s = s.replace('.T','')
    s = s.replace('.A','')
    s = s.replace('.W','')
    s = s.replace('.X','')
        
    return s


def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)

    return text.translate(translator)



def convert_number_to_word(text):
    engine = inflect.engine()

    temp_str = text.split()

    new_string = []
  
    for word in temp_str:
        if word.__getitem__(0).isdigit():
            word = word.replace(",", "")
            if word.isdigit():
                temp = engine.number_to_words(word)
                new_string.append(temp)
        else:
            new_string.append(word)
  
    temp_str = ' '.join(new_string)
    return temp_str


def split_dash_expression(text):
    return text.replace("-", " ")


def to_lower(text):
    return text.lower()




#docs_without_sw
def remove_stopwords(d):
    stop_words = stopwords.words("english")
    f = open("common_words.txt", "r")
    stop_words = stop_words + f.read().lower().split()
    stop_words = stop_words + [',']
    text_tokens = word_tokenize(d)
    tokens_without_sw = [word for word in text_tokens if not word in stop_words]
    filtered_sentence = (" ").join(tokens_without_sw)
    return filtered_sentence


def stemming(d):
    stemmer = PorterStemmer()
    text_tokens = word_tokenize(d)
    tokens_stemming = [stemmer.stem(word) for word in text_tokens ]
    filtered_sentence = (" ").join(tokens_stemming)
    return filtered_sentence