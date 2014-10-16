Help Your Kids with Computer Coding
===================================

Examples, revisions, and extensions
to the DK book [Help Your Kids with Computer
Coding](http://www.amazon.com/Help-Your-Kids-Computer-Coding/dp/146541956X)
related to the Python
[`turtle`](https://docs.python.org/3.4/library/turtle.html#module-turtle)
and [`tkinter`](https://docs.python.org/3.4/library/tkinter.html) modules.

DK's book is one of the better ones but the Python examples use some bad
practices and can be confusing to follow: 

* No code documentation at all
* Unnecessary use of `from tkinter import *` (or any `*` at all)
* Unnecessary use of `from turtle import *`
* Failing to consolidate `import` statements at top
* Extensive use of globals even from within functions
* Poor use of structured data
* Absence of any traditional Object-Oriented introduction
* Unnecessary abbreviation and obfuscation of variable and function names
* Use of `\` for line continuation
* Failure to mention the [`ttk`](http://wiki.tcl.tk/14796) upgrades

If unchecked these could instill bad habits into new programmers taking
them at face value. This repo is to help parents and students make the
best of this otherwise good book and learn to avoid the bad parts.

To understand why these are bad practices we suggest the following official
Python documentation: 

* [PEP 8](http://legacy.python.org/dev/peps/pep-0008/)
* [Idioms and Anti-Idioms in Python](https://docs.python.org/3.4/howto/doanddont.html)
* [Google Python Style Guide](http://google-styleguide.googlecode.com/svn/trunk/pyguide.html)
* [Yahoo Python Coding Standards](http://lists.osafoundation.org/pipermail/dev/2003-March/000479.html)
* [CKAN Python Coding Standards](http://docs.ckan.org/en/latest/contributing/python.html)

Scratch v.s. Blockly
====================

It's worth noting as well that this book uses
[Scratch](http://scratch.mit.edu/), which is suffers from
the following inadequacies compared to
[Blockly](https://code.google.com/p/blockly/) as used by
[learn.code.org](http://learn.code.org):

* No functions at all ([Snap!](http://snap.berkeley.edu/) created to address)
* Not open source
* Requires 'Flash' instead of just JavaScript
* Cannot be used to output other code (Blockly outputs JavaScript, Python
  and more).

The book does provide some structure to the otherwise unstructured Scratch
web site. By following along in the book this could be used to provide the
same sort of progressive challenges that learn.code.org does but in an
arguably less effective way.

LICENSE
=======

While these examples fall under copyright with the book, fair use
allows us to expand and comment on them here. We assume you have already
purchased a copy of the book and are seeking clarification and what it
contains or want to expand on what you have learned in it. Any additional
contributions (not in the book) are public domain.
