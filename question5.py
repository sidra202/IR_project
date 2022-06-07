import question1 as q1
import question2 as q2
import question3 as q3

def text_processor(text):
    # IMPORTANT :: Keep the sorting as it is
    text = q1.deleteSigns(text)
    text  = q3.date_processor(text)
    text = q1.remove_punctuation(text)
    text = q1.convert_number_to_word(text)
    text = q1.split_dash_expression(text)
    text = q1.to_lower(text)
    text = q1.remove_stopwords(text)
    text = q1.stemming(text)
    text = q2.lemmatize_all(text)

    return text


    
