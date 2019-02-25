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
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score

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
    X_train, X_test, y_train, y_test = train_test_split(vaccine_df['text_clean'],
                                                        vaccine_df['status'],
                                                        test_size = 0.33)
    tknzr = RegexpTokenizer('\w+')
    cvec = CountVectorizer(lowercase=True, strip_accents = 'unicode', 
                           stop_words="english", min_df = 0.01,
                           max_df = 0.95, 
                           tokenizer = tknzr.tokenize)
    X_train_counts = cvec.fit_transform(X_train)
    tfidf_t = TfidfTransformer(use_idf=True)
    X_train_tfidf = tfidf_t.fit_transform(X_train_counts)
    clf = MultinomialNB().fit(X_train_tfidf, y_train)
    y_pred = clf.predict(cvec.transform(X_test))
    print(accuracy_score(y_test, y_pred))