# CSC 242, Spring 2013
# Final exam study problem template
# Amber Settle

from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin, urlparse

# Question 1
class Crawler1(object):
    def __init__(self):
        self.visited = set()
            
    def crawl(self, url):
        'recursive web crawler that calls analyze() on each web page'
        links = self.analyze(url)
        self.visited.add(url)
        for link in links:
            x = urlparse(link)
            y = urlparse(url)
            try:
                if link not in self.visited and x.netloc == y.netloc:
                    self.crawl(link)
            except:
                pass
            
                
    def analyze(self, url):
        'returns the list of URLs found in the page url'
        print("Visiting", url)
        content = urlopen(url).read().decode()
        collector = Collector(url)
        collector.feed(content)
        urls = collector.getLinks()
        return urls

# Question 2
class Crawler2(object):
    def __init__(self):
        'constructor'
        self.discovered = set()

    def reset(self):
        'reset the visited links'
        self.discovered = set()

    def crawl(self, startURL):
        'an iterative breadth-first search web crawler'
        urlQueue = queue()
        urlQueue.enqueue(startURL)
        while urlQueue.isEmpty() == False:
            links = self.analyze(urlQueue[0])
            self.discovered.add(urlQueue[0])
            urlQueue.dequeue()
            for link in links:
                if link not in urlQueue and link not in self.discovered:
                    urlQueue.enqueue(link)
        

    def analyze(self, url):
        'returns the list of URLs found in the page url'
        print("Visiting", url)
        content = urlopen(url).read().decode()
        collector = Collector(url)
        collector.feed(content)
        urls = collector.getLinks()
        return urls

# Helper classes for Question 2
class queue(object):
    def __init__(self):
        self.q = []
    def dequeue(self):
        if self.isEmpty():
            raise EmptyQueueError('dequeue from empty queue')
        return self.q.pop(0)
    def enqueue (self, item):
        return self.q.append(item)
    def size(self):
        return len(self.q)
    def isEmpty(self):
        return (self.size() == 0)
    def __repr__(self):
        return self.q.__repr__()
    def __str__(self):
        return self.q.__str__()
    def __getitem__(self, key):
        return self.q[key]
    def __setitem__(self, key, value):
      self.q[key] = value
    def __iter__(self):
        return self.q.__iter__()
    
class EmptyQueueError(Exception):
    def __init__(self, value):
        self.v = value
    def __str__(self):
        return repr(self.v)
    
class Collector(HTMLParser):
    def __init__(self, url):
        HTMLParser.__init__(self)
        self.url = url
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http':
                        self.links.append(absolute)

    def getLinks(self):
        return self.links
