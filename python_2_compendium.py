# !/usr/bin/env python
# -*- coding: utf-8 -*-

# VARIABLE AND DATA TYPES
#
# Variable types are determined by the value stored within the variable. There are three main categories of variable
# types in Python (and most of other programming language). They are listed below, ordered by increasing complexity.
#
# 1. Primitive Variables - they are capable of storing a single value. In Python there are four primitive variable
# types, which are listed below:
#     - integer,
#     - float,
#     - string,
#     - boolean.
# 2. Compound Variables
# 3. Complex Variables
#
# Types are categories for things within Python with which Python will work. Types are:
#
#     - integer - whole number from negative infinity to infinity: -1, 0, 1,
#     - float - short for 'floating point number' any rational number, usually used with decimals: -1.5, 0.0, 1.5,
#     - string - set of letters, numbers, or other characters: 'word', '123',
#     - tuple - list with a fixed number of elements: (1, 2, 3,),
#     - list - list without a fixed number of elements: [1, 2, 3],
#     - dictionary - type with multiple elements, in which values are addressed by keys: {1: 'a','b': 2,3: 3}.
#
# The following types are immutable objects:
#
#     - numeric types (int, float, complex),
#     - string,
#     - tuple,
#     - frozen set,
#     - bytes.
#
# The following objects are mutable objects:
#
#     - list,
#     - dict,
#     - set,
#     - byte array.
#
#
# CODE INTROSPECTION
#
# print type(int)  # return type of an object
# print id(int)  # return the “identity” of an object that is unique and constant for this object during its lifetime
# print dir(int)  # return a list of valid attributes for that object
# print callable(int)  # return True if the object argument appears callable, False if not
# print getattr(int, 'real')  # return the value of the named attribute
# print hasattr(int, 'real')  # return True if the string is the name of one of the object’s attributes
# print help()  # invoke the built-in help system - this function is intended for interactive use
#
# example - filter callable methods of object:
#
# def callable_methods(obj):
#     attributes = dir(obj)
#     for attr in attributes:
#         if callable(getattr(obj, str(attr))):
#             print attr
#
# callable_methods(list)
#
#
# COMPARATORS AND BOOLEANS
#
# Anything in parentheses () is evaluated as its own unit.
# 'not' is evaluated first
# 'and' is evaluated next
# 'or' is evaluated last
#
# True and True is True
# True and False is False
# False and False is False
# True or True is True
# True or False is True
# False or False is False
# Not True is False
# Not False is True
#
# bool_1 = 3 < 5
# bool_2 = 5 < 4
# bool_3 = 5 == 5
# bool_4 = 5 != 2.5 * 2
# bool_5 = 5 >= 5
# bool_6 = (True or 7 > 6) and (not 6 ** 2 != 36) or (5 == 'Alpha')
#
# print bool_1, bool_2, bool_3, bool_4, bool_5, bool_6
#
#
# NUMBERS
#
# var1 = 5  # int (signed integers)
# var2 = 3.23E-3  # float (floating point real values)
# var3 = 3.14j  # complex (complex numbers)
# var4 = -0x19323L  # long (long integers)
#
# print var1, var2, var3, var4, float(var1), int(var2)
#
# print 5.0 + 2  # sum
# print 5.0 - 2  # difference
# print 5.0 * 2  # product
# print 5.0 / 2  # quotient
# print 5/2  # quotient - integer by integer gives integer
# print 5.0 // 2.0  # floored quotient
# print 5.0 % 2  # remainder
# print abs(5.5)  # absolute value of x
# print 5.0 ** 2
#
#
# STRINGS
#
# print 'quintessential'[0]  # first character
# print 'quintessential'[2:5]  # characters from 3rd to 5th
# print 'quintessential'[2:]  # characters from 3rd
# print 'hello' + ' world'  # concatenated string
# print 'hello ' * 2
#
# print 'surreptitious'.upper()  # converts lowercase characters to uppercase
# print 'surreptitious'.lower()  # converts uppercase characters to lowercase
# print 'surreptitious'.capitalize()  # capitalizes first letter
# print 'Surreptitious'.swapcase()  # inverts case for all letters
# print 'hello world'.title()  # returns 'titlecased' version of string
# print 'luminescence'.isalpha()  # returns true if string contains at least 1 character and all characters are letters
# print '-'.join(['a', 'b', 'c'])  # merges the strings, with defined string separator
# print 'a-b-c'.split('-')  # splits strings according to delimiter string
#
#
# LISTS
#
# print [0, 1, 2, 3, 4, 5, 6, 7][0:7:2]  # string[first:last:+step], '+' starts from the beginning
# print [0, 1, 2, 3, 4, 5, 6, 7][7:0:-2]  # string[first:last:-step], '-' starts from the end
# print [0, 1, 2, 3, 4, 5, 6, 7][1:5]  # string[first:last] returns elements indexed from 1 do last-1
# print [0, 1, 2, 3, 4, 5, 6, 7][0]  # first element
# print [0, 1, 2, 3, 4, 5, 6, 7][5:]  # returns substring containing elements indexed from 5 to the end
# print [0, 1, 2, 3, 4, 5, 6, 7][:5]  # returns substring containing elements indexed from beginning to 5
# print [0, 1, 2, 3] + [4, 5, 6, 7]  # concatenated lists
# print [0, 1, 2, 3] * 2
#
# example_list = ['a', 'b', 'c', 0, 1, 2]
#
# example_list.append('aurora')  # appends object to the list - returns None
# example_list.extend('aurora')  # appends the contents of sequence to the list - returns None
# example_list.insert(3, 'new')  # inserts object to the list at defined index - returns None
# example_list.remove('c')  # removes object from list - returns None
# example_list.reverse()  # reverses objects of list - returns None
# example_list.sort()  # sorts objects of list - returns None
#
# print example_list
#
# print example_list.count(1)  # number of occurrence of object
# print example_list.index('a')  # index of occurrence of object, the lowest
# print example_list.pop()  # removes and returns the last object from the list
#
# a, b, c, d, e, f = example_list
# print a, b, c, d, e, f
#
#
# TUPLES
#
# example_tuple = 'a', 'b', 'c', 0, 1, 2  # brackets are not to required for tuples
# single_tuple = (1, )  # one element tuple requires comma at the end - if comma is omitted the type of object is the
# same like type of element inside brackets
#
# print (0, 1, 2, 3)[0]  # first element
# print (0, 1, 2, 3)[1:3]  # elements from 2nd to 3rd
# print (0, 1, 2, 3)[2:]  # elements from 3rd element
# print (0, 1, 2, 3) + (4, 5, 6, 7)  # concatenated lists
# print (0, 1, 2, 3) * 2
#
#
# DICTS
#
# Dictionaries values - no restrictions.
# Dictionaries keys - must be unique; must be immutable (e.q. list are not allowed)
#
# example_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
# dict_to_append = {6: 'six', 7: 'seven'}
#
# example_dict.clear()  # remove all entries in dict - returns None
# example_dict.update(dict_to_append)  # appends the contents of given dict to the original dict - returns None
#
# print example_dict
#
# print example_dict[1]  # value for key: 1, if key is not available returns Exception
# print example_dict.keys()  # all keys
# print example_dict.values()  # all values
# print example_dict.items()  # real list of dict's (key, value) tuple pairs
# print example_dict.iteritems()  # generator 'creating' one item at a time every time next() is called on it
#     - items() probably takes more memory and time initially but accessing each element is fast
#     - iteritems() probably takes less space and time initially, but a bit more time in generating each element.
# print example_dict.copy()  # shallow copy of a dict
# print example_dict.get(1)  # returns a value for the given key, if key is not available returns None
# print example_dict.has_key(1)  # true if key in dict
#
# keys_tuple = ('key_1', 'key_2', 'key_3')
#
# print dict.fromkeys(keys_tuple)
# print dict.fromkeys(keys_tuple, 'value_for_all')
#
#
# SETS
#
# Contains an unordered collection of unique and immutable objects. Sets are mutable and frozensets immutable.
#
# print {'ineffable', 'ineffable', 'aquiver', 'nefarious'}  # returns a set of elements
# print set(['ineffable', 'ineffable', 'aquiver', 'nefarious'])  # returns a set of elements
# print set('ineffable')  # returns a set of elements
# print(frozenset('sonorous'))  # # returns a frozenset of elements
#
# list_to_convert = ['A', 'B', 'C', 'D', 'A']
# set_from_list = set(list_to_convert)
# set_from_list.add('E')
# set_from_list.remove('D')
# set_from_list.clear()
#
# print set_from_list
#
# set_1 = {1, 2, 3, 4, 5, 6}
# set_2 = {3, 4, 5, 6, 7, 8}
# set_3 = {5, 6, 7, 8, 9, 0}
# set_4 = {1, 2, 3}
#
# print set_1.difference(set_2)
# print set_1.difference(set_2).difference(set_3)
#
# print set_4.issubset(set_1)  # True
# print set_4.issubset(set_4)  # True
# print set_1.issubset(set_4)  # False
#
# print set_4.issuperset(set_1)  # False
# print set_4.issuperset(set_4)  # True
# print set_1.issuperset(set_4)  # True
#
# print set_1 > set_2
# print set_1 > set_4
#
#
# BUILD-IN METHODS - DATA TYPE CONVERSION
#
# import datetime
# now = datetime.datetime.now()
#
# print int('6')  # converts x to an integer
# print long('5500')  # converts x to a long integer
# print float(7)  # converts x to a floating-point number
# print complex('1+2j')  # creates a complex number
# print str(now)  # converts x to a string representation - computes a string containing the value of now
# print repr(now)  # converts x to an expression string - returns the code needed to rebuild now object with eval()
# print eval('1 + 4')  # interprets a string as code and evaluates it
# print tuple([1, 2, 3])  # converts x to a tuple
# print list((2, 4, 6))  # converts x to a list
# print dict([(2, 4), (3, 9), (4, 16)])  # creates a dictionary from a sequence of (key,value) tuples
#
#
# BUILD-IN METHODS - MATH
#
# print divmod(17, 5)  # the pair (x // y, x % y)
# print round(80.23456, 2)  # x rounded to n digits from the decimal point - round(0.5) is 1.0, round(-0.5) is -1.0
# print pow(100, 2)  # the value of x**y
# print max(54, 99, 1000)  # the largest of its arguments: the value closest to positive infinity
# print min(-100, 40, 8)  # the smallest of its arguments: the value closest to negative infinity
# print cmp(80, 100)  # -1 if x < y, 0 if x == y, or 1 if x > y
#
#
# OPERATORS
#
# Python language supports the following types of operators:
#
#     - arithmetic operators (+, -, /, //, **)
#     - comparison (relational) operators (==, !=, <, >, <=, >=)
#     - assignment operators (=, +=, -=, *=, /=, %=, **=, //=)
#     - logical operators (and, or, not)
#     - bitwise operators (&, |, ^, ~, >>, <<)
#     - membership operators (not in, in)
#     - identity operators (is, is not)
#
#
# IF STATEMENT AND SIMPLE LOOPS EXAMPLES
#
# It is possible to use a 'for' loop through: list, dict, string etc.
#
# 1 example: for, break
#
# for letter in 'python':
#     if letter == 'h':
#         break
#     print 'current letter :', letter
#
# 2 example: while, break
#
# var = 10
# while var > 0:
#     print 'current variable value :', var
#     var -= 1
#     if var == 5:
#         break
#
# 3 example: for, continue
#
# for letter in 'python':
#     if letter == 'h':
#         continue
#     print 'current letter :', letter
#
# 4 example: while, continue
#
# var = 10
# while var > 0:
#     var -= 1
#     if var == 5:
#         continue
#     print 'current variable value :', var
#
# 5 example: for, pass
#
# for letter in 'Python':
#     if letter == 'h':
#         pass
#         print 'this is pass block'
#     print 'current letter :', letter
#
# 6 example: for, enumerate(example_list)
#
# example_list = ['first', 'second', 'third']
# for index, item in enumerate(example_list, start=0):
#     print index + 1, item
#
# 7 example: for, zip(list_1, list_2)
#
# list_1 = [3, 9, 17, 15, 19]
# list_2 = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
# for a, b in zip(list_1, list_2):
#     if a > b:
#         print a
#     else:
#         print b
#
# 8 example: for, items()
#
# example_dict = {1: 1, 2: 2, 3: 3, 4: 4}
#
# for k, v in example_dict.items():
#     if example_dict[k] is v:
#         print 'objects are the same'
#     else:
#         print 'objects are different'
#
# # 9 example: for, iteritems()
#
# example_dict = {1: 1, 2: 2, 3: 3, 4: 4}
#
# for k, v in example_dict.iteritems():
#     if example_dict[k] is v:
#         print 'objects are the same'
#     else:
#         print 'objects are different'
#
#
# IMPORTS, LIBRARIES, UTILITIES
#
# Importing order in Python:
#   - standard library
#   - external frameworks/tools
#   - local modules
#
# import math  # imports entire library
# print math.sqrt(25)
#
# from math import *  # imports entire library, not recommended because of polluting the namespace
# print sqrt(25)
#
# from math import sqrt
# print sqrt(25)
#
# from math import sqrt as pierwiastek
# print pierwiastek(25)
#
# pylint - Python tool that checks for errors in Python code, tries to enforce a coding standard and looks for code
# smells. It can also look for certain type errors, it can recommend suggestions about how particular blocks can be
# refactored and can offer you details about the code’s complexity. Other similar projects would include the now defunct
# pychecker, pyflakes, flake8 and mypy. The default coding style used by Pylint is close to PEP 008.
# (to install on Ubuntu: sudo apt-get install pylint)
#
# isort - Python tool to sort imports alphabetically and separate them automatically into sections. It provides a
# command line utility, Python library and plugins for various editors to quickly sort all your imports. It is very
# useful in Django projects, especially in views where we usually deal with a great amount of imports.
# (to install on Ubuntu: sudo apt-get install isort)
#
# coverage - Python tool for measuring code coverage of Python programs. It monitors your program, noting which parts
# of the code have been executed, then analyzes the source to identify code that could have been executed but was not.
# Coverage measurement is typically used to gauge the effectiveness of tests. It can show which parts of your code are
# being exercised by tests, and which are not.
# (to install on Ubuntu: need to install the python-dev and gcc support files before installing coverage via pip)
#
# pdb - module that defines an interactive source code debugger for Python programs. It supports setting (conditional)
# breakpoints and single stepping at the source line level, inspection of stack frames, source code listing, and
# evaluation of arbitrary Python code in the context of any stack frame. It also supports post-mortem debugging and can
# be called under program control.
# (to install on Ubuntu: import pdb)
#
#
# LIST AND DICT COMPREHENSION
#
# evens_to_50 = [x for x in range(51) if x % 2 == 0]
# doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
# even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
# cubes_by_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0]
# threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]
# squares = {x: x**2 for x in [1,2,3,4,5]}
#
#
# BUILD-IN METHODS AND GENERAL EXPRESSIONS
#
# to_print = raw_input('What\'s the result of 2+2: ')
# print 'You said that the result of {0} + {1} is {2}'.format(2, 2, to_print)
# print 'You said that the result of %s + %s is %s' % (2, 2, to_print)
# print 'Beautiful english word list: Assemblage, Bucolic, Comely, Denouement, Ebullience, Forbearance, Gossamer, ' \
#       'Harbinger, Ineffable, Labyrinthine, Mellifluous, Nemesis, Opulent'
# example_list = ['one', 'two', 'three']
# del example_list[0]   # del statements - removes an object
# print example_list
# print sum([2, 2, 2, 2, 2], 2)  # sums value items in iterable object from start point
# print len('string_with_25_characters')  # return the length (the number of items) of an object
# print sorted([1, 2, 3, 4, 5])  # return a new sorted list from the items in iterable object



# FINISH HERE
# http://anandology.com/python-practice-book/iterators.html
# https://stackoverflow.com/questions/9884132/what-exactly-are-pythons-iterator-iterable-and-iteration-protocols

# range() creates a list, which all values are stored in memory and you can read from it item by item during iteration
# (in Python 3 range is supported, but the type is 'range' not 'list' )
# for num in range(2, 50, 4):
#     print num
# xrange() creates a generator object, that is iterator, which all values are not stored in the memory. They generate
# the values on the fly (in Python 3 xrange is not supported)
# for num in xrange(2, 50, 4):
#     print num

# yield
#
# zip
#
# keys = ['a','b','c']
# values = [1,2,3]
# print zip(keys,values)
#
# dict_from_zip = {}
# for (k,v) in zip(keys, values):
#     dict_from_zip[k] = v
# print dict_from_zip













# UNIT TESTING
#
# '''do funkcji check_letter piszemy testy'''
#
# import unittest
#
# def check_letter(word, letter):
#     if letter in word:
#         return True
#     else:
#         return False
#
# class Test1(unittest.TestCase):
#     def test_letter(self):
#         x = check_letter('michal', 'i')
#         self.assertTrue(x)
#
# if __name__ == '__main__':
#     unittest.main()
#
# Testy jednostkowe i asercja
#
# import unittest
#
# class MathTest(unittest, TestCase):
#
#    def test_add(self):
#        self.assertEqual(2+3, 5)
#
# PYTHON TRICKS
# w Pythonie 2.x. True może mieć przypisaną wartość False
#
# *args = list of arguments
# **kwargs = dictionary of arguments, in which keys = names of argument, values = values of argument
# it is used when you are not sure how many named/unnamed arguments might be passed to your function
#
# def print_everything(*args):
#     for count, thing in enumerate(args):
#         print '{0}. {1}'.format(count, thing)
#
# def table_things(**kwargs):
#     for name, value in kwargs.items():
#         print '{0} = {1}'.format(name, value)
#
# print_everything('apple', 'banana', 'cabbage')
# table_things(apple='fruit', cabbage='vegetable')
#
# list_c + lambda żeby kwadraty liczy od 1 do 50
#
# lambdą i list comprehensions zrobić kwadraty od 1 do 50
# kwadrat = lambda x: x**2
# sqr_to_50 = [kwadrat(i) for i in range(51)]
# print sqr_to_50
#
# print map(lambda x: x**2, range(51)) # dla każdego argumentu z listy wykona się funkcja
#
# '''Anonymous function - gdy użyjemy razem funkcji filter oraz lambda, funkcja
# filter użyji lambdy, aby określić co ma filtrować z listy'''
#
# my_list = range(16)
# print filter(lambda x: x % 3 == 0, my_list)
#
# languages = ['HTML', 'JavaScript', 'Python', 'Ruby']
# print filter(lambda x: x == 'Python', languages)
#
# squares = [x ** 2 for x in range(1, 11)]
# print filter(lambda x: 30 < x < 70, squares)
#
# Check orders of paragraphs, missing build-in methods and general statemens and Python tricks, list of useful libraries
