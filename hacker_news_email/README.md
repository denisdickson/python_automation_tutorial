# Projeto Scraper Python

    Projeto criado seguindo parte do tutorial do canal destinado
    a automação com python FreecodeCamp.org onde é ensinado a como
    criar um top de notícias do site HackerNews.

    Processo do script: 
        -Cria uma função para extrair e organizar dados do site HackerNews usando o beautifulsoup.
        - Compõe email organizado
        - configura login do emissor e emails dos receptores usando smtp
        -Cria titulo e assunto do email com datetime
        -Inicializa o server e envia o e-mail
        -sai do server



## Bibliotecas utilizadas :

### http requests import requests
### webscraping from bs4 import BeautifulSoup
### send the emailimport smtplib