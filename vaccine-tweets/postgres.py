# -*- coding: utf-8 -*-
"""
@author: verascity

This script (which will eventually be modulized, someday, probably!) will set 
up a connection with a PostgreSQL database and populate it with information
collected from current_tweets' Twitter scraper.

"""

import psycopg2
import credentials as cd


def get_connection(dbname, host='localhost', user='user', password='password'):

    connect_str = "dbname={} host={} user={} password={}".format(dbname, host, user, password)

    return psycopg2.connect(connect_str)

