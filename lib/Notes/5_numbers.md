# Introduction to Python Development 


## CHAPTER 2.2
## Numbers

Let's learn about some of the core data types in Python: the number types int and float.

## Python Documentation For This Video
[Numeric types (the int and float types) Official documentation](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)


## Numbers
- There are to main types of numbers we'll use in Python: int and float. For the most part, we won't be calling methods on number types â€” instead, we will use a variety of operators.
```python
>>> 2 + 2 # Addition
4
>>> 10 - 4 # Subtraction
6
>>> 3 * 9 # Multiplication
27
>>> 5 / 3 # Division
1.66666666666667
>>> 5 // 3 # Floor division, always returns a number without a remainder
1
>>> 8 % 3 # Modulo division, returns the remainder
2
>>> 2 ** 3 # Exponent
8
```
- If either of the numbers in a mathematical operation in Python is a float, then the other will be converted before carrying out the operation and the result will always be a float.

## Converting Strings and Numbers
- It's not uncommon for us to need to convert from one type to another when writing a script. Python provides built-in functions for doing that with the built-in types. For strings and numbers, we can use the str, int, and float functions to convert from one type to another (within reason).
```python
>>> str(1.1)
'1.1'
>>> int("10")
10
>>> int(5.99999)
5
>>> float("5.6")
5.6
>>> float(5)
5.0
```
You'll run into issues trying to convert strings to other types if they aren't present in the string.
```python
>>> float("1.1 things")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: '1.1 things'
```