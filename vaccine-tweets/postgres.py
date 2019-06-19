# -*- coding: utf-8 -*-
"""
@author: verascity

This script (which will eventually be modulized, someday, probably!) will set 
up a connection with a PostgreSQL database and populate it with information
collected from current_tweets' Twitter scraper.

"""

import psycopg2


def get_connection(dbname):

    connect_str = "dbname={} host='localhost' user='user' password='password'".format(dbname)

    return psycopg2.connect(connect_str)