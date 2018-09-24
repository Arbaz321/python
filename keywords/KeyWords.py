'''

KeyWords.py - Arbaz Aziz

This program determines the key words in a document using tf-idf [term frequency - inverse document frequency] by reading the file, tokenizing the
file, storing the words in a dictionary with its tf score (how many times this words appears in this text) and its idf score. The final scores are computer by [tf * log(number of documents/number of documents where word is found)]

'''

#Dictionary of words with their scores 
	# {
	#   word name : {
	#					tf : 1,
	#                   docs : 1,
	#					tf-idf: 0
	#               }
	# } 

#Number of files in 'texts' folder (ordered files)
NUMBER_OF_OTHER_TEXT_FILES = 401 

#PURPOSE: Reads file and returns the text as a string 
#INPUT: Path to main text file 
#OUTPUT: File as a string
def readFile(path):
	with open(path, 'rb') as fp:
		return fp.read().decode('utf-8')

#PURPOSE: Reads file as string, removes special characters, lowercases, and tokenizes the words (split into list by spaces)
#INPUT: String of text
#OUTPUT: List of tokens (individual words)
import re
def tokenize(text):
	return re.sub(r'([^\s\w]|_)+', '', text).lower().split(' ')

def getOtherPathFile(fileNumber):
	if fileNumber < 10:
		return './texts/00' + str(fileNumber) + '.txt'
	elif  fileNumber < 100:
		return './texts/0' + str(fileNumber) + '.txt'
	else:
		return './texts/' + str(fileNumber) + '.txt'
#PURPOSE: Check if the token from main file is in the dictionary and update the term frequency (how many times it appears in main file) if token in dict
#INPUT: dictionary of words and the token/word to add to dictionary 
#OUTPUT: updated dictionary with words and dict of properties/[tf, df, docs]
def updateDictionaryTF(dictionary, token):
	#Using try because compiler returns "KeyError" if token not in dict
	try:
		#If token in dictionary already
		if dictionary[token]:
			#increment tf by 1
			dictionary[token]['tf'] += 1
	except:
		#if not in dictionary, add token and properties and default values of 1
		dictionary[token] = {
			'tf': 1, 
			'docs': 1,
			'tf-idf': 0
		}
	return dictionary

#PURPOSE: Check if token from other file is in dictionary of words from main file and add token to list of words found if token in dictionary
#INPUT: Dictionary of words and the token/word to add to dictionary
#OUTPUT: updated list with word if it is in dict
def updateList(dictionary, token, List):
	#Using try because compiler returns "KeyError" if token not in dict
	try:
		#If token in dictionary already
		if dictionary[token]:
			#increment tf by 1
			List.append(token)
	except:
		#If token not in dictionary, just return without doing anything
		pass
	return List

#PURPOSE: Loop through list of words in both other file and main file and increment their 'docs' property if found
#INPUT: dictionary of words and list of words (in both files) to increment
#OUTPUT: updated dictionary with document's doc count ('doc')
def updateDictionaryDOCS(dictionary, List):
	#Go through list of words
	uniqueWords = set(List)
	for word in uniqueWords:
		#increment 'docs' property of word
		dictionary[word]['docs'] += 1
	return dictionary

#PURPOSE: Go through dictionary and compute TF-IDF scores in each word
#INPUT: Dictionary of words, list of all the words in dictionary to loop through and look up, and number of total files
#OUTPUT: Updated dictionary of words from main text with tf-idf scores 
from math import log
def computeTFIDF(dictionary, tokens, numFiles):
	#tf * log(numFiles / docs)
	for token in tokens:
		tf = dictionary[token]['tf']
		df = dictionary[token]['docs']
		dictionary[token]['tf-idf'] = tf * log(numFiles / df) 
	return dictionary

#PURPOSE: Read in two words in the dictionary and sort them based on their tf-idf scores
#INPUT: Two entries from the dictionary
#OUTPUT: + or - number that determines if swap or not
def compare(dictionary, word1, word2):
	score1 = dictionary[word1]['tf-idf']
	score2 = dictionary[word2]['tf-idf']
	return score1 - score2

#Main Function
def main():	
	#Initialize dictionary of words
	words = dict() 
	# Read from file
	pathToMainFile = './texts/001.txt'
	mainFileText = readFile(pathToMainFile)
	# Tokenize file
	tokenizedMainFile = tokenize(mainFileText)
	# Read through tokens (list)
	for token in tokenizedMainFile:
		# Store them in dictionaries (key = word, value = dictionary storing tf and idf (default = 1))
		# Count term frequencies (tf) and store them in dictionary
		words = updateDictionaryTF(words, token)
	# Read each other file separately (to determine # of documents word appears in)
	for fileNumber in range(2, NUMBER_OF_OTHER_TEXT_FILES + 1):
		#Initialize a list of words in other document that match words in main file. This is made so we know which word's DOCS property to increment
		wordsInOtherFile = []
		pathToOtherFile = getOtherPathFile(fileNumber)
		otherFile  = readFile(pathToOtherFile)
		# Tokenize each file
		otherTokens = tokenize(otherFile)
		# Determine idf of each word
		for otherToken in otherTokens:
			# (1) Count how many times each token appears in other documents
			wordsInOtherFile = updateList(words, otherToken, wordsInOtherFile)
		# (2) Count how many documents each word appears in
		words = updateDictionaryDOCS(words, wordsInOtherFile)
	# Compute tf-idf (1)/(2) and Update dictionary
	words = computeTFIDF(words, tokenizedMainFile, NUMBER_OF_OTHER_TEXT_FILES+1)
	#sort words in main file based on tf-idf
	# simpleWordDictionary = dict()
	# import operator
	# for word in words:
		# simpleWordDictionary[word] = words[word]['tf-idf']
	# sorted_x = sorted(simpleWordDictionary.items(), key=operator.itemgetter(1), reverse=True)
	with open('./texts/stopwords.txt', 'rb') as fp:
		stopwords = fp.read().decode('ascii')
	
	# for word in tokenizedMainFile:
	# 	if(words[word]['tf-idf'] > 3):
	# 		print(word, ':', words[word]['tf-idf'])
	count = 0
	for word in tokenizedMainFile:
		# print(word, ":", words[word]['tf-idf'])
		if(word not in stopwords):
			# if(words[word]['tf-idf'] > 3):
	 		print(word, end=' ')
	 		count += 1

	print(count/len(tokenizedMainFile) * 100)
if __name__ == '__main__':
	main()