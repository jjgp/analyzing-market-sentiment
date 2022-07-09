from transformers import pipeline


# sentiment_pipeline = pipeline("sentiment-analysis")
# data = ["I love you", "I hate you"]
def predict(
    data, custom_model: str = "finiteautomata/bertweet-base-sentiment-analysis"
):
    sentiment_pipeline = pipeline("sentiment-analysis")
    return sentiment_pipeline(data)
