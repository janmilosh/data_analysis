from django.shortcuts import render
from django.http import HttpResponse
import twitter
import json

def index(request):
    return HttpResponse(get_tweets())

def get_tweets():

    # Twitter API key constants
    CONSUMER_KEY = '0c99AONeJmB57SeQEgzWScZMg'
    CONSUMER_SECRET ='TFPzeNc5zXQyCXmWGyO0uAgyquBYo48UDdBNiBqEbfoOayDdZD'
    OAUTH_TOKEN = '1580239388-OHIozETc2iWeVt9zwYAXmDE5xJpbhA8CozErc1m'
    OAUTH_TOKEN_SECRET = 'opIQ0yfQncpjOaQRM5J6JvuDnSdsFFY1hH4R6nDD0PlNZ'
    
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                                CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)

    WORLD_WOE_ID = 1

    US_WOE_ID = 23424977

    world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
    us_trends = twitter_api.trends.place(_id=US_WOE_ID)

    world_trends = [trend['name'] for trend in world_trends[0]['trends']]
    us_trends = [trend['name'] for trend in us_trends[0]['trends']]

    return us_trends