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

pd.set_option('display.max_colwidth', -1)

def dict_from_api(query, geocode=None, limit=1000):
    
    tweet_dict = {}
    for tweet in tweepy.Cursor(api_setup().search, q=query, 
    lang='en', tweet_mode='extended', result_type='recent',
    geocode=geocode).items(limit):
        
        try: 
            tweet_dict[tweet.id_str] = tweet.full_text
        except tweepy.TweepError as err:
            print(err.api_code)
        
    return tweet_dict

def api_setup():
    
    auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, 
                               credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.ACCESS_KEY, 
                          credentials.ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
                 wait_on_rate_limit_notify=True)
    
    return api

if __name__ == "__main__":
#    vaccine_dict = dict_from_api('vaccine -filter:retweets', 
#                    geocode='45.7669047,-122.4940866,300mi')
    vaccine_df = pd.DataFrame.from_dict(vaccine_dict, orient='index')
    vaccine_df.columns = ['text']