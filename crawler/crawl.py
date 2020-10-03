from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urlparse
import urllib.request
import requests
import database
import clearText
import re 
text_file = open('text.txt', 'at')
database.MakeTable()
 

def headerExtractor(soup):
    for heading in soup.find_all(re.compile('^h[1-6]$')):
        text_file.write(heading.text.strip() + '\n')

def getData(URL, DM, depth):
    if depth == 2:
        return

    print(URL)
    database.PushURL(URL)
    
    html_page = requests.get(URL, {'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(html_page.text, "html.parser")
    
    headerExtractor(soup)
    
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

Theme = []
def generateTheme(query): 
    query = query.replace(' ', '+')
    URL = f"https://google.com/search?q={query}"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
  
    headers = {"user-agent": USER_AGENT}    
    resp = requests.get(URL, headers=headers)
    soup = BeautifulSoup(resp.content, "html.parser")
  
    for div in soup.find_all('div'):
        if div.find("div",{"id": 'search'}):
            for link in div.findAll('a'):
                URL = link.get('href')
                if URL is not None:
                    DM = urllib.parse.urljoin(urllib.parse.urlparse(URL).scheme, urllib.parse.urlparse(URL).netloc)
                    if urllib.parse.urlparse(URL).scheme.startswith('http') or urllib.parse.urlparse(URL).scheme.startswith('https'):
                        inf = (URL, DM)
                        Theme.append( inf )
                    
generateTheme("bgmama")

for link in Theme:
    print(link)
    getData(link[0], link[1], 0)
    print("<===========================>")
print("final")
   
clearText.clear()
#clearText.correctLines()
database.pushText()
