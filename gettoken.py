#!/usr/bin/env python3
import tweepy

#Informações de autenticação estão no arquivo auth.py
#Edite o arquivo sample_auth.py com as credenciais corretas e salve como auth.py
from auth import *

auth = tweepy.OAuthHandler(consumer_key(),consumer_secret(),callback="oob")

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepyException:
    print("Failed to get request token")
 
print(redirect_url)    

verifier = input('Verifier:')

try:
    auth.get_access_token(verifier)
except tweepy.TweepyException:
    print("Failed to get request token")

print(auth.access_token)
print(auth.access_token_secret)
