import tweepy
import configparser
import pandas as pd
#ENLACE DE YOUTUBE!! --> https://www.youtube.com/watch?v=Lu1nskBkPJU

#read configs
config=configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token= config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']
#print(api_key)
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token,access_token_secret)


api = tweepy.API(auth)

public_tweets = api.home_timeline()

print(public_tweets[0].created_at)
#.created_at --> fecha en la que fue creado
#.text --> texto
#.user.screen_name --> para ver quien creó el tweet

columns = ['Time', 'User', 'Tweet']
data = []
for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

df = pd.DataFrame(data,columns=columns)
df.to_csv('tweets.csv')