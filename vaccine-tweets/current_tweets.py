# -*- coding: utf-8 -*-
"""
@author: verascity

This module contains functions for use with Tweepy and the Twitter API. It 
will gather tweets from the previous 7 days about a topic, optionally from a
specific location, and save relevant information as a JSON string. It then 
loads the json file into a Pandas dataframe.

"""

import tweepy
import pandas as pd
import credentials

pd.set_option('display.max_colwidth', -1)

def df_from_api(query, geocode=None, limit=25):
    
    tweet_dict = {}
    for tweet in tweepy.Cursor(api_setup().search, q=query, 
    lang='en', tweet_mode='extended', result_type='recent',
    geocode=geocode).items(limit):
        
        try: 
            tweet_dict[tweet.id_str] = tweet._json
        except tweepy.TweepError as err:
            print(err.api_code)
    
    vaccine_df = pd.DataFrame.from_dict(tweet_dict, orient='index')
    
    return vaccine_df

def api_setup():
    
    auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, 
                               credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.ACCESS_KEY, 
                          credentials.ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
                 wait_on_rate_limit_notify=True)
    
    return api

if __name__ == "__main__":
    vaccine_df = df_from_api('vaccine -filter:retweets', 
                    geocode='40.6617743,-73.9710957,300mi')
    columns = ['created_at', 'id_str', 'full_text', 'entities',
               'in_reply_to_user_id_str', 'in_reply_to_screen_name',
               'user', 'is_quote_status', 'retweet_count', 'favorite_count']
    vaccine_df = vaccine_df[columns]
    user_df = vaccine_df['user'].apply(pd.Series)
    user_cols = ['id_str', 'name', 'screen_name', 'location', 'description', 
                 'created_at', 'verified', 'followers_count', 'friends_count', 
                 'listed_count', 'favourites_count', 'statuses_count']
    user_df = user_df[user_cols]
    ent_df = vaccine_df['entities'].apply(pd.Series).drop('symbols', axis=1)
#    hashtags = ent_df['hashtags'].apply(pd.Series) I need a better way to handle this.
#    mentions = ent_df['user_mentions'].apply(pd.Series)
    
    