# -*- coding: utf-8 -*-
"""
@author: verascity

This module contains functions for natural language processing/sentiment
analysis. It uses the NLTK library to identify Tweet text as either pro- or 
anti-vaccination using a Naive Bayes classifier.
"""

from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

def stemmer(df):
    stemmer = SnowballStemmer('english')
    df['text_clean'] = df['text_clean'].apply(lambda x: ' '.join([stemmer.stem(w) for w in x.split(' ')]))
    return df

def strip_all(df):
    df = (strip_user_names(df)
         .pipe(strip_links))
    return df

def strip_links(df):
    df['text_clean'] = df['text_clean'].replace(r'https:\S+', '', regex=True)
    return df

def strip_user_names(df):
    df = create_clean_text_col(df)
    df['text_clean'] = df['text_clean'].replace(r'@[a-zA-Z0-9]+', '', regex=True)
    return df

def create_clean_text_col(df):
    df['text_clean'] = df['text']
    return df
    

if __name__ == "__main__":
    vaccine_df = strip_all(vaccine_df)
    vaccine_df = stemmer(vaccine_df)
    tknzr = RegexpTokenizer('\w+')
    vec = TfidfVectorizer(stop_words="english",
                           tokenizer = tknzr.tokenize)
    dtm = vec.fit_transform(vaccine_df['text_clean'])
    vec_df = pd.DataFrame(dtm.toarray(), columns=vec.get_feature_names())

    print(vec.get_feature_names())
 #   print(vaccine_df['text_clean'])
    
    
    
    
    
    
    
#    X_train, X_test, y_train, y_test = train_test_split(vaccine_df['text_clean'],
#                                                        vaccine_df['status'],
#                                                        test_size = 0.33)
#    tknzr = RegexpTokenizer('\w+')
#    vec = TfidfVectorizer(lowercase=True, stop_words="english",
#                           tokenizer = tknzr.tokenize)
#    bow = vec.fit_transform(vaccine_df['text_clean'])
#    vec_df = pd.DataFrame(bow.toarray(), columns=vec.get_feature_names())