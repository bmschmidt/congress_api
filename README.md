This repo is used to fetch and parse some data used as a demo for building the MySQL database behind a [Bookworm](http://bookworm.culturomics.org) using [Presidio](https://github.com/bmschmidt/Presidio). The data consists of summaries of bills in US Congress and the corresponding metadata for each bill.

# Download the Data #

```python
python get_and_unzip_data.py
```

This will download and unzip the data using the multiprocessing module to do everything in parallel.

# Parse the Data #

```python
python congress_parser.py
```

This will prep the data by creating the individual .txt files for each bill as well as build the **jsoncatalog.txt** file.
