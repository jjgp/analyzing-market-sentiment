import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from config import settings
from loguru import logger
from scraper import RedditScraper
from transformers import pipeline

reddit = RedditScraper()
st.title("$TSLA Market Sentiment Analyzer using r/TSLA Subreddit")


def load_data(number, scraping_option):
    st.write("loading new data")
    # st.write(scraping_option)
    comments = []
    for submission in scraping_option(number):
        comments.extend(reddit.get_comment_forest(submission.comments))
        logger.debug(
            submission.title,
            submission.num_comments,
            len(reddit.get_comment_forest(submission.comments)),
        )
    df = pd.DataFrame(comments)

    return df


def select_scrap_type(option):
    if option == "Hot":
        st.write("Selected Hot submissions")
        return reddit.get_hot
    if option == "Rising":
        st.write("Selected rising submissions")
        return reddit.get_rising
    if option == "New":
        st.write("Selected new submissions")
        return reddit.get_new


st.info(
    "Option has been deactivated as the same submissions were scraped because the subreddit is not too active"
)
select = st.selectbox("choose option", ["Hot", "Rising", "New"], disabled=True)


number = st.number_input("Insert a number", step=1, max_value=30, min_value=3)


sentiment_pipeline = pipeline("sentiment-analysis", settings.model_path)

data = load_data(number, select_scrap_type("Hot"))


if st.button("Analyze"):
    results = sentiment_pipeline(list(data["comment"]))
    data["label"] = [res["label"] for res in results]
    data["sentiment_score"] = [res["score"] for res in results]
    st.write(data.groupby("label").count())
    sizes = list(data.groupby("label").count()["comment"])
    labels = "Negative", "Positive"
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")
    st.pyplot(fig1)


st.write(data)
