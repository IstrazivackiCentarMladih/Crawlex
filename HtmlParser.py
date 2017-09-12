from html.parser import HTMLParser
from urllib.parse import urlparse
import urllib.request

global all_links, local_links
all_links = []
local_links = []

class LinkParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):       
        for name,value in attrs:
            if name == 'href':
                all_links.append(value)
        return
        
def same_page_check(home_url,all_links):
    for url in all_links:
        if usporedba(home_url,url) == True:
            #print(url)
            local_links.append(url)
    return local_links

def usporedba(home_url,url):
    if network_location(home_url) == network_location(url) or network_location('//'+home_url) == network_location(url):
        print(home_url,url)
        return True
    return False

def network_location(url):
    o = urlparse(url,scheme='http')
    o = o.netloc
    return o

def main():
    url = input('url :')
    home_url = network_location(url)
    parser = LinkParser()
    parser.feed(urllib.request.urlopen(url).read().decode('utf8'))
    same_page_check(home_url,all_links)
    print(local_links)
    return


main()
