#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time

# 0A. Load all texts from Disk
import pickle
import random

t0 = time()

all_texts_file = "all_texts.pkl"
try:
    all_texts = pickle.load( open(all_texts_file, "r") )
except IOError:
    print "PLEASE CHANGE YOUR CURRENT DIR TO /code/\n"
    raise

# 0B. Take a random sample
random.seed(107)
random_texts = random.sample(all_texts, 3000)

t0 = round(time() - t0, 2)

# =====================================
# 1. Apply tf-idf model to selected sample
from sklearn.feature_extraction.text import TfidfVectorizer

t1 = time()

vectorizer = TfidfVectorizer(sublinear_tf = True, max_df = 0.5)
tfidf_model = vectorizer.fit_transform(random_texts)

t1 = round(time() - t1, 2)

# =====================================
# 2. Evaluating inertia for each K in range
from sklearn.cluster import KMeans

t2 = time()

scores = {}
for k in range(10, 25):
    km_model_test = KMeans(n_clusters = k, max_iter = 300, n_init = 5)
    km_model_test.fit(tfidf_model)

    scores[k] = km_model_test.inertia_

t2 = round(time() - t2, 2)

# =====================================
# 3. Graphing the results
import matplotlib.pyplot as plt

t3 = time()

k_values = scores.keys()
errors = scores.values()

plt.plot(k_values, errors)
plt.xticks(k_values)

plt.title('Inertia vs # of Clusters')
plt.xlabel('k')
plt.ylabel('Inertia')

plt.savefig("choosing_k.png")

t3 = round(time() - t3, 2)

# =====================================
# Sum-up time as performance measure
print "2. Choosing value for K: {0}".format(t0 + t1 + t2 + t3)
