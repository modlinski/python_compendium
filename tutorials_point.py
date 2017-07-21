#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python has five standard data types"""

# print dir(str)
# print dir(list)
# print dir(int)
# print dir(tuple)
# print dir(dict)

"""1. Numbers"""

print '='*15
print "1. Numbers"
print '='*15

var1 = 5                # int (signed integers)
var2 = 3.14j            # complex (complex numbers)
var3 = 32.3E18          # float (floating point real values)
var4 = -0x19323L        # long (long integers)

# del var1              

print var1, var2, var3, var4, float(var1), int(var3)

x = 11.0
y = 2.0

print 11/2           # integer by integer gives integer!
print x + y          # sum of x and y
print x - y          # difference of x and y
print x / y          # quotient of x and y
print x // y         # (floored) quotient of x and y
print x % y          # remainder of x / y
print abs(x)         # absolute value or magnitude of x
print x ** y         # x to the power y

"""2. Strings"""

print '='*15
print "2. Strings"
print '='*15

strng = 'Hello world!'

print strng              # Prints complete string
print strng[0]           # Prints first character of the string
print strng[2:5]         # Prints characters starting from 3rd to 5th
print strng[2:]          # Prints string starting from 3rd character
print strng * 2          # Prints string two times
print strng + "TEST"     # Prints concatenated string

print strng.capitalize()           # Capitalizes first letter of string
print strng.swapcase()             # Inverts case for all letters in string
print strng.title()                # Returns "titlecased" version of string
print strng.upper()                # Converts lowercase letters in string to uppercase.
print strng.lower()                # Converts all uppercase letters in string to lowercase.
print "this".isalpha()             # Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.
print "-".join(("a", "b", "c"))    # Merges (concatenates) the string representations of elements in sequence seq into a string, with separator string.
print strng.split()                # Splits string according to delimiter str (space if not provided) and returns list of substrings; split into at most num substrings if given.
print len(strng)

"""3. Lists"""

print '='*15
print "3. Lists"
print '='*15

lst = ['abcd', 786 , 2.23, 'john', 70.2]
tinylist = [123, 'john']

print lst                # Prints complete list
print lst[0]             # Prints first element of the list
print lst[1:3]           # Prints elements starting from 2nd till 3rd 
print lst[2:]            # Prints elements starting from 3rd element
print tinylist * 2       # Prints list two times
print lst + tinylist     # Prints concatenated lists
del lst[0]
print 70.2 in lst
print len(lst)                     # Gives the total length of the list
print cmp([1 , 1 , 1], [2, 2, 2])  # Compares elements of both lists
print max([3,3,3,90])              # Returns item from the list with max value
print min([-5,2,3,4])              # Returns item from the list with min value
print list((1,2,3,'xyx'))          # Converts a tuple into list

lst.append('stringi')   # Appends object obj to list
lst.extend('stringi')   # Appends the contents of seq to list
lst.count('i')          # Returns count of how many times obj occurs in list
lst.index('i')          # Returns the lowest index in list that obj appears
lst.insert(0, [2,3])    # Inserts object obj into list at offset index
lst.pop()               # Removes and returns last object or obj from list
lst.remove('stringi')   # Removes object obj from list
lst.reverse()           # Reverses objects of list in place
lst.sort()              # Sorts objects of list, use compare func if given

"""4. Tuples - are similar to the list. The main differences between lists and 
tuples are: Lists are enclosed in brackets [] and their elements and size can 
be changed, while tuples are enclosed in parentheses () and cannot be updated.
Tuples can be thought of as read-only lists."""

print '='*15
print "4. Tuples"
print '='*15

tpl = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

tpl_2 = "P", "W", "R", "rzygi"   # Any set of multiple objects, comma-separated, written without identifying symbols, i.e., brackets for lists, default to tuples
singel_tuple = (1, )             # To write a tuple containing a single value you have to include a comma, even though there is only one value

print tpl                        # Prints complete list
print tpl[0]                     # Prints first element of the list
print tpl[1:3]                   # Prints elements starting from 2nd till 3rd 
print tpl[2:]                    # Prints elements starting from 3rd element
print tinytuple * 2              # Prints list two times
print tpl + tinytuple            # Prints concatenated lists
print len((1, 2, 3))           
print 3 in (1, 2, 3)           
print min((2, 4, 6, 8, 10))
print max((2, 4, 6, 8, 10))

"""5. Dictionaries. Dictionary values have no restrictions. However, same is not
true for the keys. More than one entry per key not allowed (which means no 
duplicate key is allowed) and keys must be immutable (which means you can use strings,
numbers or tuples as dictionary keys but something like ['key'] is not allowed)."""

print '='*15
print "5. Dictionaries"
print '='*15

dct = {}
dct['one'] = "This is one"
dct[2]     = "This is two"
dct[2]     = "This is new two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
slownik = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print dct['one']          # Prints value for 'one' key
print dct[2]              # Prints value for 2 key
print tinydict            # Prints complete dictionary
print tinydict.keys()     # Prints all the keys
print tinydict.values()   # Prints all the values
dct.copy()                # Returns a shallow copy of dictionary dict
dct.clear()               # remove all entries in dict
del slownik['Name']       # remove entry with key 'Name'
slownik['Age'] = 8        # update existing entry
slownik['High'] = '1.8'   # Add new entry
print dct
print len(slownik)        # Gives the total length of the dictionary
print str(slownik)        # Produces a printable string representation of a dict
print type(slownik)       # Returns the type of the passed variable

seq = ('name', 'age', 'sex')
dct_2 = dict.fromkeys(seq)
dct_2 = dict.fromkeys(seq, 10)    #  Create a new dictionary with keys from seq and values set to value.
print slownik.get('Age')          # The method get() returns a value for the given key. If key is not available then returns default value None.
print slownik.has_key('Class')    # Returns true if key in dictionary dict, false otherwise
print slownik.items()             # Returns a list of dict's (key, value) tuple pairs
print slownik.keys()              # Returns list of dictionary dict's keys
print slownik.values()            # Returns list of dictionary dict's values
slownik.update(tinydict)
print slownik

"""Sets. A set contains an unordered collection of unique and immutable objects.
The set data type is, as the name implies, a Python implementation of the sets
as they are known from mathematics. This explains, why sets unlike lists or tuples
can't have multiple occurrences of the same element. Though sets can't contain
mutable objects, sets are mutable. Frozensets are like sets except that they
cannot be changed."""

print '='*15
print "Sets."
print '='*15

print set("It's new for me")           # Converts something to a set.

cities = set(["Frankfurt", "Basel","Freiburg"])
cities.add("Strasbourg")
print cities

print frozenset("It's new for me")     # Converts something to a frozen set.
cities = frozenset(["Frankfurt", "Basel","Freiburg"])

"""Data Type Conversion"""

print '='*15
print "Data Type Conversion"
print '='*15

print int('6')                         # Converts x to an integer. base specifies the base if x is a string.
print long('5500'[3])                  # Converts x to a long integer. base specifies the base if x is a string.
print float(7)                         # Converts x to a floating-point number.
print complex('150000'[1])             # Creates a complex number.
print str(123456789)                   # Converts object x to a string representation.
print repr(98765)                      # Converts object x to an expression string.
print eval('1 + 4')                    # Interprets a string as code and evaluates it.
print tuple([1, 2, 3])                 # Converts s to a tuple.
print list((2, 4, 6))                  # Converts s to a list.
print dict([(2, 4),(3, 9),(4, 16)])    # Creates a dictionary. d must be a sequence of (key,value) tuples.
print divmod(17, 5)                    # the pair (x // y, x % y)

"""Python language supports the following types of operators.

- Arithmetic Operators (+, -, /, //, **)
- Comparison (Relational) Operators (==, !=, <, >, <=, >=)
- Assignment Operators (=, +=, -=, *=, /=, %=, **=, //=)
- Logical Operators (and, or, not)
- Bitwise Operators (&, |, ^, ~, >>, <<)
- Membership Operators (not in, in)
- Identity Operators (is, is not)

Let us have a look on all operators one by one."""

"""Loops."""

print '='*15
print "Loops."
print '='*15

# 1 Example (for, break)

for letter in 'Python':
   if letter == 'h':
      break
   print 'Current Letter :', letter

# 2 Example (while, break)

var = 10
while var > 0:              
   print 'Current variable value :', var
   var = var -1
   if var == 5:
      break
print "Good bye!"

# 3 Example (for, continue)

for letter in 'Python':
   if letter == 'h':
      continue
   print 'Current Letter :', letter

# 4 Example (while, continue)

var = 10
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print 'Current variable value :', var
print "Good bye!"

# 5 Example (for, pass)

for letter in 'Python': 
   if letter == 'h':
      pass
      print 'This is pass block'
   print 'Current Letter :', letter

print "Good bye!"

# 6 Example (nested loops)

i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " is prime"
   i = i + 1

print "Good bye!"

"""Mathematical Functions"""

print '='*15
print "Mathematical Functions"
print '='*15

import math

print math.ceil(70.5)      # The ceiling of x: the smallest integer not less than x
print math.exp(3)          # The exponential of x: e^x
print math.floor(-45.17)   # The floor of x: the largest integer not greater than x
print math.fabs(-45.17)    # The absolute value of x
print math.log(100.12)     # The natural logarithm of x, for x>0
print math.log10(100.12)   # The base-10 logarithm of x for x>0
print math.modf(10.05)     # The fractional and integer parts of x in a two-item tuple. Both parts have the same sign as x. The integer part is returned as a float.
print math.sqrt(100)       # The square root of x for x > 0

print round(80.23456, 2)   # x rounded to n digits from the decimal point. Python rounds away from zero as a tie-breaker: round(0.5) is 1.0 and round(-0.5) is -1.0.
print pow(100, 2)          # The value of x**y.
print max(54, 99, 1000)    # The largest of its arguments: the value closest to positive infinity
print min(-100, 40, 8)     # The smallest of its arguments: the value closest to negative infinity
print cmp(80, 100)         # -1 if x < y, 0 if x == y, or 1 if x > y

"""Trigonometric Functions"""

"""Random Number Functions"""

print '='*15
print "Random Number Functions"
print '='*15

import random

print random.choice('A String')       # A random item from a list, tuple, or string.
print random.randrange(100, 1000, 5)  # A randomly selected element from range(start, stop, step)
print random.random()                 # A random float r, such that 0 is less than or equal to r and r is less than 1
print random.shuffle([20, 16, 10, 5]) # Randomizes the items of a list in place. Returns None.
print random.uniform(5, 10)           # A random float r, such that x is less than or equal to r and r is less than y

"""Date and time"""

"""Functions"""

"""Modules"""

"""Files I/O"""

"""Exceptions"""
