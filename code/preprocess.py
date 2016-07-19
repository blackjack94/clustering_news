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

    ### remove punctuation
    text = content.translate(string.maketrans("", ""), string.punctuation)
    return text

path = '../texts'
try:
    filenames = os.listdir(path)
except OSError:
    print "Please change your current working directory to code/\n"
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
