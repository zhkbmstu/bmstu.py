# coding: utf-8
import json


articles = json.load(open('articles.json', 'r'))

for article in articles:
	print "%s:\"%s\"\n\t%s\n\n" % (article['author'], article['title'], article['text'])