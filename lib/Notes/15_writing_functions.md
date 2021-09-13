# Introduction to Python Development 


## CHAPTER 4.1
## Writing Functions

- Being able to write code that we can call multiple times without repeating ourselves is one of the most powerful things that we can do when programming. Let's learn how to define functions in Python.

## Python Documentation For This Video
- [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

## Function Basics
1. We can create functions in Python using the following:
    - The def keyword
    - The function name - lowercase starting with a letter or     underscore (_) 
    - Left parenthesis (()
    - 0 or more argument names
    - Right parenthesis ())
    - A colon :
- An indented function body
2. Here's an example without an argument:
```python
>>> def hello_world():
...     print("Hello, World!")
...
>>> hello_world()
Hello, World!
>>>
```
3. If we want to define an argument, we will put the variable name we want it to have within the parentheses:
```python
>>> def print_name(name):
...     print(f"Name is {name}")
...
>>> print_name("Keith")
Name is Keith
```
4. Let's try to assign the value from print_name to a variable:
```python
>>> output = print_name("Keith")
Name is Keith
>>> output
>>>
```
5. Neither of these examples has a return value, but we will usually want to have a return value unless the function is our "main" function, or carries out a "side-effect" like printing. If we don't explicitly declare a return value, then the result will be None.

6. We can declare what we're returning from a function using the return keyword:
```python
>>> def add_two(num):
...     return num + 2
...
>>> result = add_two(2)
>>> result
4
```
## Working with Multiple Arguments
1. When we have a function that takes multiple arguments, we need to separate them using commas and give them unique names:
```python
>>> def add(num1, num2):
...     return num1 + num2
...
>>> result = add(1, 5)
>>> result
6
```
## Using Keyword Arguments
1. Every function call we've made up to this point has used what are known as positional arguments, but if we know the name of the arguments and not necessarily the positions we can call them all using keyword arguments like so:
```python
>>> def contact_card(name, age, car_model):
...     return f"{name} is {age} and drives a {car_model}"
...
>>> contact_card("Keith", 29, "Honda Civic")
'Keith is 29 and drives a Honda Civic'
>>> contact_card(age=29, car_model="Civic", name="Keith")
'Keith is 29 and drives a Civic'
>>> contact_card("Keith", car_model="Civic", age="29")
'Keith is 29 and drives a Civic'
>>> contact_card(age="29", "Keith", car_model="Civic")
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
```
2. When we're using position and keyword arguments, every argument after the first keyword argument must also be a keyword argument. It's sometimes useful to mix them, but often times we'll use either all positional or all keyword.

## Defining Default Arguments
1. Along with being able to use keyword arguments when we're calling a function, we're able to define default values for arguments to make them optional when the information is commonly known and the same. To do this, we use the assignment operator (=) when we're defining the argument:
```python
>>> def can_drive(age, driving_age=16):
...     return age >= driving_age
...
>>> can_drive(16)
True
>>> can_drive(16, driving_age=18)
False

```
2. Default arguments need to go at the end of the arguments list when defining the function, so that positional arguments can still be used to call the function.
