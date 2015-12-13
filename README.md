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
