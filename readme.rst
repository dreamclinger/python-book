Python Tutorial
====
https://github.com/michaelliao

Introduction to Python
====
Installing Python
Python interpreter
First Python Program
Use a text editor
Input and output

Python foundation
====
Data types and variables
String and encoding
Use list and tuple
Conditional and loop
Use dict and set

Function
====
Call functions
Defined Functions
Function parameters
Recursive function
Advanced Features
Sliced
Iteration
List of Formula
Builder
Functional Programming

Higher-order functions
====
Anonymous functions
Decorators
Partial function

Modules
====
Using the Module
Installation of third-party modules
Use __future__

Object-Oriented Programming
====
Classes and instances
Access restrictions
Inheritance and polymorphism
Gets the object information

Advanced Object-Oriented Programming
====
Use __slots__
Useproperty
Multiple inheritance
Custom class: custom-class.py
Use metaclass: meta-class.py

Errors, debugging and testing
====
Error Handling
Debugging
Unit Testing
Document test

IO Programming
====
Document literacy
Manipulating files and directories
Serialization

Processes and Threads
====
Multi-process
Multithreading
ThreadLocal
Process vs. thread
Distributed Process

Regex
====

Built common module
====
collections
base64
struct
hashlib
itertools
XML
HTMLParser

Commonly used third-party modules
====
PIL

Graphical interface
====

Network Programming
====
TCP / IP Introduction
TCP programming
UDP programming

E-mail
====
SMTP mail
POP3 receive mail

Access database
====
Use SQLite
Use MySQL
Use SQLAlchemy

Web Development
====
Introduction to the HTTP protocol
Introduction to HTML
WSGI interface
Using Web Framework
Using Templates

Coroutine
====
gevent

Combat
====
Day 1 - set up the development environment
Day 2 - write database module
Day 3 - write ORM
Day 4 - write Model
Day 5 - write Web Framework
Day 6 - Add a profile
Day 7 - write MVC
Day 8 - Construction of the front
Day 9 - write API
Day 10 - Register and login
Day 11 - Create a page written in the log
Day 12 - write log List
Day 13 - to enhance development efficiency
Day 14 - complete Web App
Day 15 - deploying Web App
Day 16 - write Mobile App

Final summary
====






Data Structure
====

Type
----
>>> x = 'abc'
>>> isinstance(x, str)
True

Dict
----
#因为dict的存储不是按照list的方式顺序排列
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key

#默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.itervalues()，如果要同时迭代key和value，可以用for k, v in d.iteritems()。
#当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
#那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断

from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代

Object Oriented Design
====

Custom class, e.g. __init__()
----
http://igorsobreira.com/2010/09/16/difference-between-one-underline-and-two-underlines-in-python.html



Structured Query Language
====


