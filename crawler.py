import math
import ast

def searchPhrase(searchQuery):
	words = searchQuery.split()
	results = []
	documentScores = {}

	for word in words:
		res = searchWord(word)
		result = []
		result.append(word)
		result.append(res)
		results.append(result)

	for result in results:
		scores = result[1]

		for docResult in scores:
			tmp = documentScores.get(docResult[0], [0, 0])
			tmp[0] = tmp[0] + docResult[1]
			tmp[1] = tmp[1] + 1
			documentScores[docResult[0]] = tmp

	for doc in documentScores:
		print("Document: " + str(doc) + " received a score of " + str(documentScores[doc][0] / documentScores[doc][1]) + " for '" + searchQuery + '"')

	return

def searchWord(searchQuery):
	numDocumentsTotal = getNumDocumentsTotal()
	invertedIndex = getInvertedIndex()
	numDocumentsMatched = 0
	results = []
	for term in invertedIndex:
		if term == searchQuery:
			for doc in invertedIndex[term]:
				numDocumentsMatched = numDocumentsMatched + 1
			for doc in invertedIndex[term]:
				docScores = invertedIndex[term][doc]
				termFrequency = 0
				for docScore in docScores:
					termFrequency = (termFrequency + tf(docScore[0], docScore[1])) / 2
				docID = doc
				inverseFreq = idf(numDocumentsTotal, numDocumentsMatched)
				tfIDF = tfidf(termFrequency, inverseFreq, docID)
				result = []
				result.append(docID)
				result.append(tfIDF)
				results.append(result)
	return results

def tf(termFrequency, frequencyWeight):
	return 1 + math.log10(termFrequency * frequencyWeight)

def idf(totalDocuments, numberDocumentsContainingQuery):
	idf = math.log10(totalDocuments / numberDocumentsContainingQuery)
	return idf

def timeRelevanceWeight(docID):
    #for now, simply return weight of 1 so it doesn't affect calculations if it is used
    return 1.0

def tfidf(tf, idf, docID):
	return (tf * idf) * timeRelevanceWeight(docID)

#here is where you define any method to save the inverted index (mysql, textfile, static variable, etc.)
def saveInvertedIndex(invertedIndex):
	outputFile = open('invertedindex.txt', 'w')
	outputFile.write(str(invertedIndex))
	return

#here is where you define any method to retrieve an invertedIndex (mysql, textfile, static variable, etc.)
def getInvertedIndex():
	inputData = open('invertedindex.txt', 'r').read()
	invertedIndex = ast.literal_eval(inputData)
	return invertedIndex

#here is where you define any method to retrieve the number of total documents in the corpus (mysql num rows, textfile, static variable, etc.)
def getNumDocumentsTotal():
	numDocumentsTotal = 3000
	return numDocumentsTotal

searchPhrase('hello world there')