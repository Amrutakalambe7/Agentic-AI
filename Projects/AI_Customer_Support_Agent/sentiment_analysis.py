# Contains logic for performing sentiment analysis.
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

#download the necessary data
nltk.download('vader_lexicon')

#Initiate Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

#define a function to get the sentiment of the user input
def get_sentiment(user_input):
    sentiment_score = sia.polarity_scores(user_input)
    if sentiment_score['compound'] >= 0.05:
        return '😊 Positive'
    elif sentiment_score['compound'] <= -0.05:
        return '😔 Negative'
    else:
        return '😐 Neutral'
    
# Test the function with a sample input
if __name__ == "__main__":
    user_input = "I love this product. It's amazing!"
    sentiment_result = get_sentiment(user_input)
    print(f"Sentiment Analysis Result: {sentiment_result}")
