def headerExtractor(soup):
    for heading in soup.find_all(re.compile('^h[1-6]$')):  #re.compile tursi pattern
        print(heading.text.strip())
