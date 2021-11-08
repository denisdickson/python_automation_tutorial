#!Python3
# Importa conteúdo da página do tedtalk
import requests
# webscrapping
from bs4 import BeautifulSoup
# regular expression pattern matchin
import re
# from urllib.request import urlretrieve #downloading mp4
# for argument parsing
import sys

# ExceptionHandling
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED Talk URL")

#
#

# sends get requests to get content of url and store in object r
r = requests.get(url)

print("Download's about to start")

soup = BeautifulSoup(r.content, features="lxml")

for val in soup.findAll("script"):
    if(re.search("talkPage.init", str(val))) is not None:
        result = str(val)

result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")

mp4_url = result_mp4.split('"')[0]

print("Downloading videom from "+mp4_url)

file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]

print("Storing video in ... "+file_name)

r = requests.get(mp4_url)

with open(file_name, 'wb') as f:
    f.write(r.content)

# alternate method
#urlretrieve(mp4, url, file_name)

print("Download process finished")
