from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
text = input("Enter the text: ")
score = analyzer.polarity_scores(text)
if score['compound'] >= 0.05:
   sentiment = "Positive"
elif score['compound'] <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"
print(f"Feedback Client :,{text}")
print(f"Sentiment : {sentiment}")