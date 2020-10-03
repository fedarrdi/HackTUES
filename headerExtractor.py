def headerExtractor(soup):
    for heading in soup.find_all(re.compile(r'^h[1-6]$|^p$')):  #re.compile tursi pattern ^nachalo &kray
        print(heading.text.strip()+"\n")
