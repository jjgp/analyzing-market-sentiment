from datetime import datetime

import pandas as pd
import requests


def GetStockData(
    API_KEY,
    symbol="TSLA",
    start_date="2020-01-01",
    end_date="2022-06-01",
    interval="1h",
):

    """
    Gets stock and crypto currency quotes from twelvedata.

    https://twelvedata.com/
    For more API documentation:
    https://twelvedata.com/docs
    Register for a free API Key:
    https://twelvedata.com/pricing

        Parameters:
            API_KEY - String:       twelvedata API key.
            symbol - String:        Stock ticker symbol (e.g TSLA, DOGE, etc.).
                                        For cryptocurrencies, use symbol/currency (e.g. DOGE/USD, DOGE/BTC, etc.)
            start_date - String:    Beginning date for quote. Format: YYYY-mm-dd

            end_date - String:      End date for quote. Format: YYYY-mm-dd
            interval - String:      Time interval(resolution) for quotes.
                                        values: 1h, 1day, 1week, 1month
        Returns:                    Request JSON and Pandas DataFrame

    """

    # Pre-process dates
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    days = end_date - start_date
    days = str(days.days)

    url = (
        "https://api.twelvedata.com/time_series?symbol="
        + symbol
        + "&interval="
        + interval
        + "&outputsize="
        + days
        + "&apikey="
        + API_KEY
    )

    # Send request to API to get json and load into pandas dataframe.
    r = requests.get(url)
    j = r.json()

    df = pd.DataFrame.from_dict(j["values"])

    df = df.rename(columns={"datetime": "timestamp"})

    return j, df


def NormalizeDates(df, timestamp_col="timestamp", interval="1h"):

    """
    Normalizes DataFrame to a specified time interval.

        Parameters:
            df - Pandas DataFrame
            timestamp_col - String:     The column name of the timestamp column in the DataFrame
            interval - String:          The interval for the timestamp to be normalized/truncate
                                            values: 1h, 1day, 1week, 1month, quarter
    """

    test_date = "2020-01-01 00:00"
    d1 = datetime.strptime(test_date, "%Y-%m-%d %H:%M")
    dfTest = pd.DataFrame({"timestamp": [d1]})
    dfTest.timestamp.dtypes

    if dfTest.timestamp.dtypes != df[timestamp_col].dtypes:
        try:
            df[timestamp_col] = [
                datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
                for dt in df[timestamp_col].tolist()
            ]
        except:
            pass

        try:
            df[timestamp_col] = [
                datetime.strptime(dt, "%Y-%m-%d %H")
                for dt in df[timestamp_col].tolist()
            ]
        except:
            pass

        try:
            df[timestamp_col] = [
                datetime.strptime(dt, "%Y-%m-%d") for dt in df[timestamp_col].tolist()
            ]
        except:
            pass

    if interval == "1h":
        df["hour"] = [dt.hour for dt in df[timestamp_col].tolist()]
        df[timestamp_col] = [
            datetime(dt.year, dt.month, dt.day) for dt in df[timestamp_col].tolist()
        ]
        df.groupby
        df = df.sort_values(timestamp_col)

    elif interval == "1day":
        df[timestamp_col] = [
            datetime(dt.year, dt.month, dt.day) for dt in df[timestamp_col].tolist()
        ]
        df = df.sort_values(timestamp_col)

    elif interval == "1week":
        df["year"] = [dt.year for dt in df[timestamp_col].tolist()]
        df["week"] = [dt.isocalendar()[1] for dt in df[timestamp_col].tolist()]
        df = df.sort_values(timestamp_col)

    elif interval == "1month":
        df[timestamp_col] = [
            datetime(dt.year, dt.month, 1) for dt in df[timestamp_col].tolist()
        ]
        df = df.sort_values(timestamp_col)

    elif interval == "quarter":
        df["year"] = [dt.year for dt in df[timestamp_col].tolist()]
        df["quarter"] = [dt.quarter for dt in df[timestamp_col].tolist()]
        df = df.sort_values(timestamp_col)
    return df
