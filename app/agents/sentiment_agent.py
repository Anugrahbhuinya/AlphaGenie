from textblob import TextBlob

def analyze_sentiment(text="Reliance sees strong growth and positive outlook"):
    """
    Simple sentiment analysis (mock or real news later)
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "sentiment": sentiment,
        "score": float(round(polarity, 2))
    }