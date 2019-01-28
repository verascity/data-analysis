# -*- coding: utf-8 -*-
"""
@author: verascity

This module contains functions for use with Tweepy and the Twitter API. It 
will gather tweets from the previous 7 days about a topic, optionally from a
specific location, and save relevant information in a .json file. It then 
loads the json file into a Pandas dataframe.

"""

import tweepy
import json
import pandas as pd
import credentials



auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.ACCESS_KEY, credentials.ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, 
                 wait_on_rate_limit_notify=True)

tweet_dict = {}
for tweet in tweepy.Cursor(api.search, q='vaccine -filter:retweets -filter:replies', 
                           lang='en', tweet_mode='extended', result_type='recent',
                    geocode='45.7669047,-122.4940866,50mi').items(10):
    t_id = tweet.id_str
    tweet_dict[t_id] = tweet.full_text
    
print(tweet_dict)
