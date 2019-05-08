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

Strings can be used in many ways. Here are some of them:

#### Changing cases with methods in a string

Let us try one thing. Open a file, name it *name.py* and type this in it:
```
name = "bebe rexha"
print(name.title())
```
Save this file and run it. You will get the following output:
```
Bebe Rexha
```
In this example, the lowercase string "bebe rexha" is stored in the variable name. The method title() appears after the variable in the print() statement. A method is an action that Python can perform on a piece of data. The
dot (.) after name in name.title() tells Python to make the title() method
act on the variable name. Every method is followed by a set of parentheses,
because methods often need additional information to do their work.
That information is provided inside the parentheses. The title() function
doesn’t need any additional information, so its parentheses are empty.
title() displays each word in titlecase, where each word begins with a
capital letter. This is useful because you’ll often want to think of a name as a
piece of information. For example, you might want your program to recognize the input values Bebe, BEBE, and bebe as the same name, and display all of
them as Bebe.

There are other useful string methods in python that deal with cases. For example:
```
name = "bebe rexha"
print(name.upper())
print(name.lower())
```
This will give this output:
```
BEBE REXHA
bebe rexha
```

#### Combining or concatenating strings
There are times when we need to concatenate/combine strings. In python, it is very easy. For example:
```
first_name = "Bebe"
second_name = "Rexha"
full_name = first_name + " " + second_name
print(full_name)
```
The output to this code will be:
```
Bebe Rexha
```
So, as we can see, Python uses **+** to concatenate strings. The method of combining strings is called *concatenation*. 

Concatenation is useful, for instance, we can make full messages for it. For example:
```
first_name = "Bebe"
second_name = "Rexha"
full_name = first_name + " " + second_name
message = "Hey " + full_name.title() + "!"
print(message)
```
This will print:
```
Hey Bebe Rexha!
```
Note that we used title() so that the name is formatted appropriately. But just to see if anything happens, use the same code without the title() method.

#### Adding Whitespace to Strings with tabs or newlines
In programming, whitespace refers to any nonprinting character, such as
spaces, tabs, and end-of-line symbols. You can use whitespace to organize
your output so it’s easier for users to read.

To add a tab to your text, use the character combination \t:
```
print("Python")
print("\tPython")
```
which will print:
```
Python
  Python
```
Similarly, for newline, we use \n.

#### Stripping whitespace

Extra whitespace can be confusing in your programs. To programmers
'python' and 'python ' look pretty much the same. But to a program, they
are two different strings. Python detects the extra space in 'python ' and
considers it significant unless you tell it otherwise.
It’s important to think about whitespace, because often you’ll want to
compare two strings to determine whether they are the same. For example,
one important instance might involve checking people’s usernames when
they log in to a website. Extra whitespace can be confusing in much simpler
situations as well. Fortunately, Python makes it easy to eliminate extraneous
whitespace from data that people enter.
Python can look for extra whitespace on the right and left sides of a
string. To ensure that no whitespace exists at the right end of a string, use
the rstrip() method.
```
fav = 'Me '
print(fav)
print(fav.rstrip())
```
The output will be:
```
'Me '
'Me'
```
You can also strip whitespace from the left side of a string using the
lstrip() method or strip whitespace from both sides at once using strip():
```
fav = ' Me '
print(fav)
print(fav.rstrip())
print(fav.lstrip())
print(fav.strip())
```
This will output:
```
' Me '
' Me'
'Me '
'Me'
```

![Python Joke](https://i.pinimg.com/originals/11/b4/20/11b420fbf1595be3056ad6355277933c.jpg)

#### Avoiding Syntax Errors with Strings
One kind of error that you might see with some regularity is a syntax error.
A syntax error occurs when Python doesn’t recognize a section of your program as valid Python code. For example, if you use an apostrophe within
single quotes, you’ll produce an error. This happens because Python interprets everything between the first single quote and the apostrophe as a
string. It then tries to interpret the rest of the text as Python code, which
causes errors.

Here’s how to use single and double quotes correctly.
Here’s how to use single and double quotes correctly. Save this program
as apostrophe.py and then run it:
```
message = "One of Python's strengths is its diverse community."
print(message)
```
The apostrophe appears inside a set of double quotes, so the Python
interpreter has no trouble reading the string correctly:
```
One of Python's strengths is its diverse community.
```
However, if you use single quotes, Python can’t identify where the string
should end:
```
message = 'One of Python's strengths is its diverse community.'
print(message)
```
You’ll see the following output:
```
File "apostrophe.py", line 1
 message = 'One of Python's strengths is its diverse community.'
 ^u
SyntaxError: invalid syntax 
```
In the output you can see that the error occurs at u right after the
second single quote. This syntax error indicates that the interpreter doesn’t
recognize something in the code as valid Python code. Errors can come
from a variety of sources, and I’ll point out some common ones as they arise.
You might see syntax errors often as you learn to write proper Python code.
Syntax errors are also the least specific kind of error, so they can be difficult
and frustrating to identify and correct. 

**Your editor’s syntax highlighting feature should help you spot some syntax errors
quickly as you write your programs. If you see Python code highlighted as if it’s
English or English highlighted as if it’s Python code, you probably have a mismatched quotation mark somewhere in your file.**

```
Try It Yourself
Save each of the following exercises as a separate file with a name like
name_cases.py. If you get stuck, take a break or see the suggestions in
Appendix C.
2-3. Personal Message: Store a person’s name in a variable, and print a message to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?”
2-4. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.
2-5. Famous Quote: Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks:
Albert Einstein once said, “A person who never made a
mistake never tried anything new.”
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s name in a variable called famous_person. Then compose your message
and store it in a new variable called message. Print your message.
2-7. Stripping Names: Store a person’s name, and include some whitespace
characters at the beginning and end of the name. Make sure you use each
character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip().
```
