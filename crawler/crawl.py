from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urlparse
import urllib.request
import requests
import database
import re
 
text_file = open('text.txt', 'at')

database.MakeTable()
 
def getData(URL, DM, depth):
    if depth == 2:
        return

    database.PushURL(URL)
  
    html_page = requests.get(URL, {'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(html_page.text, "html.parser")
  
    if not html_page.status_code == 200:
        return 
    
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
                    getData(URL, DM, depth + 1)

DM = "https://reddit.com/"
URL = "https://reddit.com/"
getData(URL, DM, 0)
