# Introduction to Python Development 


## CHAPTER 2.7
## Dictionaries (dicts)

1. Learn how to use dictionaries (the dict type) to hold onto key/value information in Python.

2. Python Documentation For 
    - [Dictionaries](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)


## Dictionaries
1. Dictionaries are the main mapping type that we'll use in Python. This object is comparable to a Hash or "associative array" in other languages.

## Things to note about dictionaries:

1. Unlike Python 2 dictionaries, as of Python 3.6 keys are ordered in dictionaries. Will need OrderedDict if you want this to work on another version of Python.
2. You can set the key to any IMMUTABLE type (no lists)
3. Avoid using things other than simple objects as keys.
4. Each key can only have one value (so don't have duplicates when creating a dict)
5. We create dictionary literals by using curly braces ({ and }), separating keys from values using colons (:), and separating key/value pairs using commas (,). Here's an example dictionary:
```python
>>> ages = { 'kevin': 59, 'alex': 29, 'bob': 40 }
>>> ages
{'kevin': 59, 'alex': 29, 'bob': 40}
```
6. We can read a value from a dictionary by subscripting using the key:
```python
>>> ages['kevin']
59
>>> ages['billy']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'billy'
```
7. Keys can be added or changed using subscripting and assignment:
```python
>>> ages['kayla'] = 21
>>> ages
{'kevin': 59, 'alex': 29, 'bob': 40, 'kayla': 21}
```
8. Items can be removed from a dictionary using the del statement or by using the pop method:
```python
>>> del ages['kevin']
>>> ages
{'alex': 29, 'bob': 40, 'kayla': 21}
>>> del ages
>>> ages
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ages' is not defined
>>> ages = { 'kevin': 59, 'alex': 29, 'bob': 40 }
>>> ages.pop('alex')
29
>>> ages
{'kevin': 59, 'bob': 40}
>>> {}.pop('billy')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'billy'
```
9. Since this is our second time running into a KeyError it's worth looking at a way to avoid these when we're attempting to read data from a dictionary. For that, we can use the get method:
```python
>>> ages.get('kevin')
59
>>> ages.get('billy')
>>>
```
10. Now we're receiving None instead of raising an error when we try to get the value for a key that doesn't exist.

11. It's not uncommon to want to know what keys or values we have without caring about the pairings. For that situation we have the values and keys methods:
```python
>>> ages = {'kevin': 59, 'bob': 40}
>>> ages.keys()
dict_keys(['kevin', 'bob'])
>>> list(ages.keys())
['kevin', 'bob']
>>> ages.values()
dict_values([59, 40])
>>> list(ages.values())
[59, 40]
```
12. Alternative Ways to Create a dict Using Keyword Arguments
There are a few other ways to create dictionaries that we might see, those being using the dict constructor with key/value arguments and a list of tuples:
```python
>>> weights = dict(kevin=160, bob=240, kayla=135)
>>> weights
{'kevin': 160, 'bob': 240, 'kayla': 135}
>>> colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla', 'red')])
>>> colors
{'kevin': 'blue', 'bob': 'green', 'kayla': 'red'}
```