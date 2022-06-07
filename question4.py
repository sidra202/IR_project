#q4
from textblob.en import Spelling
import re
from nltk.tokenize import word_tokenize

############OFFLINE################

# textToLower = ""

# with open("CISI.txt","r") as f1:                        # Open our source file
#     text = f1.read()                                  # Read the file                 
#     textToLower = text.lower()                        # Lower all the capital letters

# words = re.findall("[a-z]+", textToLower)             # Find all the words and place them into a list    
# oneString = " ".join(words)                           # Join them into one string

# pathToFile = "CISI_train.txt"                              # The path we want to store our stats file at
# spelling = Spelling(path = pathToFile)                # Connect the path to the Spelling object
# spelling.train(oneString, pathToFile) 



############################ONLINE################3
def f(dataset,query):
    pathToFile= dataset
    pathToFile=pathToFile+"_train.txt"
    spelling = Spelling(path = pathToFile)     
    q=word_tokenize(query)
    w=[]
    for word in q:
        w.append(spelling.suggest(word))

    s=[]
    for sub in w:
        s.append(sub[0][0])


    sugQuery=""

    for word in s:
        sugQuery+=word
        sugQuery+=" "

    return sugQuery
