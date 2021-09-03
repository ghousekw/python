# Introduction to Python Development 


## CHAPTER 2.3
## Working with Variables

- Almost any script we write will need to have a way for us to hold on to information for use later on.
That's where variables come into play.

### Working with Variables
1. We can assign a value to a variable by using a single = and we don't need to (nor can we) specify the type of the variable.

```python
>>> my_str = "This is a simple string"
```
2. Now we can print the value of that string by using my_var later on:
```python
>>> print(my_str)
This is a simple string
```
3. Before, we talked about how we can't change a string because it's immutable. This is easier to see now that we have variables.

```python
>>> my_str += " testing"
>>> my_str
'This is a simple string testing'
```
4. That didn't change the string â€” it reassigned the variable. The original string of "This is a simple string" was unchanged.

5. An important thing to realize is that the contents of a variable can be changed, and we don't need to maintain the same type.
```python
>>> my_str = 1
>>> print(my_str)
1
```
6. Ideally, we wouldn't change the contents of a variable called my_str to be an int, but it is something that Python would let us do.

7. One last thing to remember is that if we assign a variable with another variable it will be assigned to the result of the variable and not whatever that varible points to later.
```python
>>> my_str = 1
>>> my_int = my_str
>>> my_str = "testing"
>>> print(my_int)
1
>>> print(my_str)
testing
```