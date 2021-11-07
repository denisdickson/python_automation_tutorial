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
        cnt += ((str(i+1)+' :: '+tag.text+"\n" + '<br>') if tag.text != 'More' else '')
        # print(tag.prettify) #find_all('span', attrs={'class':'sitestr'})
    return(cnt)


cnt = extract_news('https://news.ycombinator.com/')
content += cnt
# print(content)
content += ('<br>-----</br>')
content += ('<br><br> End of Message')

# Send the email

print('Composing Email...')

# update email details
SERVER = 'smtp.gmail.com'  # SMTP server
PORT = 587  # Port number
FROM = 'theemailtosendthemsgs'  # from email id
TO = 'itcanbealistofemails'  # my email ids
PASS = 'putyourpsswd'  # myemail id's password

# fp = open(file_name, 'rb')
# Create a text/plain message
#msg = MIMEText('')
msg = MIMEMultipart()

msg['Subject'] = 'Top New Stories HN[Automated Email]' + \
    ' '+str(now.day)+'-'+str(now.month)+'-'+str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))
# fp.close()

print('Initialing Server ... ')

server = smtplib.SMTP(SERVER, PORT)
#server = smtplib.SMTP_SSL('smtp.gmail.com',456)
server.set_debuglevel(0)  # set to 0 for not seeing errors
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent ... Quiting server ')

server.quit()
