#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import random

# 1A. Load all texts from Disk
all_texts_file = "all_texts.pkl"
all_texts = pickle.load( open(all_texts_file, "r") )

# 1B. Take a random sample
random.seed(107)
random_texts = random.sample(all_texts, 3000)

# ==================================
# 2. Apply tf-idf model to selected sample
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf = True, max_df = 0.5)
tfidf_model = vectorizer.fit_transform(random_texts)

# =====================================
from sklearn.cluster import KMeans

# 3A. Evaluating inertia for each K in range
scores = {}
for k in range(10, 25):
    km_model_test = KMeans(n_clusters = k, max_iter = 300, n_init = 5)
    km_model_test.fit(tfidf_model)

    scores[k] = km_model_test.inertia_

# 3B. Graphing
import matplotlib.pyplot as plt

k_values = scores.keys()
errors = scores.values()

plt.plot(k_values, errors)
plt.xticks(k_values)

plt.xlabel('k')
plt.ylabel('Inertia')

plt.title('Inertia vs # of Clusters')
plt.show()
