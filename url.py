from urllib.request import urlopen

def example1():
    url="http://www.cdm.depaul.edu"
    word="DePaul"
    file=urlopen(url)
    html=file.read().decode()
    print(html)
    print(html.count(word))

def countwords(address,wordList):
    file = urlopen(address)
    html = file.read().decode()
    for word in wordList:
        print('{} appears {} times'.format(word,html.count(word)))

