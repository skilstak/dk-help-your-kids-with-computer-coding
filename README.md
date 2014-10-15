Help Your Kids with Computer Coding
===================================

Examples, revisions, and extensions to the DK book 'Help Your Kids with
Computer Coding'.

DK's book is one of the better ones but the Python examples use some bad
practices and can be confusing to follow &mdash; especially the `tkinter`
Bubble Blaster project:

* Unnecessary use of `from tkinter import *` (or any `*` at all)
* Unnecessary use of `from turtle import *`
* Failing to consolidate `import` statements at top
* Extensive use of globals even from within functions
* Poor use of structured data
* Absence of any traditional Object-Oriented introduction
* Unnecessary abbreviation and obfuscation of variable and function names

If unchecked these could instill bad habits into new programmers taking
them at face value. This repo is to help parents and students make the
best of this otherwise good book and learn to avoid the bad parts.

To understand why these are bad practices we suggest the following official
Python documentation: 

* [PEP 8](http://legacy.python.org/dev/peps/pep-0008/)
* [Idioms and Anti-Idioms in
  Python](https://docs.python.org/3.4/howto/doanddont.html)

LICENSE
=======

While these examples fall under copyright with the book, fair use
allows us to expand and comment on them here. We assume you have already
purchased a copy of the book and are seeking clarification or what it
contains or want to expand on what you have learned in it.
