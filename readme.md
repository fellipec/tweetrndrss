### Warning! Because the API access to X (Formely Twitter) was disabled, this software doesn't work anymore and this repository will be archived
### Aviso! Como o acesso à API do X (anteriormente Twitter) foi desativado, este software não funciona mais e este repositório será arquivado.

TweetRndRSS
===========

Tuíta um artigo aleatório de um feed RSS
----------------------------------------

### Configuração

- No arquivo `tweetrndrss.py` ajuste as seguintes variáveis
     - `FeedURL` = A URL do feed que vai usar
    - `TweetMessage` = A mensagem do Tuíte antes do título do artigo
    - `TweetSize` = Tamanho máximo do texto
    - `useImage` = True para usar imagem
    - `imageFile` = nome do arquivo de imagem temporário
- Renomeie o arquivo `sample_auth.py` para `auth.py` e preencha com o `consumer_key` e `consumer_secret` que podem ser obtidos em `https://developer.twitter.com/en/portal/apps/new` 
- Execute o arquivo `gettoken.py` para obter o `access_token_key` e `access_token_secret` que devem ser preenchidos no arquivo `auth.py`

### Uso
Execute o arquivo `tweetrndrss.py`. Cada vez que for executado, um artigo aleatório do feed RSS será tuitado. Você pode usar o serviço `cron` no Linux ou o Agendador de Tarefas no Windows para automatizar a execução

TweetRndRSS
===========

Tweets a Random RSS Feed Article
--------------------------------

### Configuration

- Adjust the following variables in `tweetrndrss.py` file
     - `FeedURL` = The RSS feed URL
    - `TweetMessage` = Text to tweet before article name
    - `TweetSize` = Maximum tweet size
    - `useImage` = True to use images
    - `imageFile` = Temporary image name file
- Rename file `sample_auth.py` to `auth.py` and fills `consumer_key` and `consumer_secret` that you can get here `https://developer.twitter.com/en/portal/apps/new` 
- Run the file `gettoken.py` to autenthicate with Twitter to get `access_token_key` and `access_token_secret` which you should paste in `auth.py`

### Usage
Run the file `tweetrndrss.py`. Each time it runs, a random article from the RSS feed will be tweeted. You can use `cron` if running on Linux, or the Task Scheduler if running on Windows to automate the execution
