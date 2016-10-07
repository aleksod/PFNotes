## 2016.09.16 Lecture

### Python
Numerics
* Integers
* Floats
* Complex
* Boolean (type bool)

Division in Python is special. 8/6 will give you 1, unless you mention decimals: 8.0/6. Alternatively, you can use float(8/6).  
* float(22/7) will give you 3.0  
* float(22)/7 will actually give you 3.14...  
* 8//6 just gives you 1.0 as it just slashes all the decimals.  
* To see if a number is even, do modulo 2 (% 2). 7%2 gives you 1, 8%2 gives you 0.  

Good programming etiquette tells us to write all variables in lower case with words connected by _ instead of spaces.

Significant whitespace  
 Traditional languages usually have this for if:  
  if (z>50)  
  {  
    print("sweet")  
  }  
  However, Python only needs indentation to know what is nested inside:  
  if z>50:  
    print 'a'  

Incrementing something is easy, can do += -= *= /=.  

_raw_input("prompt text")_ asks for input, always saves as string. Can surround raw_input command with int() or float().  

if:, else:, elif: for logical conditionals  
Can do 5 <= x < 10 in one line.

_not_ is a unary operator since only requires one operand. _and, or_ need two operands.  

Read about _continue_ on your own.  

_pass_ is a placeholder for nothing on the line in a loop due to significant whitespace.  

For ipython in particular, _whos_ shows dashboard with all variables of the current ipython session.  


## 2016.09.20 Lecture

Today we are going to look at 3 topics:
1. strings
2. for loops
3. lists  

String: sequence of characters  
Triple quotes allow '''strings
on
separate
lines
'''  

Can concatenate with '+' and repeat strings with '*'  

Methods don't change variables, but act on them. Ex: s.split() splits a sentence, for example, or anything you want. We can chain methods, just keep adding dot methods. Ex: s.replace('this', 'that ').strip()  

In the example above, 's' is a project and so is everything else in Python. Methods act on objects via dot notation.  

What is whitespace?
  Whitespace: spaces, tabs, line breaks, page breaks, etc.  

Reversing a string: s[::-1]  

Swapping variables: x, y = y, x  
Similarly, x, y = (3, 4).  

Functions and methods are also objects (everything is an object!).  

Whitespace in Python is 4 spaces by convention, but any number of spaces is OK (stick to 4!).  

Formatting:  '%s' is a format specifier:  
'hello %s' % 'Alexei'  
'hello %s %s' % ('Alexei', "Demchouk")  
Can also do 'hello, {name1} {name2}'.format(name1='abc', name2='def')  

### Lists
You can nest lists: [1,3, 'radf', ['tre', 5]]  

Lists are mutable, they can be changed with methods. Strings do not change with running methods on them. Ex: x.pop() will remove the last element from x, so x is different now.  

All lists and strings are ITERABLES.  

in - membership operator. Ex: 'bcd' in s => returns True if 'bcd' is found as an element in s.  

NoneType is has only one example: None

## 2016.09.22 Lecture

###Various numbering systems:
* base 2, starts with "0b", ex: 0b10 = 2, 0b1000 = 8
* base 8, starts with "0", ex: 010 = 8, 0100 = 64
* base 16, starts with "0x", ex: 0x10 = 16, 0x0f = 15  

###Tuples are immutable lists, basically.  
* t = (1, 2)
* t = 1, 2
* t = tuple([1, 2])
* t = (9,) # must have a comma after the number, otherwise is just a number  

Language-wise,  
* singleton
* double, duple
* triple
* quadruple
* 7-tuple, etc.  

###Dictionaries are unordered data structures. Keys are immutable, values can be mutable, unless they are tuples.  

dict.items - creates a list of key-value pairs
dict.iteritems - creates key-value pairs on demand, so not as memory intensive.  

Empty dictionaries are created by dict() or {}.  

###Sets - mutable unordered __unique__ element collection.  

Empty sets are created by set().  

## 2016.09.27 Lecture  

__import this__ is an interesting Easter egg in Python  

### Functions
Functions are used for
1. reusability
2. abstraction

We have dealt with functions before, such as __len(), enumerate(), range(), list(), str(), dict(), raw_input(), etc.__  

Methods are also functions that MUST be called from an object through dot notation.  

Functions may accept arguments (the stuff that goes into parenthesis).  

To define a function, use __def__. For example:  

def function_name():
  return 5  

If a string is created immedately after the function definition, then that string will be used as a help for that function (a.k.a. docstring), ex. s.f?  

def f(n):
  """This
  is
  a
  doctring"""
  return 8*n

Parameter is _n_ in def f(n). Argument is what you put in parenthesis to work with, ex. f(8).  

Default value can be defined like this:
  def f(n, m=2):
    return 2*n+m

If only one number is passed, m=2 will be used for m.  

It may be a good practice for all parameters to have default values.  

def f (n, m, x=1, y=2) - n and m are mandatory arguments to be passed, x and y are keyword arguments. So __f(3, 4, 2)__ is understood as n=3, m=4, x=2, with the default y=2. __f(3, 3, y=6)__ will be executed with y=6 and x=1.  

#### Variable Scope

Values outside of functions are GLOBAL and can be accessed anywhere, inside functions and outside. Values in functions are local and are not accessible outside of functions.  

### List Comprehension
Example:
  In [30]: [2*n for n in range(4)]
  Out[30]: [0, 2, 4, 6]  
  In [31]: '-'.join(s.upper() for s in ['hello', 'world'])
  Out[31]: 'HELLO-WORLD'  
  In [32]: [n for n in range(20) if n%3==0]
  Out[32]: [0, 3, 6, 9, 12, 15, 18]  

### Dictionary Comprehension  
Format:
  {k: v for (k, v) in [('a', 1), ('b', 2)]}
Example:
  In [33]: {k: k + ' dog' for k in ['a', 'b']}
  Out[33]: {'a': 'a dog', 'b': 'b dog'}

Instead of lists can use "generators" with (), e.g. it generates values on demand one by one and does not store the whole list in memory. Ex:  
  g = (n for n in range(8)) # is a generator
  [n for n in g] # will give you a list  

## 2016.09.29 Lecture  

### Lambda
Used for quick short functions, ex:
  f = lambda x,y: x+y
  In [108]: f(3,4)
  Out[108]: 7

### Map
In [111]: map(lambda x:3*x, [1,2,3,4])
Out[111]: [3, 6, 9, 12]

### Filter
In [112]: filter(lambda x: x%2==1, [1,2,3,4,5])
Out[112]: [1, 3, 5]

### Reduce
In [115]: reduce(lambda x, y: x+y, [2,3,4])
Out[115]: 9
In [116]: reduce(lambda x,y: 10*x+y, [1,2,3,4])
Out[116]: 1234

### Magic Methods
Every object have a special methods:
  x.__ [type tab after two _]  
Functions also have magic methods, just do the same: type in function name and then a dot and a double _.  

### Sort and Lambda
In [125]: x
Out[125]: ['asdf', 'qwer', 'zxcv']
In [126]: x.sort(key=lambda s:s[2]) # sorts by the third character in the string
In [127]: x
Out[127]: ['zxcv', 'asdf', 'qwer']

### Top-Down Programming
Placeholds Driven Development, ex:  
def create_report():
    pass

In [129]: f = open('test.txt')
In [130]: f.close()
In [131]: f
Out[131]: <closed file 'test.txt', mode 'r' at 0x105c05d20>
In [132]: f = open('test.txt', 'r') # opens in read only mode
In [133]: f = open('test.txt', 'w') # opens in write mode

In [134]: f.write("""This is a test\nThis is only a test\nEnd test""")

### Importing Detour

Module:
 * single Python file (.py)

Package:
 * directory
 * multiple modules

Script:
 * single file
 * generally executed from the command line
 * It is a good idea to dedicate a portion of scripts for main block through magic function __name__ to only be executed when the script is run, but not when it is imported:
  if __name__ = "__main__":
    your code goes here

Can import like this:
  import text_file_processing
Or:
  import text_file_processing as tfp
Or:
  from text_file_processing import name_of_the_module

So tfp can be used instead of typing text_file_processing.  

Import things like "random" and "math":
  import random
  import random

Only in ipython if you make changes in .py file, you need to reload it with __reload__ command. Otherwise it won't show up in the environment.  

### Debugging
Can debug using
 1. print statements, a.k.a. tracing
 2. remove lines of code one by one until it works via hashes "#"

## 2016.10.04 Lecture  
### Object Oriented Programming (OOP)
* classes, objects (instances)
* attributes, methods
* constructor
* "self"
* magic methods
* inheritance  

#### Objects and Classes
Example: fake object "Student" might have the following attributes:
* name
* id
And methods
* submitHW (function)

A class is a type of an object. Ex:  
type(5) ==> int  

#### Design Principles
* Encapsulation - hiding the inner workings, only exposing the interface of objects
* Inheritance - can create new classes by copying and altering old classes
* Polymorphism  

Create a class:
class Example_Class():
  pass  

To instantiate is to create an instance of a class, ex:  
c = Example_Class()  

Command __isinstance()__ tests if something is an instance of which class, ex:  
In [145]: isinstance(8, int)
Out[145]: True  

#### Constructors  
A constructor is a method that is called whenever you create or instantiate an object from a class, ex:  
In [146]: class OurClass():  
   .....:     def __init__(self):  
   .....:         self.name = "Intro to Python"  
   .....:         

In [147]: x = OurClass()  
In [148]: x.name  
Out[148]: 'Intro to Python'  
In [149]: x2 = OurClass()  
In [150]: x2.name = "Test"  
In [151]: x2.name  
Out[151]: 'Test'    

"self" is a reference to the current object.  
Essentially __init__ is a magic function.  

If you have a doctring (""" """), calling it up with a magic function __doc__ will work.  

def __str__(self):  
  return "This class is named %s" % self.name  
This HAS to return a string.

def __init__(self, name, location, size, questions_asked=None):  
  self.name = name  
  self.location = location  
  self.size = size  
  if questions_asked == None:  
      self.questions_asked = list()  
  else:  
      self.questions_asked = questions_asked  

Whenever you create a method inside a class, the very first parameter MUST be "self" so the method knows it is part of that class.  

def add_questions_asked(self, question):  
  self.questions_asked.append(question)  

OurClass.add_questions_asked(x, "what is a dict")  
That will work because of that "self" reference in the class definition above.  

add_questions_asked is a method because it is a function within the class OurClass().  

Static/class attribute can be simply defined by just putting something like this after the first line of class definition outside of the constructor __init__:  
example_static_attribute = 5  

If it is a mutable attribute and you change it, then it will change in EVERY object instantiated from that class:  

#### Inheritance  
Example:  

class GalvanizeClass(OurClass):  

  def __init__(self, name):  
    self.name = name  
    self.location = "Galvanize SF"  

Inherits everything from OurClass so all other methods still would work, but location has been customized.  

In ipython type in "edit function_name" will summon a text editor with that function to edit.  

## 2016.10.06 Lecture  
"Dunder str" is what's referring to ____str____ method

### Design Approaches
One approach to designing a solution:
1. design outline
2. coding
3. testing
4. debugging

When creating a class with a method in it that starts with an underscore "_", this method is only visible to the internal workings of the class and cannot be called outside of it via the dot notation.  

When creating a method inside another method within a class, one does not have to include "self" in attributes since it is a helper function and is local.  

### Collections
Type in "import collections"  
c = collection.Counter()
from collections import defaultdict  
d2 = defaultdict(float) # initializes a dictionary where values are float, in this case  
import re # imports regular expressions functionality
