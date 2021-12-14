
import pandas as pd
import numpy as np
# ML Packages For Vectorization of Text For Feature Extraction
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB  # Naive Bayes Classifier
import re

def process_post(post):
    # processes the text by removing usernames,urls,digits
    # converting the text into lowercase
    # removes all single characters, punctuations, extra spaces
    post = post.lower()                                           
    post = re.sub('@[^\s]+', '', post)                            
    post = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', ' ', post) 
    post = re.sub(r"\d+", " ", str(post))                         
    post = re.sub('&quot;'," ", post)                              
    post = re.sub(r"\b[a-zA-Z]\b", "", str(post))                 
    post = re.sub(r"[^\w\s]", " ", str(post))                     
    post = re.sub(r'(.)\1+', r'\1\1', post)                       
    post = re.sub(r"\s+", " ", str(post))                             
    return post
    

def prediction_result(datav):
    total_data = pd.read_csv("train.csv", encoding="ISO-8859-1")  

    pd.set_option('display.max_colwidth', -1)
    post = total_data.columns.values[2]
    sentiment = total_data.columns.values[1]    
    total_data['processed_post'] = np.vectorize(process_post)(total_data[post])

    count_vectorizer = CountVectorizer(ngram_range=(1,2))   
    final_vectorized_data = count_vectorizer.fit_transform(total_data['processed_post'])
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(final_vectorized_data, 
                                                            total_data[sentiment],
                                                            test_size=0.2, 
                                                            random_state=69)    
    comment2 = [datav]         
    check = count_vectorizer.transform(comment2).toarray()     
    model_naive = MultinomialNB().fit(X_train, y_train) 
    predicted_naive = model_naive.predict(check)
    print(predicted_naive)
    if predicted_naive == 1:
        result = 'Emergency'         
    else:
        result = 'Feedback'
    return result
            




