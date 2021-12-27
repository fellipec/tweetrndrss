TweetRndRSS
===========

Tweets a Random RSS Feed Article
--------------------------------

### Configuração

- No arquivo `tweetrndrss.py` mude a URL do `NewsFeed` para o feed que deseja tuitar
- Renomeie o arquivo `sample_auth.py` para `auth.py` e preencha com o `consumer_key` e `consumer_secret` que podem ser obtidos em `https://developer.twitter.com/en/portal/apps/new` 
- Execute o arquivo `gettoken.py` para obter o `access_token_key` e `access_token_secret` que devem ser preenchidos no arquivo `auth.py`

### Uso
Basta executar o arquivo `tweetrndrss.py`. Cada vez que for executado, um artigo aleatório do feed RSS será tuitado. Você pode usar o serviço `cron` no Linux ou o Agendador de Tarefas no Windows para automatizar a execução