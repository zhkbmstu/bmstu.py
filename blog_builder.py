# coding: utf-8
import json


articles = json.load(open('articles.json', 'r'))

blog_file = open('blog.html', 'a')
blog_file.write('<html><head><meta charset="utf-8"><title>Статьи</title></head>\n<body>\n')	

for article in articles:
	print "%s:\"%s\"\n\t%s\n\n" % (article['author'], article['title'], article['text'])
	blog_file.write('<article>\n<h2>' + article['author'].encode('utf8') + ':"' + article['title'].encode('utf8') + '"</h2>\n<div>\n' + article['text'].encode('utf8') + '\n</div>\n</article>\n\n') 

blog_file.write("</body></html>")
blog_file.close()
