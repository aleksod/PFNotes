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
