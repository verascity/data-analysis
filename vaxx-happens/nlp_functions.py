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
    

vaccine_df = strip_user_names(vaccine_df)
vaccine_df = strip_links(vaccine_df)
vaccine_df = strip_non_words(vaccine_df)

print(vaccine_df.text_clean[0][0])