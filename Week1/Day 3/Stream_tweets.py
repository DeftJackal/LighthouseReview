import twitter
import json
import os
consumer_key = os.environ['TwitterAPIKey']
consumer_secret = os.environ['TwitterAPIKeySecret']
access_token = os.environ['TwitterAccessToken']
access_token_secret = os.environ['TwitterAccessTokenSecret']
api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)
def main(PATH, NAME, FILTER, LANGUAGES, limit):
    count = 0
    with open(os.path.join(PATH, NAME+'.txt'), 'a') as f:
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
        for line in api.GetStreamFilter(track=FILTER, languages=LANGUAGES):
            if count > limit:
                return
            else:
                f.write(json.dumps(line))
                f.write('\n')
                count += 1

lang = ['en', 'de']                
main('G:\LighthouseLabs\Data\Twitter', 'Happy', ':)', lang, 300)