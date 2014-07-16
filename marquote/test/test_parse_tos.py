import re
import urllib
from bs4 import BeautifulSoup

def test_first():
    from marquote.chain import Chain
    from marquote.Parser.startrek import StarTrekParser
    from marquote.Backend.mysqlbackend import SQLBackend

#    soup = BeautifulSoup(urllib.request.urlopen("http://www.chakoteya.net/startrek/episodes.htm"))
    url = "http://www.chakoteya.net/startrek/"
#    liste = []
#
#    for line in soup.find_all('a'):
#        if re.match('\d\d?\.htm', str(line.get('href'))):
#            liste.append(str(line.get('href')))
#
    chain = Chain(SQLBackend("mysql+mysqlconnector://marquote:marquote@localhost/marquote"))
    chain.parser = StarTrekParser()


#    for episode in liste:
#        chain.parse(url + episode,"TOS")
    chain.parse(url + "42.htm", "TOS")

    assert True

