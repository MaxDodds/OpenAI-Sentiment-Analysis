from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_sentiment_value(text):
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)['compound']