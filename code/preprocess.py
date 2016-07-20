#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import string
import pickle

def parse_out_text(f):
    f.seek(0)

    # decode utf-8, lowercase and strip, then encode
    content = f.read().decode('utf-8').lower().strip()
    content = content.encode('utf-8')

    # remove punctuation
    text = content.translate(string.maketrans("", ""), string.punctuation)
    return text

# Start the performance clock
from time import time
t0 = time()

# Read and process all files in texts/
path = '../texts'
try:
    filenames = os.listdir(path)
except OSError:
    print "PLEASE CHANGE YOUR CURRENT DIR TO /code/\n"
    raise

all_texts = []
for filename in filenames:
    filepath = path + '/' + filename
    article = open(filepath, 'r')

    text = parse_out_text(article)
    all_texts.append(text)

    article.close()

# Write to Disk
pickle.dump( all_texts, open("all_texts.pkl", "w") )

# Stop the performance clock & measure time
print "1. Preprocess time: {0}".format( round(time() - t0, 2) )
