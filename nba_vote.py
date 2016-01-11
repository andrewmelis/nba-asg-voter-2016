import os, twitter
from datetime import datetime

def nba_votes():
    consumer_key = os.environ.get('CONSUMER_KEY', "not a real key")
    consumer_secret = os.environ.get('CONSUMER_SECRET', "not a real secret")
    access_token_key = os.environ.get('ACCESS_TOKEN_KEY', "not a real key")
    access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET', "not a real secret")
    api = login(consumer_key, consumer_secret, access_token_key, access_token_secret)
    players = os.environ.get('PLAYERS', "LeBron James").split(",")
    return [vote_for_player(api, player) for player in players]

def login(consumer_key, consumer_secret, access_token_key, access_token_secret):
    api = twitter.Api(consumer_key = consumer_key,
                      consumer_secret = consumer_secret,
                      access_token_key = access_token_key,
                      access_token_secret = access_token_secret)
    print api.VerifyCredentials()
    return api

def vote_for_player(api, player_name):
    update_text = "{} #NBAVOTE at {}".format(player_name, str(datetime.now()))
    return api.PostUpdate(update_text)

nba_votes()
