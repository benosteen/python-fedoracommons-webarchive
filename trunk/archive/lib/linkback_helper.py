from BeautifulSoup import BeautifulSoup

class LocationHTMLParser():
    def __init__(self):
        self.links = []

    def feed(self, html_text):
        soup = BeautifulSoup(html_text)
        pagelinks = soup.findAll('a')
        for link in pagelinks:
            if link.get('href', None):
                self.links.append(link.get('href', None))
            
    def get_links(self):
        return self.links
            
