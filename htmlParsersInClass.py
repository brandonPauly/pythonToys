from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin

def testParser(url):
    content = urlopen(url).read().decode()
    # Change this line to test our parser
    parser = Collector(url)
    parser.feed(content)
    return parser.getLinks()

class Collector(HTMLParser):
    'collect a list of URLs from a page'
    def __init__(self, url):
        HTMLParser.__init__(self)
        self.lst = []
        self.url = url

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for item in attrs:
                # item is a tuple
                if item[0] == 'href' and 'mailto' not in item[1]:
                    self.lst.append(urljoin(self.url, item[1]))

    def getLinks(self):
        return self.lst

class DataCollector(HTMLParser):
    'collect the contents into a string'
    def __init__(self):
        HTMLParser.__init__(self)
        self.contents = ''

    def handle_data(self, data):
        self.contents += data

    def getData(self):
        return self.contents

class LinksParser(HTMLParser):
    'print the links in a page'
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for item in attrs:
                # item is a tuple
                if item[0] == 'href':
                    print(item[1])
    
class PrettyParser(HTMLParser):
    'print tags in an indented fashion'
    def __init__(self):
        'the constructor'
        HTMLParser.__init__(self)
        self.indent = 0

    def handle_starttag(self, tag, attrs):
        if tag not in ['br', 'p', 'img']:
            print('{}{} start'.format(' ' * self.indent, tag))
            self.indent += 4

    def handle_endtag(self, tag):
        if tag != 'p':
            self.indent -= 4
            print('{}{} end'.format(' ' * self.indent, tag))

class NodeParser(HTMLParser):
    def handle_data(self, data):
        print(data.strip())

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a {} start tag with attrs: {}".format(tag, attrs))
    def handle_endtag(self, tag):
        print("Encountered a {} end tag".format(tag))

