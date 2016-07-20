#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time

# 0. Load all texts from Disk
import pickle

t0 = time()

all_texts_file = "all_texts.pkl"
try:
    all_texts = pickle.load( open(all_texts_file, "r") )
except IOError:
    print "PLEASE CHANGE YOUR CURRENT DIR TO /code/\n"
    raise

t0 = round(time() - t0, 2)

# =====================================
# 1. Apply tf-idf model to all texts
from sklearn.feature_extraction.text import TfidfVectorizer

t1 = time()

vectorizer = TfidfVectorizer(sublinear_tf = True, max_df = 0.5)
tfidf_model = vectorizer.fit_transform(all_texts)

t1 = round(time() - t1, 2)

# =====================================
# 2. Fit the tf-idf model to the final K-Means Model
from sklearn.cluster import KMeans

t2 = time()

km_model_final = KMeans(n_clusters = 18, max_iter = 300, n_init = 5)
km_model_final.fit(tfidf_model)

t2 = round(time() - t2, 2)

# =====================================
# 3. Using dict to represent clusters
import collections

t3 = time()

clusters = collections.defaultdict(list)
for text_id, label in enumerate(km_model_final.labels_):
    clusters[label].append(text_id)

# Write clusters to disk
pickle.dump( clusters, open("clusters.pkl", "w") )

t3 = round(time() - t3, 2)

# =====================================
# Sum-up time as performance measure
print "3. Building Clusters: {0}".format(t0 + t1 + t2 + t3)

# =====================================
# 4. Find the category of each label
import random

print "\n\n"
for cluster_id in clusters.keys():
    print "=============================="
    print "Cluster {0}".format(cluster_id)

    random_ids = random.sample(clusters[cluster_id], 10)
    for doc_id in random_ids:
        print all_texts[doc_id]
        print "----------\n\n"
