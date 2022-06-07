# import question1 as q1 
#q2
# #limTokens
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize


# docs_stemming_CISI=q1.getdocs_stemming_CISI()
# docs_stemming_cacm=q1.getdocs_stemming_cacm()

# docs_stemming_CISI=["cisi1","cisi2"]
# docs_stemming_cacm=["cacm1","cacm2"]

def lemmatize_all(sentence):
    limTokens=[]
    wnl = WordNetLemmatizer()
    text_tokens = word_tokenize(sentence)
    for word, tag in pos_tag(text_tokens):
        if tag.startswith("NN"):
            limTokens.append(wnl.lemmatize(word, pos='n'))
        elif tag.startswith('VB'):
            limTokens.append(wnl.lemmatize(word, pos='v'))
        elif tag.startswith('JJ'):
            limTokens.append(wnl.lemmatize(word, pos='a'))
        else:
            limTokens.append(word)
    filtered_sentence = (" ").join(limTokens)
    return filtered_sentence

# docs_lem_CISI=[]
# docs_lem_cacm=[]

# for d in docs_stemming_CISI:
#     docs_lem_CISI.append(lemmatize_all(d))
# print("1")


# for d in docs_stemming_cacm:
#     docs_lem_cacm.append(lemmatize_all(d))
# print("2")

# def getdocs_lem_CISI():
#     return docs_lem_CISI

# def getdocs_lem_cacm():
#     return docs_lem_cacm



# # stemTokens.append("went")
# # stemTokens.append("was")
# print(docs_lem_cacm[0])
