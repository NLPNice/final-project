# Data

We will use data from the [European Patent Office](https://www.epo.org/searching-for-patents/data/bulk-data-sets/text-analytics.html) which contains data from 1978 to 2019, roughly 5.8 million patents that rounds to approximately 210GB of data.

Since the huge amount of data available we will work with a subset of all the available data, in particular with files *...* which contains roughly *x* patents documents.

The notebook [DataExtraction](./DataExtraction.ipynb) contains the pipeline used to extract data from a single file.

Since we will be using several different files we converted the notebook to a single script, [data_extraction.py](./data_extraction.py), that takes care of looping over each single file, extracts the needed information and exports it for later usage in csv format.



