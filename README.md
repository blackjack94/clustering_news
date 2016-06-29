## Clustering News

1. **28 thousands** real Vietnamese articles, they are unlabeled
2. Find **Category** for each article
3. **Do it Effectively**

### PLAN (using sklearn)

(**preprocess.py**)

1. Read all files in _texts/_ directory
2. **Lowercase and Remove Punctuation** for each file
3. Write processed files to Disk

(**choosing_k.py**)

1. Read processed files from Disk
2. Take a **10% (3000) random files**
3. Use **Tf-Idf to represent** each sampled file
4. Fit the representation to **K-Means for K from 10 to 24**, and graph
5. Use **elbow method** to choose K (18)

(**clustering.py**)

1. Read processed files from Disk
2. Use **Tf-Idf to represent** each file
3. Fit the representation to **K-Means for K = 18**
4. Using dict to represent 18 clusters
5. Take a random sample of 10 articles in each cluster to **decide the cluster's name**
