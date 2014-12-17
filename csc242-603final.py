# CSC 242-603
# Final exam template
# Brandon Pauly

# You do not need to write doc strings

import os
from html.parser import HTMLParser
from urllib.request import urlopen, urljoin

# Question 1
# This class provided for reference -- do not modify
class intList(list):
    'a class for lists containing only integers'
    
    def __init__(self, items = []):
        for val in items:
            if type(val) != int:
                raise ValueError('{} is not an integer'.format(val))
        list.__init__(self, items)
        
    def __setitem__(self, i, val):
        if type(val) == int:
            list.__setitem__(self, i, val)
        else:
            raise ValueError('{} is not an integer'.format(val))

    def append(self, val):
        if type(val) == int:
            list.append(self, val)
        else:
            raise ValueError('{} is not an integer'.format(val))

    def extend(self, items):
        for val in items:
            if type(val) != int:
                raise ValueError('{} is not an integer'.format(val))
        list.extend(self, items)

    def insert(self, i, val):
        if type(val) == int:
            list.insert(self, i, val)
        else:
            raise ValueError('{} is not an integer'.format(val))

    def __iter__(self):
        return EvenIter(self)

# Write this class for the question

#Just couldn't figure out how to not return the None
# **** I think this works now
class EvenIter(object):
    def __init__(self, ilst):
        self.ilst = ilst
        self.index = 0

    def __next__(self):
        if self.index > len(self.ilst)-1:
            raise StopIteration
        # ***** Make sure you don't run off the end of the list
        while self.index < len(self.ilst) and ((self.ilst[self.index])%2) != 0:
            self.index += 1
        x = self.ilst[self.index]
        self.index += 1
        return x

# Question 2
def removeDups(s):
    if len(s) == 0:
        return ''
    elif len(s) == 1:
        return s
    else:
        x = removeDups(s[1:])
        if s[0].lower() == s[1].lower():
            return x
        else:
            return s[0] + x

# Question 3
def nestingCount(path):
    count = 1
    lst = []
    for item in os.listdir(path):
        n = os.path.join(path,item)
        try:
            # **** This looks fine
            lst.append(nestingCount(n))
        except:
            pass
    if len(lst) > 0:
        count += max(lst)
    return count
            

# Question 4
class ImageParser(HTMLParser):
    'a parser for images in an HTML file'
    
    def __init__(self, url):
        'constructor'
        HTMLParser.__init__(self)
        self.url = url
        self.urlList = []

    def handle_starttag(self, tag, attrs):
        'called when an opening tag is reached'
        if tag == 'img':
            self.urlList.append(urljoin(self.url,attrs[0][1]))

    def getItems(self):
        'return the image locations gathered'
        return self.urlList

def testIParser(url):
    'Test the ImageParser class'
    content = urlopen(url).read().decode()
    iParser = ImageParser(url)
    iParser.feed(content)
    return iParser.getItems()
