# -*- coding: utf-8 -*-
"""
@author: verascity

This module contains functions for natural language processing/sentiment
analysis. It uses the NLTK library to identify Tweet text as either pro- or 
anti-vaccination using a Naive Bayes classifier.
"""

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

def lemmatize(df):
    wnl = WordNetLemmatizer()
    df['text_clean'] = (df['text_clean'].apply(lambda x: [wnl.lemmatize(w) for w in x.split(' ')])
                                        .apply(lambda x: ' '.join(x)))
    return df

def strip_all(df):
    df = strip_user_names(df)
    df = strip_links(df)
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
    vaccine_df = lemmatize(vaccine_df)
    tknzr = RegexpTokenizer('\w+')
    vec = TfidfVectorizer(lowercase=True, stop_words="english",
                           tokenizer = tknzr.tokenize)
    dtm = vec.fit_transform(vaccine_df['text_clean'])
    vec_df = pd.DataFrame(dtm.toarray(), columns=vec.get_feature_names())

    print(vec.get_feature_names())
 #   print(vaccine_df['text_clean'])