#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 0. Titles of Clusters (some is duplicated)
cluster_titles = { 0: 'Education', 1: 'Business', 2: 'Tech News', 3: 'Entertainment',
                   4: 'Business', 5: 'Family', 6: 'Travel', 7: 'Laws',
                   8: 'Laws', 9: 'World News', 10: 'Science', 11: 'Health',
                   12: 'Entertainment', 13: 'World News', 14: 'Family', 15: 'Video',
                   16: 'Education', 17: 'Tech News' }

# 1. Read all files in texts/
#    Load all clusters
import os
import pickle

path = '../texts'
clusters_file = "clusters.pkl"
try:
    filenames = os.listdir(path)
    clusters = pickle.load( open(clusters_file, "r") )
except (OSError, IOError):
    print "PLEASE CHANGE YOUR CURRENT DIR TO /code/\n"
    raise

# 2. Build a list of categories for respective articles
categories = ['' for _ in range( len(filenames) )]

for cluster, articles in clusters.items():
    category = cluster_titles[cluster]
    for idx in articles:
        categories[idx] = category

# 4. Convert built dictionary to DataFrame & to_csv
import pandas as pd

articles_df = pd.DataFrame( { 'Title': filenames, 'Category': categories}, columns = ['Title', 'Category'] )

articles_df.to_csv('../results.csv')
