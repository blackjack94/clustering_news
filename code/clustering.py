#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 0. Load all texts from Disk
import pickle

all_texts_file = "all_texts.pkl"
all_texts = pickle.load( open(all_texts_file, "r"))

# ==================================
# 1. Apply tf-idf model to all texts
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf = True, max_df = 0.5)
tfidf_model = vectorizer.fit_transform(all_texts)

# =====================================
# 2. Fit the tf-idf model to the final K-Means Model
from sklearn.cluster import KMeans

km_model_final = KMeans(n_clusters = 18, max_iter = 300, n_init = 5)
km_model_final.fit(tfidf_model)

# ===================================
# 3. Using dict to represent clusters
import collections

clustering = collections.defaultdict(list)
for text_id, label in enumerate(km_model_final.labels_):
    clustering[label].append(text_id)

# =================================
# (Example-only)
# 4. Guess the category of label-3:
import random

random_ids = random.sample(clustering[3], 10)
for doc_id in random_ids:
    print all_texts[doc_id]
    print "----------\n\n"
