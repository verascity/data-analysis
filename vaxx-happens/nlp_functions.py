# -*- coding: utf-8 -*-
"""
@author: verascity

This module contains functions for natural language processing/sentiment
analysis. It uses the NLTK library to identify Tweet text as either pro- or 
anti-vaccination using a Naive Bayes classifier.
"""

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

def lemmatize(df):
    wnl = WordNetLemmatizer()
    df['text_clean'] = df['text_clean'].apply(lambda x: [wnl.lemmatize(w) for w in x])
    return df

def strip_all(df):
    df = strip_user_names(df)
    df = strip_links(df)
    df['text_clean'] = df['text_clean'].str.lower()  
    df = strip_non_words(df) 
    df = strip_stopwords(df) 
    return df

def strip_stopwords(df):
    stop_words = stopwords.words('english')
    df['text_clean'] = df['text_clean'].apply(lambda x: [w for w in x if w not in stop_words])
    return df

def strip_non_words(df):
    tknzr = RegexpTokenizer('\w+')
    df['text_clean'] = df['text_clean'].apply(tknzr.tokenize)
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

    print(vaccine_df.text_clean.head())