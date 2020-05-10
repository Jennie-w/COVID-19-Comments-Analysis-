import pandas as pd


from textblob import TextBlob 
a = pd.read_csv("321UScasesincreased.csv")

def sentiment(x):
    sentiment = TextBlob(x)
    return sentiment.sentiment.polarity
a['sentiment'] = a['comment'].apply(sentiment)

a

a.to_csv('321UScasesincreased_sentiment.csv', index  = False)