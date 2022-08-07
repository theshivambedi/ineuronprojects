
'''
  question 1

 * is an expression.It is an expression as we can multiply with it
  "hello" is a string value
  -87.8 is a floating point value
  - is an expression
  / is an expression
  + is an expression
  6 is an integer value '''

'''  question 2 diff between string and variable

  answer 2: String is a sequence of characters which we store in "" or '' in python
 variable is like a placeholder or containers in which is used to store data in programming language. It's a named location to our data.'''

"""question 3: 3 different data types

#Boolean which tells us true false, string which is sequence of character in single or double quotes. Numeric data types such as 
 float, integer"""

"""question 4: what is an expression made up of, what do all expression do?
Expressions are made up of operators and operands whom purpose to produce some value. Expressions in simple language are made up of
values whom we call operands and operators such as arithmetic operators who do mathematical operations such as add, subtract etc.
other type of operatos are assignment operators, logical operators etc. 

All expression produce some value. They calculate according to the operatos used and gave us the final result. 
"""

'''ques 5:

The very first difference is expression leads to some result, that is it evaluates to some value. where as statement executes something. 
We can assign expression to some variable but we can't assign statement to some variable. 
like we can't assign print statement to some variable or loops, functions, classes etc. 

expression example: 3+4 or a = 8+9 or 2==2
statement = for i in a: or print(a) or a = 2
'''

"""question 6

after running the code, bacon variable contains 22 only and not 23. Reason being, += is the right assignment operator and not +"""
bacon = 22
bacon + 1
print("bacon is: ", bacon)

# QUESTION 7

a = 'spam' + 'spamspam'
b = 'spam'*3
print(a)
print(b)

'''question 8
The reason eggs is a valid variable and 100 is invalid because there are certain rules to declare name for variables. 
one of them is that a vraiable name can't start from number, it has to be start from alphabet. We can use alphanumeric as variable
name but the starting should always be an alphabet'''

"""question 9  
The three functions can be int() for integer, float() for floating point integer and str() for string version"""

a = 6
print(int(a))
print(float(a))
print(str(a))

"""question 10 

The reason we are getting an error is because we can't concatenate string with other data types. In cases of string, we can 
 do string concatenation that is adding string with string to make it a single string. the right way would be, """

a10 = 'I have eaten ' + '99' + ' burritos.'
print(a10)
