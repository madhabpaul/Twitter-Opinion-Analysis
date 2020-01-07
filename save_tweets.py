import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'o1KgaU6CH27oNsfsFhXSDxuGm'
consumer_secret = 'i0GqyOatL0YWvqwT7Q5A9uPrl0vYJ5MEcXDqcrXd0UJrGDLIeU'
access_token = '2545424857-Cr32dNpm1u6AY0lpNADMGHTYuC0Yr9j1NUKIUEc'
access_token_secret = 'IMXDqQGRVyzwyY0pZtInJOvhwtqVieYE801xcEMXAFy03'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
# Open/Create a file to append data
csvFile = open('indveng.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#INDvENG",count=100,
                           lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])