import tweepy, json


def print_tweet_info(tweet):

    print('*'*40)
    print('Tweet by:', tweet['text'])
    print('Tweet at:', tweet['created_at'])
    print('Id:', tweet['id'])
    print('Language:', tweet['lang'].title())
    user = tweet['user']
    print('Tweeted by:', user['name'], end=' ')
    if user['verified']:
        print('(Verified)')
    else:
        print('(Not Verified)')
    print('Location:', user['location'])
    print('who has', user['followers_count'], 'followers')
    original_tweet = tweet.get('retweeted_status')
    if original_tweet is None:
        print('This was an original tweet')
    else:
        print('This was retweeted', original_tweet['retweet_count'], 'times')
        original_user = original_tweet['user']
        print('The original tweet was', original_tweet['id'], 'from', original_user['name'])
    print('*'*40)


class TweetWriter(tweepy.streaming.StreamListener):

    def on_data(self, data_str):
        try:
            tweet_dictionary = json.loads(data_str)
            print_tweet_info(tweet_dictionary)
        except UnicodeEncodeError as e:
            print('****UnicodeEncodeError', e)
            return True

        return True

    def on_error(self, status):
        print('Error occurred, the status is', status)

def main():
    consumer_key = 'AEiJXrEzk4y5edY1DC2iYUqdy'
    consumer_secret = 'RDHf8dZ9nDlEUGxOv8TNoY6I6VjqS8vJxkh4Mvh94lTvcJ4hj6'
    access_token = '4847154993-UpHinTUthPDFLt0lgoAMWr6C1HmUVDbXKL85aqY'
    access_token_secret = 'O9m8mUB8JyKRAW4V8ZVf5fauLTq84CP3ybjNeAUUXrSRG'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    listener = TweetWriter()

    stream = tweepy. Stream(auth, listener)

    search_list = ['ww3']

    stream.filter(track=search_list)

main()
