#!Python3

# http requests
import requests

# webscraping
from bs4 import BeautifulSoup

# send the email
import smtplib

# Email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime
now = datetime.datetime.now()

# email content place holder
content = ''


# extracting Hacker news Stories

def extract_news(url):
    print('Extracting hackernews stories...')
    cnt = ''
    cnt += ('<b> HN Top Stories: </b> \n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'Valign': ''})):
        cnt += ((str(i+1)+' :: '+tag.text+"\n"+'<br>') if tag.text != 'More' else '')
        # print(tag.prettify) #find_all('span', attrs={'class':'sitestr'})
    return(cnt)


cnt= extract_news('https://news.ycombinator.com/')
content += cnt
#print(content)
content += ('<br>-----</br>')
content += ('<br><br> End of Message')

