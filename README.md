Label the News
==============

<img src="http://i.imgur.com/Zy5MiEs.jpg" alt="Entropy Logo" height="180" width="180" align="right" />

_"Label the News"_ is one of the two challenges in Junior Division at **Entropy 2016 (final round)** - Vietnam's first academic competition in Data Science, before Data Science becomes a buzzword.

This problem is a classical NLP text classification one, i.e., before Deep Learning. I posted here since it contributes to [my final prize](https://www.facebook.com/entropy.jvn/photos/pb.100064899933338.-2207520000./1620025078310865/).

**Outline of README**

- [Problem Summary](#problem-summary)
- [Solution Plan](#solution-plan)
- [Detailed Algorithms](#detailed-algorithms)
- [Outputs](#outputs)
  + [Why 18 clusters](#why-18-clusters)
  + [Naming clusters](#naming-clusters)
  + [results.csv](#csv-output)
  + [Performance](#performance)
- [Comments](#comments)


## Problem Summary

Given 28 thousands text files, each represents an article in Vietnamese without category:

1. Find the best category for each article
2. The process has to be time-effective (not too slow)


## Solution Plan

We will approach the problem as an Unsupervised Learning one, with 3 requirements:

1. Group articles by content similarities
2. Name those groups
3. Do it effectively!

On requirement 1, we need to represent these texts by vectors, a.k.a **feature extraction**, then apply a **clustering algorithm** to those extracted vectors.

On requirement 2, we have to inspect each group's content. Since there are too many texts, we may want to do it with a **random sample** from each group.

On requirement 3, a primary performance bottleneck is the number of features and algorithm complexity. We will solve this with **feature selection** and **K-Means clustering** (reasonable complexity).

Here is the solution plan:

0. Clean the texts (lowercased, no punctuation)
1. Use **TF-IDF representation** to represent those texts (set **limit** for _number of features_)
2. Use **elbow method** to find the best value of K in the **estimated range**
3. Apply **K-means clustering** to build K clusters (or groups) by content similarities
4. Take a **random sample** from each group, inspect their contents, then label the group
5. Output a .csv file with rows of (*filename* + *category*) for each article


## Detailed Algorithms

### Cleaning Texts (code/preprocess.py)

1. Read all files in **texts/** directory
2. For each file (UTF-8 encoded): lowercase, strip and remove punctuation
3. Write processed files to disk

### Choosing K (code/choosing_k.py)

First, we have to estimate a range for K. Take a random sample of 30 articles from the archive, all of them is from [VnExpress][2], which has 18 categories.

On other famous news sites, the number varies from 14 to 20 categories. Hence, a reasonable estimate would be 10 to 24, with a strong focus around 18.

Since we have to apply K-means clustering multiple times (10 to 24), for performance reasons, we'll only apply it to a 10% random sample of the archive.

1. Read processed files from disk
2. Take a random sample of 3000 files
3. Use **Tf-Idf to represent** each sampled file
4. Fit the representation to **K-Means for K from 10 to 24**
5. Graph then use **elbow method to choose K**

The best value of K is 18. [Why?](#why-18-clusters)

### Clustering (code/clustering.py)

1. Read processed files from Disk
2. Use **Tf-Idf to represent** each file
3. Fit the representation to **K-Means at K = 18**
4. Use **dictionary to represent** 18 clusters
5. Write dictionary to disk
6. For each cluster, take a **random sample of 10 articles**, print them out and decide the category

### results.csv (code/output.py)

At this step, we should have a category associated with each cluster.

1. Load the **dictionary of 18 clusters** from disk
2. Load all files in **texts/** directory
3. For each file: find its associated cluster (using the dictionary), then the cluster's category
4. Build a **DataFrame** of filename and its category
5. Export **results.csv**


## Outputs

### Why 18 clusters

<img src="http://i.imgur.com/fojcNTh.png" alt="Elbow Graph" height="400" />

By the **elbow method**, there are two crucial points on the graph: K=11 and K=18. Since we're focused around K=18, we choose this value.

### Naming clusters

As noted before, we take a random sample of 10 articles in each cluster to decide its category, the process goes as this:

1. For each sampled article, **google its title**
2. Note down the category of the original article
3. Choose the most repeated category

``` python
{ 0: 'Education', 1: 'Business', 2: 'Tech News', 3: 'Entertainment',
  4: 'Business', 5: 'Family', 6: 'Travel', 7: 'Laws',
  8: 'Laws', 9: 'World News', 10: 'Science', 11: 'Health',
  12: 'Entertainment', 13: 'World News', 14: 'Family', 15: 'Video',
  16: 'Education', 17: 'Tech News' }
```

### CSV output

Detailed results are included in **results.csv**, where each row is a filename and its associated category (translated to English).

### Performance

Performance are measured directly in the code, then printed out.

1. Preprocess time: 249.89 seconds
2. Choosing value for K: 259.34 seconds
3. Building Clusters: 450.33 seconds


## Comments

### Duplication of clusters' titles

Since there are duplication in clusters' titles, we may over-estimate the value of K. However, this is not a problem, since inspecting sampled files from each cluster produce totally consistent results.

Digging deeper, duplication makes sense, since some clusters represent a sub-category instead of a category. For example, both cluster 0 and cluster 16 represent **Education**, but cluster 16 represents **"Learning English"** sub-category, and cluster 0 represent **all else in Education**.

Removing duplication, there are 11 categories in total, which is the other crucial point we noted during the **elbow method**. We may want to re-apply K-Means at K=11 and see the results.

### Vietnamese Language

To this point, there is no crucial difference between Vietnamese and English in this problem (except some UTF-8 encoding in the preprocessing).

However, we can boost performance by **removing stopwords** (and therefore reducing the number of features). The list of all stopwords in Vietnamese can be found using [JVnTextPro][3].

Some may even think of applying **stemming**, but to the best of my knowlege (a native speaker), Vietnamese is a monosyllabic language, and therefore stemming cannot be applied.


[1]: http://www.jvn.edu.vn/entropy/
[2]: http://vnexpress.net/
[3]: http://jvntextpro.sourceforge.net/
