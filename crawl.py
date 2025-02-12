from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urlparse
import urllib.request
import requests
import database
import clearText
import re 
import sys
import shutil

text_file = open('text.txt', 'at')

database.MakeTable()



def headerExtractor(soup):
    for heading in soup.find_all(re.compile(r'^h[1-6]$|^p$|^a$')):
        add =''
        if heading.name == 'h1':
            add = '# '
        if heading.name == 'h2':  
            add = '## '
        if heading.name == 'h3':
            add = '### '
        if heading.name == 'h4':
            add = '#### '
        if heading.name == 'h5':
            add = '##### '
        if heading.name == 'h6':
            add = '###### '
        if heading.name == 'a':
            add = '- '
        text_file.write(add + heading.text.strip() + '\n')


def clearURLS(URL):
    restrict={"api.", "feedback.","ads.","support.",".googleusercontent.com","policies.","translate.","maps.","adweek.", "play.google.com", "payments.google.com"}
    for res in restrict:
        if URL.find(str(res)) != -1:
            return 1
    return 0

def getData(URL, DM, depth):
    if depth == 2:
        return

    print(URL)
    database.PushURL(URL)

    html_page = requests.get(URL, {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'})
    soup = BeautifulSoup(html_page.text, "html.parser")

    if not html_page.status_code == 200:
        return

    headerExtractor(soup)

    for link in soup.findAll('a'):
        currURL = link.get('href')
        currDM = DM
        if currURL and not currURL.startswith('#'):
            if urllib.parse.urlparse(currURL).netloc == '':
                currURL = urllib.parse.urljoin(currDM, currURL)
            else:
                currDM = urllib.parse.urljoin(urllib.parse.urlparse(currURL).scheme, urllib.parse.urlparse(currURL).netloc)        
            
            if not currURL.startswith('http') and not currURL.startswith('https'):          
                continue

            if not database.URLvis(currURL) and not clearURLS(currURL):
                getData(currURL, currDM, depth + 1)

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
                    if urllib.parse.urlparse(URL).scheme.startswith('http') and  urllib.parse.urlparse(URL).scheme.startswith('https') and not clearURLS(URL):
                        inf = (URL, DM) 
                        Theme.append( inf )


theme_entry = sys.argv[1]
def main():
    generateTheme(str(theme_entry))
    step = 0
    final = int(len(Theme))
    for link in Theme:
        if step != 0 and step != final - 1:
            print(step)
            print("<===========================>")   
            print(link)
            getData(link[0], link[1], 0)
       
        if step == 2:
            break
        step = step + 1
    print("<!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>")
    print("ready")
    print("<!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>")
    clearText.clear()
    clearText.correctLines()
    database.pushText()
    shutil.copyfile('text.txt', 'text.md')
main()
