# Data preprocessing

## Preprocessing
Data from EPO is highly structured. Arguably, being patents in the domain of law documents, descriptions and claims should be fairly consistent in the way they are written.

We didn't need to perform heavy preprocessing. Our current pipeline is fully contained in the notebook [Preprocessing.ipynb](./Preprocessing.ipynb). 
Files are hosted on Google Drive ([out_claim.zip](https://drive.google.com/file/d/1Lz0CJQ5YmGQWKmcOQtQFr3gzsR_3BYL0/view?usp=sharing), [out_descr.zip](https://drive.google.com/file/d/1LXXtd_To_5sDBTAa7Hq9pfW1zzO5Cuo7/view?usp=sharing), [out_title.zip](https://drive.google.com/file/d/1HcFgE5uSuKSPSjRbBnAPHMcKLbmt48q9/view?usp=sharing)) to avoid the storage of large files on Github.

The result of the preprocessing yields the file [summaries_claims.zip]

## Content analysis
We noticed that handling long documents is a rather hard task, additionally patents and claims length varies from very long document to very short documents.
On the notebook [DatasetAnalysis.ipynb](./DatasetAnalysis.ipynb) we perform some analysis of the dataset in order to find wether its possible to remove some documents and retrieve a more balanced dataset.

