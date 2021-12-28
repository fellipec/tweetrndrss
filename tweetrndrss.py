#!/usr/bin/env python3
import tweepy
import feedparser
import random
import sqlite3
import ssl

#Contorno para erros do SSL com o feedparser
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

#Informações de autenticação estão no arquivo auth.py
#Edite o arquivo sample_auth.py com as credenciais corretas e salve como auth.py
from auth import *

#Definições
NewsFeed = feedparser.parse("https://somesite.net/feed/")

#Inicialização do Banco de Dados
conn = sqlite3.connect('rss.db')
cur = conn.cursor()

#Verifica se existe a tabela FEED
cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='RSS' ''')
if cur.fetchone()[0]==0 : #Tabela RSS não existe, cria-se a tabela
    conn.execute('''CREATE TABLE RSS (
    ID    CHAR(50) PRIMARY KEY NOT NULL,
    TITLE TEXT                 NOT NULL);''')
    print("Tabela RSS Criada")
    conn.commit()
else :
    print("Tabela RSS já existe")

#Insere o RSS no banco de dados
for entry in NewsFeed.entries:
    cur.execute("INSERT OR IGNORE INTO RSS VALUES (?, ?)",(entry.id,entry.title))
    conn.commit()

#Recupera o total de artigos salvos no banco de dados e sorteia um
cur.execute('SELECT COUNT(*) FROM RSS')
total = int(cur.fetchone()[0])
rndArticleID = random.randint(1,total)

#Recupera a entrada com o ID aleatório escolhido
cur.execute('SELECT ID, TITLE FROM RSS WHERE ROWID = ?',(rndArticleID,))
article = cur.fetchone()

#Gera um Tuite com o título e URL do artigo
TweetText = "Artigo antigo. Confira: " + article[1]
TweetText = TweetText[0:270-len(article[0])] + " " + article[0]
print(TweetText)

#Configura o Twitter
authtw = tweepy.OAuthHandler(consumer_key(),consumer_secret())
authtw.set_access_token(access_token_key(),access_token_secret())
api = tweepy.API(authtw,wait_on_rate_limit=True)

api.update_status(TweetText)

#Fecha o banco de dados
conn.commit()
conn.close()
