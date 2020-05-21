# ShakespeareanBot

import tweepy as tp
import time
import os

# credentials to login to Twitter API
consumer_key = 'fODVsPdXIPZsJNH22nfkqhCns'
secret_key = 'csLcawy0V4ulslW6iNHjXFMyC0vitaAWwizA5A0pN1pQEO3iw4'
access_token = '1227708535061897216-tSPDwzNjeh6Yi4CEhj6fp5dX0Y7AxI'
secret_access = 'g8FzkuvOzGtbC9kl4NZOJITmpeJV3S2zPGKWeilBw9xgr'

# Login to Twitter Account API
auth = tp.OAuthHandler(consumer_key, secret_key)
auth.set_access_token(access_token, secret_access)
api = tp.API(auth)

os.chdir('jim_harbaugh')
for pic in os.listdir('.'):
  # update status for string based Tweet
  api.update_with_media(pic, '#GoBlue')
  time.sleep(5)
