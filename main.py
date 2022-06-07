import fileReader as fr
import question5 as q5
import question6 as q6
import question7 as q7
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def load_cor(dataset):
    file_name =dataset
    file_name=file_name+"_corpus.pkl"
    open_file = open(file_name, "rb")
    loaded_list = pickle.load(open_file)
    open_file.close()
    return loaded_list


def main_func(query,dataset):
    corpus=load_cor(dataset)
    query=[q5.text_processor(query)]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    Y = vectorizer.transform(query)
    return q7.cos_sim(X,Y)

