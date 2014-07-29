from django.shortcuts import render
from django.http import HttpResponse
import twitter

def index(request):
    return HttpResponse("Hello, world. You're at the base_app index.")

def getTweets():
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)