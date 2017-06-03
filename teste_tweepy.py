import tweepy

# Consumer keys and access tokens, used for OAuth
consumer_key = 'l0AXEOXgxPbQSUk2ObxOGsVZ9'
consumer_secret = 'Akd3tw8g2uFLN5JkysaPm06A4qWaZA4waXi0EKk7l1OgK9cshV'
access_token = '851843353046130688-zE5MCedndemBa75TvodaSCrQgdE0v63'
access_token_secret = 'hPamyWQSOz8KPhqRVyHOEXRQD8btqYXRzhiLJsb6FIFOj'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    #encoded = string.encode("utf-8", errors='ignore')
    #print (encoded) 
    print(tweet.text)

