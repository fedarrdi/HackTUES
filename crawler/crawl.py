from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urlparse
import urllib.request
import requests
import database
import re
 
text_file = open('text.txt', 'at')

database.MakeTable()
 
def getData(URL, DM):
    print(URL)
    database.PushURL(URL)
    
    html_page = requests.get(URL, {'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(html_page.text, "html.parser")
    
    text_file.write(str(soup))  
    
    for link in soup.findAll('a'):
        URL = link.get('href')
        if URL and not URL.startswith('#'):
            if urllib.parse.urlparse(URL).netloc == '':
                URL = urllib.parse.urljoin(DM, URL)
                if not urllib.parse.urlparse(URL).scheme.startswith('http') and not urllib.parse.urlparse(URL).scheme.startswith('https'):
                    continue
            else:
                DM = urllib.parse.urljoin(urllib.parse.urlparse(URL).scheme, urllib.parse.urlparse(URL).netloc)
                if not database.URLvis(URL):
                    getData(URL, DM)

DM = "https://www.reddit.com"
URL = "https://www.reddit.com"
getData(URL, DM)
