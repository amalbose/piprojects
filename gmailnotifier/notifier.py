import feedparser
import urllib.request

USERNAME="amalbose"
PASSWORD="zfgkltsmpjcrkebr"
#PASSWORD="mkg@1947"

URL="https://amalbose@gmail.com:zfgkltsmpjcrkebr@mail.google.com/gmail/feed/atom"

response=urllib.request.urlopen(URL).read()
print(response)
