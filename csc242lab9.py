# CSC 242, Spring 2013
# Lab 9 
# Brandon Pauly

from html.parser import HTMLParser
from urllib.request import urlopen

# Question 1
class HeaderParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.insideHeader = False
        self.headings = []

    def handle_starttag(self, tag, attrs):
        if tag in ['h1','h2','h3','h4','h5','h6']:
            self.insideHeader = True
            

    def handle_endtag(self, tag):
        if tag in ['h1','h2','h3','h4','h5','h6']:
            self.insideHeader = False

    def handle_data(self, data):
        if self.insideHeader == True:
            self.headings.append(data.strip())

    def getHeadings(self):
        return self.headings

def testHParser(url):
    'Test the HeaderParser class'
    content = urlopen(url).read().decode()
    hParser = HeaderParser()
    hParser.feed(content)
    return hParser.getHeadings()

# Question 2
class ListParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.lstLst = []
        self.insideList = False

    def handle_starttag(self, tag, attrs):
        if tag == 'li':
            self.insideList = True

    def handle_endtag(self, tag):
        if tag == 'li':
            self.insideList = False

    def handle_data(self, data):
        if self.insideList == True:
            self.lstLst.append(data.strip())

    def getItems(self):
        return self.lstLst

def testLParser(url):
    'Test the ListParser class'
    content = urlopen(url).read().decode()
    lParser = ListParser()
    lParser.feed(content)
    return lParser.getItems()
