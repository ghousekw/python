# Introduction to Python Development 


## CHAPTER 2.6
## Tuples & Ranges

1. The most common immutable sequence type that we're going to work with is going to be the tuple. We'll also look at the range type as an alternative to a sequential list.

2. Python Documentation For 
    - [Sequence Types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
    - [Tuples](https://docs.python.org/3/library/stdtypes.html#tuple)
    - [Ranges](https://docs.python.org/3/library/stdtypes.html#range)


## Tuples
1. Tuples are a fixed-width, immutable sequence type. We create tuples using parenthesis ((, )) and at least one comma (,):
```python
>>> point = (2.0, 3.0)
```
2. Since tuples are immutable, we don't have access to the same methods that we do on a list. We can use tuples in some operations like concatenation, but we can't change the original tuple that we created.
```python
>>> point_3d = point + (4.0,)
>>> point_3d
(2.0, 3.0, 4.0)
```
3. One interesting characteristic of tuples is that we can unpack them into multiple variables at the same time:
```python
>>> x, y, z = point_3d
>>> x
2.0
>>> y
3.0
>>> z
4.0
```
4. The time we're most likely to see tuples will be when looking at a format string that's compatible with Python 2:
```python
>>> print("My name is: %s %s" % ("Keith", "Thompson"))
```
## Ranges
1. Ranges are an immutable sequence type that defines a start, a stop, and a step value, and then the values within are calculated as it is iteracted with. 
2. This allows for ranges to be used in place of sequential lists and while taking less memory and including more items.
```python
>>> my_range = range(10)
>>> my_range
range(0, 10)
>>> list(my_range)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1, 14, 2))
[1, 3, 5, 7, 9, 11, 13]
```
3. Notice that the "stop" value is not included in the range, the values are all up-until the stop.
