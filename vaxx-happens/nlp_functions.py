# -*- coding: utf-8 -*-
"""
@author: verascity

This module contains functions for natural language processing/sentiment
analysis. It uses the NLTK library to identify Tweet text as either pro- or 
anti-vaccination using a Naive Bayes classifier.
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer