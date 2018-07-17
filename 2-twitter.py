import tweepy
import csv
from textblob import TextBlob

#Configuration for the API
consumer_key = 'eGbY1F6KF0LtKt4xt4ERhWfcW'
consumer_secret = 'zsdwcOYSXjfqemMaaKRezczsu7CD1236GNeWrebeBLaH9gN7tJ'

access_token = '730143916062838786-7BOU6W6wn7KCSotuEjfooQHul6zE9Za'
access_token_secret = 'LJPa0KlI4LEA4njbbAUFtCHFdwpZYsnkHLAwDQQSuxSxQ'

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