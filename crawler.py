import math

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
				tfIDF = tfidf(termFrequency, inverseFreq)
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

def tfidf(tf, idf):
	return tf * idf

#here is where you define any method to retrieve an invertedIndex (mysql, textfile, static variable, etc.)
def getInvertedIndex():
	invertedIndex = {'hello': {1: [[3, 0.1]], 2: [[8, 0.3], [2, 0.1]], 4: [[1, 0.5], [7, 0.1]]}, 'world': {1: [[2, 0.8], [3, 0.4]], 4: [[3, 0.9]]}, 'there': {1: [[4, 0.1], [6, 0.2]], 4: [[1, 0.2], [8, 0.2]]}}
	return invertedIndex

#here is where you define any method to retrieve the number of total documents in the corpus (mysql num rows, textfile, static variable, etc.)
def getNumDocumentsTotal():
	numDocumentsTotal = 3000
	return numDocumentsTotal

searchPhrase('hello world there')