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
