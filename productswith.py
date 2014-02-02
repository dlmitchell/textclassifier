from __future__ import division
import json
import collections
import nltk
from nltk import *
from nltk.probability import *
from nltk.corpus import names
import random


# to run:
#> python productswith.py xbox|playstations|keurig| 
def main(args):

	name = args[1]
	
	is_text = make_text(make_lower(open("text/" + name + "/is.txt").read()))
	not_text = make_text(make_lower(open("text/" + name + "/not.txt").read()))

	dist1 = print_diversity(is_text)
	dist2 = print_diversity(not_text)

	# words from set one not in set two
	print "\n==== Set difference of first group ====\n"
	for d in dist1.keys()[:20]:	
		print d, percentage(not_text.count(d), len(not_text))

	print "\n==== Set Difference of second group ====\n"
	for d in dist2.keys()[:20]:	
		print d, percentage(is_text.count(d), len(is_text))

	classify(name)


def classify(name):
	is_the_thing = get_lines(open("text/" + name + "/is.txt").read())
	is_not_the_thing = get_lines(open("text/" + name + "/not.txt").read())

	things = ([(thing, 'is_the_thing') for thing in is_the_thing] + 
			  [(thing, 'is_not_the_thing') for thing in is_not_the_thing])

	random.shuffle(things)

	featuresets = [(features(n), g) for (n,g) in things]
	train_set, test_set = featuresets[75:], featuresets[:75]
	classifier = nltk.NaiveBayesClassifier.train(train_set)
	print classifier.show_most_informative_features(50)

	all_things = get_lines(open("text/" + name + "/all.txt").read())
	for line in all_things:
		if classifier.classify(features(line)) is "is_the_thing":
			print line

# Takes a list of 
def make_text(contents):
	return Text(nltk.word_tokenize(contents))

def print_diversity(text):	
	print "--====--"
	dist = FreqDist(text)
	for k in dist.keys()[:20]:
		print k, percentage(text.count(k), len(text))

	return dist

# ------------------------------------------------------------------------------------------	

def features(word):
	features = {}
	# features['first_word'] = word.split(' ')[0]
	features['has(gb)'] = ('gb' in word.lower())
	features['has(and)'] = ('and' in word.lower())	
	# features['has(for)'] = ('for' in word.lower())
	return features
 	
# ------------------------------------------------------------------------------------------		

def get_lines(file_biz):
	strings = []

	split = file_biz.split('\n')

	for s in split:
		strings.append(s.lower().strip())

	return strings

def make_lower(file_biz):
	strings = []
	split = file_biz.split(' ')

	for s in split:
		strings.append(s.lower().strip())


	return  " ".join(strings)


# ------------------------------------------------------------------------------------------

def percentage(count, total):
	return 100 * count / total

# ------------------------------------------------------------------------------------------

def lexical_diversity(text):
	return len(text) / len(set(text))

# ------------------------------------------------------------------------------------------	

if __name__ == '__main__':
	main(sys.argv)

