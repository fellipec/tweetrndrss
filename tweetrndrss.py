#!/usr/bin/env python3
from feedparser.util import FeedParserDict
import tweepy
import feedparser
import random
import sqlite3
import ssl
import requests
import datetime

#Contorno para erros do SSL com o feedparser
#Workarround to SSL errors with feedparser
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

#Informações de autenticação estão no arquivo auth.py
#Edite o arquivo sample_auth.py com as credenciais corretas e salve como auth.py
#Authentication information is on auth.py file. 
#Edit the file sample_auth.py with your correct credentials and save as auth.py
from auth import *

#Definições globais
#Global definitions
FeedURL = "https://www.reddit.com/r/ScarlettJohansson/.rss"
TweetMessage = 'Scarlett! \n'
useToD = True
TweetMorning = 'Scarlett passando para desejar um bom dia\n\n'
TweetAfternoon = 'Scarlett passando para desejar uma boa tarde\n\n'
TweetEvening = 'Scarlett passando para desejar uma boa noite\n\n'
TweetSize = 200
useImage = True
imageFile = 'scarlett.jpg'

#Mensagem variável conforme a hora do dia
#Message changing with time of day
if useToD:
    currentTime = datetime.datetime.now()
    if currentTime.hour < 12:
        TweetMessage = TweetMorning
    elif 12 <= currentTime.hour < 18:
        TweetMessage = TweetAfternoon
    else:
        TweetMessage = TweetEvening


#Inicialização do Banco de Dados
#Database init
conn = sqlite3.connect('rss.db')
cur = conn.cursor()

#Verifica se existe a tabela FEED
#Checks for the FEED table
cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='RSS' ''')
if cur.fetchone()[0]==0 : #Tabela RSS não existe, cria-se a tabela / Table don't exists, creat it
    conn.execute('''CREATE TABLE RSS (
    ID    CHAR(50) PRIMARY KEY NOT NULL,
    TITLE TEXT                 NOT NULL,
    LINK  TEXT,
    MEDIA TEXT);''')
    print("Tabela RSS Criada")
    conn.commit()
else :
    print("Tabela RSS já existe")

#Insere o RSS no banco de dados
#INSERT the RSS feed into the database
NewsFeed = feedparser.parse(FeedURL)
for entry in NewsFeed.entries:
    mediaurl = ''
    if entry.has_key('media_thumbnail') :
        mediaurl = entry.media_thumbnail[0]['url']
    cur.execute("INSERT OR IGNORE INTO RSS VALUES (?, ?, ?, ?)",(entry.id,entry.title,entry.link,mediaurl))
    conn.commit()

#Recupera o total de artigos salvos no banco de dados e sorteia um
#Finds the total of articles in the database and select a random one
cur.execute('SELECT COUNT(*) FROM RSS')
total = int(cur.fetchone()[0])
rndArticleID = random.randint(1,total)

#Recupera a entrada com o ID aleatório escolhido
#SELECTs the random article
cur.execute('SELECT LINK, TITLE, MEDIA FROM RSS WHERE ROWID = ?',(rndArticleID,))
article = cur.fetchone()

#Gera um Tuite com o título e URL do artigo
#Generates the Tweet
TweetText = TweetMessage # + article[1]
TweetText = TweetText[0:TweetSize-len(article[0])] + " " + article[0]
print(TweetText)

#Configura a API do Twitter
#Configure the Twitter API
authtw = tweepy.OAuthHandler(consumer_key(),consumer_secret())
authtw.set_access_token(access_token_key(),access_token_secret())
api = tweepy.API(authtw,wait_on_rate_limit=True)

if useImage:
    #Baixa a imagem do feed RSS
    #Download the image from RSS feed
    r = requests.get(article[2])
    pic = open(imageFile,'wb')
    pic.write(r.content)
    pic.close
    api.update_status_with_media(TweetText,imageFile)
else:
    #Apenas tuita um texto
    #Just tweet the text
    api.update_status(TweetText)

#Fecha o banco de dados
conn.commit()
conn.close()
