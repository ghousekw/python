Introduction:
--
Python is an interpreted language, and code is evaluated line-by-line. Since each line can be evaluated by itself, the time between evaluating each line doesn't matter, and this allows us to have a REPL.

### What is a REPL?

* REPL stands for: Read, Evaluate, Print, Loop.

* Each line is read and evaluated. The return value is then printed to the screen, and then the process repeats.

To exit the REPL, we can either type **exit()** (the parentheses are important) or hit **Ctrl+d** on your keyboard.

### Creating Our First Python Script
Let's create our first script to write our obligatory "Hello, World!" program:

```
$ vim hello.py
```
From inside this file we can enter the lines of Python that we need. For the "Hello, World!" example we only need

```
print("Hello, World!")
```

There are a few different pays that we can run this file. The first is by passing it to the python3.7 CLI.
```
$ python3.7 hello.py
```
Hello, World!

## Setting a Shebang

Executable from anywhere (in our $PATH)
Executable without explicitly using the python3.7 CLI
Thankfully, we can set the process to interpret our scripts by setting a shebang at the top of the file:

hello.py
```
#!/usr/bin/env python3.7
print("Hello, World")
```
We're not quite done, because now we need to make the file executable using chmod:

```
$ chmod u+x hello.py
```

Run the script now by using ./hello.py and we'll see the same result. If we'd rather not have a file extension on our script we can now remove that since we've put a shebang in the file. Renaming it to get rid of the extension (mv hello.py hello) and running ./hello will still result in Python 3.7 executing the script.

Adding Scripts to Our $PATH
Now we need to make sure that we can put this in our $PATH. For this course, we'll be using a bin directory in our $HOME folder to store our custom scripts, but scripts can go into any directory that is in your $PATH.

Let's create a bin directory and move our script:
```
$ mkdir ~/bin
$ mv hello.py ~/bin/hello
```
Here's how we add this directory to the $PATH in our .bashrc (the .bashrc for this course already contains this):

```
$ export PATH=$PATH:$HOME/bin
```
Finally, let's run the hello script from our $PATH:

```
$ hello
Hello, World!
```