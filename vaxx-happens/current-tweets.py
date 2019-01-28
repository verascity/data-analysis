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

