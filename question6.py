#q6
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import question5 as q5
import fileReader as fr
import pickle

def offLine_tfidf(dataset):
    corpus=fr.docsAsStrings(dataset)
    corpus=[q5.text_processor(d) for d in corpus ]
    vectorizer = TfidfVectorizer()
    X= vectorizer.fit_transform(corpus)
    return X

def load_tfidf(dataset):
    file_name =dataset
    file_name=file_name+".pkl"
    open_file = open(file_name, "rb")
    loaded_list = pickle.load(open_file)
    open_file.close()
    return loaded_list
    

def online_tfidf(query):
    vectorizer = TfidfVectorizer()
    query=[q5.text_processor(query)]
    Y = vectorizer.transform(query)
    return Y
