import urllib.request
import xml.etree.ElementTree as ET

COUNT=10

WORLD_NEWS="https://news.google.com/news/feeds?output=rss"
INDIA_NEWS="https://news.google.co.in/news/feeds?output=rss"
KERALA_NEWS="https://news.google.co.in/news/feeds?output=rss&q=kerala"

response_string=urllib.request.urlopen(KERALA_NEWS + "&num=" + str(COUNT)).read().decode('utf-8')

root = ET.fromstring(response_string)

channel = root[0]
for item in channel.iter('item'):
	print(item[0].text)
	subprocess.call(["speak",item[0].text])