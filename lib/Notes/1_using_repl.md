Introduction to Python Development 


CHAPTER 3.1
Using the REPL (Read, Evaluate, Print, Loop)


Python is an interpreted language, and code is evaluated line-by-line. Since each line can be evaluated by itself, the time between evaluating each line doesn't matter, and this allows us to have a REPL.

Documentation
Python Interpreter (https://docs.python.org/3/tutorial/interpreter.html)

What is a REPL?
REPL stands for: Read, Evaluate, Print, Loop

Each line is read and evaluated. The return value is then printed to the screen, and then the process repeats.

Python ships with a REPL, accessible by running python3.7 from a terminal.

$ python3.7
Python 3.7.2 (default, Jan 15 2019, 19:31:18)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-36)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
The >>> indicates a line to type in, like a command prompt for Python. Later on we'll see a ..., which means that we are currently sitting in a scoped area. The only way out is to enter a blank line (no spaces) before the interpreter will evaluate the entire code block.

The simplest use of this would be to do some math:

>>> 1 + 1
2
>>>
2 is the return value of the expression and it is then printed to the screen. If something doesn't have a return value, then nothing will be printed to the screen and we'll just land back at a >>> prompt. We'll cover this later, but an example would be None:

>>> None
>>>
To exit the REPL, we can either type exit() (the parentheses are important) or hit Ctrl+d on your keyboard.
