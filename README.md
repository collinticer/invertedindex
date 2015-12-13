# invertedindex

To use this library, simply call:
```python
searchWord('word')
```

Or, to search an entire phrase by splitting the string at each space, use:
```python
searchPhrase('hello world')
```

To override the default term frequency calculation, define a custom `tf(termFrequency, termWieght)` function.

For example, the default definition of:

```python
def tf(termFrequency, frequencyWeight):
	return 1 + math.log10(termFrequency * frequencyWeight)
```

Could be overridden, as:

```python
def tf(termFrequency, frequencyWeight):
	return termFrequency
```
Which would output the raw term frequency.

Below, is information on overriding each of the functions.

To learn more about term frequency, inverse document frequency, and Term frequency–Inverse document frequency calculations, [this page](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) is a great starting point.

####`tf(termFrequency, termWeight)`####

Default definition:

```python
def tf(termFrequency, frequencyWeight):
	return 1 + math.log10(termFrequency * frequencyWeight)
```

Example overriden function:

```python
def tf(termFrequency, frequencyWeight):
	return termFrequency
```

####`idf(totalDocuments, numberDocumentsContainingQuery)`####

Default definition:

```python
def idf(totalDocuments, numberDocumentsContainingQuery):
	idf = math.log10(totalDocuments / numberDocumentsContainingQuery)
	return idf
```

Example overriden function:

```python
def idf(totalDocuments, numberDocumentsContainingQuery):
	idf = math.log10(1 + (totalDocuments / numberDocumentsContainingQuery))
	return idf
```

####`tfidf(totalDocuments, numberDocumentsContainingQuery)`####

Default definition:

```python
def tfidf(tf, idf, docID):
	return (tf * idf) * timeRelevanceWeight(docID)
```

Example overriden function:

```python
def tfidf(tf, idf, docID):
	#ommiting time relevance from calculation
	return tf * idf
```

####`timeRelevanceWeight(docID)`####

Default definition:

```python
def timeRelevanceWeight(docID):
    #for now, simply return weight of 1 so it doesn't affect calculations if it is used
    return 1.0
```

Example overriden function:

```python
def timeRelevanceWeight(docID):
    #would definitely want to perform some sort of database lookup in order to retrieve creation / last revised date for the document, hard coded values
    #I used are just for proof of concept, and would result in each document being weighted the same
    tuple_time = time.strptime("2004-06-03T00:44:35", "%Y-%m-%dT%H:%M:%S")
    firstDocPosted = time.mktime(tuple_time)#time at witch oldest document in results was posted. obvious dummy value for proof of concept
    tuple_time = time.strptime("2012-06-03T00:44:35", "%Y-%m-%dT%H:%M:%S")
    lastDocPosted = time.mktime(tuple_time)#initialize time of last document in results creation time
    tuple_time = time.strptime("2010-06-03T00:44:35", "%Y-%m-%dT%H:%M:%S")
    thisDocPosted = time.mktime(tuple_time)#initialize time of this documents creation to somewhere between first and last document
    timeRelevanceWeight = (thisDocPosted - firstDocPosted) / (lastDocPosted - firstDocPosted)
    return timeRelevanceWeight
```
