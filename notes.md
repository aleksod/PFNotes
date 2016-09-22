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
