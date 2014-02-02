import nltk
import pymssql
from nltk.corpus import gutenberg


# con = pymssql.connect(host='192.168.50.86', user='david', password='1.dmitchell.1', database='ShopSavvy')
# cur = con.cursor()
# cur.execute("select top 20 * from products where  contains(title, '%playstation%') or contains(title, '%ps4%');")
# row = cur.fetchone()
# titles = []

emma = nltk.Text(gutenberg.words('austen-emma.txt'))
print len(emma)

for fileid in gutenberg.fileids():
	num_chars = len(gutenberg.raw(fileid))
	num_words = len(gutenberg.words(fileid))
	num_sents = len(gutenberg.sents(fileid))
	num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
	print int(num_chars/num_words), int(num_words/num_sents), int (num_words/num_vocab), fileid