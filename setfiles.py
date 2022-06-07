import pickle
import question6 as q6
import question5 as q5
import fileReader as fr



corpus=fr.docsAsStrings("cacm")
corpus=[q5.text_processor(d) for d in corpus ]
open_file = open("cacm_corpus.pkl", "wb")
pickle.dump(corpus, open_file)
open_file.close()



_list=q6.offLine_tfidf("cacm")
file_name = "cacm.pkl"
open_file = open(file_name, "wb")
pickle.dump(_list, open_file)
open_file.close()


open_file = open(file_name, "rb")
loaded_list = pickle.load(open_file)
open_file.close()

print(loaded_list)
