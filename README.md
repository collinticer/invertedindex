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

####`tf(termFrequency, termWeight)`####

Default definition:

```python
def tf(termFrequency, frequencyWeight):
	return 1 + math.log10(termFrequency * frequencyWeight)
```

Example overriden function:

To learn more about term frequency, inverse document frequency, and Term frequency–Inverse document frequency calculations, [this page](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) is a great starting point.

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
	return tf * idf
```

Example overriden function:

```python
def tfidf(tf, idf):
	return (tf * idf)
```
