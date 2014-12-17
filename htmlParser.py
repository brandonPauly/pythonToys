from html.parser import HTMLParser
from urllib.request import urlopen

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a {} start tag with attrs {}".format(tag,attrs))
    def handle_endtag(self, tag):
        print("Encountered a {} end tag".format(tag))

def testParser(url):
    content = urlopen(url).read().decode()
    parser = NodeParser()
    parser.feed(content)

class NodeParser(HTMLParser):
    def handle_data(self,data):
        print(data.strip())
