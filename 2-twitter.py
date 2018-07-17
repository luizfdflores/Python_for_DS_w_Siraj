import tweepy
import csv
from textblob import TextBlob

#Configuration for the API

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Get user input regarding the searched topic
try:
	selected_topic = input('Please, select the desired topic you want to search: ')
except:
	print('\nPlease provide a valid topic to be searched!')

# Get the tweets
public_tweets = api.search(selected_topic)

# Get a list with all tweets text
tweets = []
for tweet in public_tweets:
	tweets.append(tweet.text)
	#analysis = TextBlob(tweet.text)
	#print(analysis.sentiment)

# Write csv files with the data
out = csv.writer(open("2_{}_search_results.csv".format(selected_topic),"w"), delimiter=',',quoting=csv.QUOTE_ALL)
out.writerow(tweets)

print('CSV file was saved successfully!')
