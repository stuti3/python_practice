# Basics of python

Last time, we wrote a "Hello World" program, that ran successfully. It was kind of like this:
```python
print("Hello World")
```
Before diving deeper, we must understand how Python does the work.
Let us assume that you have saved this code in a file named _hello.py_. *.py* indicates that the file is a Python file and hence, the editor runs the file in a **Python Interpreter**.

![Hello World Joke](https://i.pinimg.com/originals/49/78/3e/49783e18b9ac11c560362029ba1f3328.jpg)

Now that we know how Python does the work, let's dive into the basics that is familiar in every programming language we come across, at least most of them:

### Variables
A variable, as we know, is a memory allocation that holds some value. Generally, while defining a variable, we set the type of the variable, the name and the value. But in python, there is no need to specify type. 
Example: 
```python
a = "Hello World"
print(a)
```
Do note one thing: The amount of variables you use in any program is tricky. Variables are like snakey friends, you can't have too many but those you can't do without. Remember to always try to keep your program less cluttered.

In python as well, there are rules and guidelines for using and naming variables. Here are those rules:
* Variable names can contain only letters, numbers, and underscores.
They can start with a letter or an underscore, but not with a number.
For instance, you can call a variable message_1 but not 1_message.
* Spaces are not allowed in variable names, but underscores can be used
to separate words in variable names. For example, greeting_message works,
but greeting message will cause errors.
* Avoid using Python keywords and function names as variable names;
that is, do not use words that Python has reserved for a particular programmatic purpose, such as the word print. (See “Python Keywords
and Built-in Functions” on page 489.)
* Variable names should be short but descriptive. For example, name is
better than n, student_name is better than s_n, and name_length is better
than length_of_persons_name.
* Be careful when using the lowercase letter l and the uppercase letter O
because they could be confused with the numbers 1 and 0.

![Variable Joke](https://i.redd.it/4qjnyaegv7ly.png)

Here is a small exercise to help you practice variables in python:
```
Write a separate program to accomplish each of these exercises. Save
each program with a filename that follows standard Python conventions,
using lowercase letters and underscores, such as simple_message.py and
simple_messages.py.
2-1. Simple Message: Store a message in a variable, and then print that
message.
2-2. Simple Messages: Store a message in a variable, and print that message.
Then change the value of your variable to a new message, and print the new
message
```

### Strings

A string is a data type that is just a set of characters. In Python, we define Strings as follows:
```
'Why does khudkhushi in hindi mean suicide instead of masturbation?'
"Why does khudkhushi in hindi mean suicide instead of masturbation?"
```
Python offers flexibility too, with strings and apostrophe:
```
'My friends pay restaurant bills on a "de-tu-de" basis.'
"My friends pay restaurant bills on a 'de-tu-de' basis."
```
![String Joke](https://cdn-images-1.medium.com/max/1600/1*CtIdTEzKtQo-9Bc9ljArEA.png)

Just off topic yet so much topic:
![Python Joke](https://img.devrant.com/devrant/rant/r_1755638_zkSNA.jpg)
