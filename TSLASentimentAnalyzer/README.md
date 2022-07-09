---
title: Demo
emoji: 📉
colorFrom: gray
colorTo: green
sdk: streamlit
sdk_version: 1.10.0
app_file: app.py
pinned: false
license: apache-2.0
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference


# quick start

1. install requirements with `pip install -r requirements`
2. create a .env file in the root directory and add the following variables:
   `REDDIT_API_CLIENT_ID` : the client ID of your reddit app
   `REDDIT_API_CLIENT_SECRET`: the client secret of your reddit app
   follow this tutorial to generate them. <https://www.jcchouinard.com/get-reddit-api-credentials-with-praw/>

3. run the streamlit app using :  `streamlit run app.py`

# scraping

the app use praw library to scrape submissions from reddit. A class named `scraper.RedditScraper` implements and abstracts that feature.

# sentiment analysis model
The model used in the application is a fine-tuned BERT-based model trained with labeled data scraped from TSLA subbreddit using a script that uses the scraping module `scraper.RedditScraper`.

The data is available in <https://huggingface.co/datasets/fourthbrain-demo/reddit-comments-demo> , availalbe in 2 versions (used later with DVC), and splitted into train/test datasets.
