# -*- coding: utf-8 -*-
"""
@author: verascity

This module contains functions for use with Tweepy and the Twitter API. It 
will gather tweets from the previous 7 days about a topic, optionally from a
specific location, and save relevant information in a .json file. It then 
loads the json file into a Pandas dataframe.

"""

import tweepy
import pandas as pd
import credentials


def dict_from_api(query, geocode=None, limit=100):
    
    tweet_dict = {}
    
    try:
        tweets = tweepy.Cursor(api_setup().search, q=query, lang='en', 
    tweet_mode='extended', result_type='recent', geocode=geocode).items(limit)
    except tweepy.TweepError as err:
        print(err.api_code)
    
    for tweet in tweets:    
        tweet_dict[tweet.id_str] = tweet.full_text
        
    return tweet_dict

def api_setup():
    
    auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, 
                               credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.ACCESS_KEY, 
                          credentials.ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
                 wait_on_rate_limit_notify=True)
    
    return api


    
print(dict_from_api('vaccine -filter:retweets -filter:replies', 
                    geocode='45.7669047,-122.4940866,50mi', 
                    limit=2))

