# Import sentiment analysis tool
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize analyzer
analyzer = SentimentIntensityAnalyzer()

# Get user input text
user_text = input("Please enter a sentence for sentiment analysis: ")

# Calculate sentiment scores
sentiment_scores = analyzer.polarity_scores(user_text)

# Extract score data
positive = sentiment_scores['pos'] * 100
negative = sentiment_scores['neg'] * 100
neutral = sentiment_scores['neu'] * 100
overall_score = sentiment_scores['compound']

# Display analysis result
print("\n===== AI Sentiment Analysis Report =====")
print(f"Positive Mood: {positive:.1f}%")
print(f"Negative Mood: {negative:.1f}%")
print(f"Neutral Mood: {neutral:.1f}%")
print("========================================")

# Judge overall sentiment
print("\nFinal Result:")
if overall_score > 0.05:
    print("Positive sentiment")
elif overall_score < -0.05:
    print("Negative sentiment")
else:
    print("Neutral sentiment")
