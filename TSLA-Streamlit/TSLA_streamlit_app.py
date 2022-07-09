import re
import time
from datetime import datetime

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from PIL import Image
from plotly.subplots import make_subplots

# Read CSV file into pandas and extract timestamp data
dfSentiment = pd.read_csv("./sentiment_data.csv", index_col=0)
dfSentiment["timestamp"] = [
    datetime.strptime(dt, "%Y-%m-%d") for dt in dfSentiment["timestamp"].tolist()
]

# Multi-select columns to build chart
col_list = list(dfSentiment.columns)

r_sentiment = re.compile(".*sentiment")
sentiment_cols = [col for col in col_list if r_sentiment.match(col)]

r_post = re.compile(".*post")
post_list = [col for col in col_list if r_post.match(col)]

r_perc = re.compile(".*perc")
perc_list = list(filter(r_perc.match, col_list))

r_close = re.compile(".*close")
close_list = list(filter(r_close.match, col_list))

r_volume = re.compile(".*volume")
volume_list = list(filter(r_volume.match, col_list))

sentiment_cols = sentiment_cols + post_list
stocks_cols = perc_list + close_list + volume_list

# Config for page
st.set_page_config(
    page_title="TSLA Stock Sentiment Analysis",
    page_icon="✅",
    layout="wide",
)

with st.sidebar:
    # FourthBrain logo to sidebar
    fourthbrain_logo = Image.open("./images/fourthbrain_logo.png")
    st.image([fourthbrain_logo], width=300)

    # Date selection filters
    start_date_filter = st.date_input(
        "Start Data",
        min(dfSentiment["timestamp"]),
        min_value=min(dfSentiment["timestamp"]),
        max_value=max(dfSentiment["timestamp"]),
    )

    end_date_filter = st.date_input(
        "End Date",
        max(dfSentiment["timestamp"]),
        min_value=min(dfSentiment["timestamp"]),
        max_value=max(dfSentiment["timestamp"]),
    )

    sentiment_select = st.selectbox(
        "Select Sentiment",
        sentiment_cols,
        index=0,
    )
    stock_select = st.selectbox(
        "Select Stock Data",
        stocks_cols,
        index=0,
    )

# Banner with TSLA and Reddit images
tsla_logo = Image.open("./images/tsla_logo.png")
reddit_logo = Image.open("./images/reddit_logo.png")
st.image([tsla_logo, reddit_logo], width=200)

# dashboard title
st.title("TSLA Stock Sentiment Analysis")

## dataframe filter
# start date
dfSentiment = dfSentiment[
    dfSentiment["timestamp"]
    >= datetime(start_date_filter.year, start_date_filter.month, start_date_filter.day)
]

# end date
dfSentiment = dfSentiment[
    dfSentiment["timestamp"]
    <= datetime(end_date_filter.year, end_date_filter.month, end_date_filter.day)
]
dfSentiment = dfSentiment.reset_index(drop=True)


# creating a single-element container
placeholder = st.empty()

# near real-time / live feed simulation
for i in range(1, len(dfSentiment) - 1):

    # creating KPIs
    last_close = dfSentiment["close"][i]
    last_close_lag1 = dfSentiment["close"][i - 1]
    last_sentiment = dfSentiment["sentiment_score"][i]
    last_sentiment_lag1 = dfSentiment["sentiment_score"][i - 1]

    with placeholder.container():

        # create columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs
        kpi1.metric(
            label="Sentiment Score",
            value=round(last_sentiment, 3),
            delta=round(last_sentiment_lag1, 3),
        )

        kpi2.metric(
            label="Last Closing Price",
            value=round(last_close),
            delta=round(last_close - last_close_lag1),
        )

        # create two columns for charts
        fig_col1, fig_col2 = st.columns(2)

        with fig_col1:
            # Add traces
            fig = make_subplots(specs=[[{"secondary_y": True}]])

            fig.add_trace(
                go.Scatter(
                    x=dfSentiment["timestamp"][0:i],
                    y=dfSentiment[sentiment_select][0:i],
                    name=sentiment_select,
                    mode="lines",
                    hoverinfo="none",
                )
            )

            if sentiment_select.startswith("perc"):
                yaxis_label = "Percent Change Sentiment"

            elif sentiment_select in sentiment_cols:
                yaxis_label = "Sentiment Score"

            elif sentiment_select in post_list:
                yaxis_label = "Volume"

            fig.layout.yaxis.title = yaxis_label

            if stock_select.startswith("perc"):
                fig.add_trace(
                    go.Scatter(
                        x=dfSentiment["timestamp"][0:i],
                        y=dfSentiment[stock_select][0:i],
                        name=stock_select,
                        mode="lines",
                        hoverinfo="none",
                        yaxis="y2",
                    )
                )
                fig.layout.yaxis2.title = "% Change Stock Price ($US)"

            elif stock_select == "volume":
                fig.add_trace(
                    go.Scatter(
                        x=dfSentiment["timestamp"][0:i],
                        y=dfSentiment[stock_select][0:i],
                        name=stock_select,
                        mode="lines",
                        hoverinfo="none",
                        yaxis="y2",
                    )
                )

                fig.layout.yaxis2.title = "Shares Traded"

            else:
                fig.add_trace(
                    go.Scatter(
                        x=dfSentiment["timestamp"][0:i],
                        y=dfSentiment[stock_select][0:i],
                        name=stock_select,
                        mode="lines",
                        hoverinfo="none",
                        yaxis="y2",
                    )
                )

                fig.layout.yaxis2.title = "Stock Price ($USD)"

            fig.layout.xaxis.title = "Timestamp"

            # write the figure throught streamlit
            st.write(fig)

        st.markdown("### Detailed Data View")
        st.dataframe(dfSentiment.iloc[:, 1:][0:i])
        time.sleep(1)
