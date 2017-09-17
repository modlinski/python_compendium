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
# print hasattr(int, 'real')  # return True if the string is the name of one of the object’s attributes
# print getattr(int, 'real')  # return the value of the named attribute
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
# print help()  # invoke the built-in help system - this function is intended for interactive use
# print globals()  # return a dictionary representing the current global symbol table.
# print locals()  # update and return a dictionary representing the current local symbol table
# print issubclass(str, basestring)  # return true if class is a subclass (direct, indirect or virtual) of classinfo
# print isinstance('example', basestring)  # basestring is the superclass for str and unicode
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
# print(frozenset('sonorous'))  # returns a frozenset of elements
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
# print bin(1000)  # converts an x to a binary string e.q. '0b1111101000'
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
# ITERABLE OBJECTS, ITERATORS, GENERATORS
#
# Iterable objects - objects that can be used with a for loop (examples types: list, dict, string etc).
# The iteration protocol - __iter__ method makes an object iterable. Behind the scenes, the built-in 'iter' function
# calls __iter__ method on the given iterable object. The return value of __iter__ is an iterator. Iterator should have
# a next() method and raise StopIteration when there are no more elements. Each time the next() method is called the
# iterator returns the next element.
#
# class IterableObject(object):
#     def __init__(self, n):
#         self.n = n
#
#     def __iter__(self):
#         return IterableObjectIterator(self.n)
#
# class IterableObjectIterator(object):
#     def __init__(self, n):
#         self.i = 0
#         self.n = n
#
#     def __iter__(self):
#         # Iterators are iterables too.
#         # Adding this functions to make them so.
#         return self
#
#     def next(self):
#         if self.i < self.n:
#             i = self.i
#             self.i += 1
#             return i
#         else:
#             raise StopIteration()
#
# iterable = IterableObject(5)
#
# print list(iterable)  # prints [0, 1, 2, 3, 4]
# print list(iterable)  # prints [0, 1, 2, 3, 4]
#
# iterator = IterableObjectIterator(5)
#
# print list(iterator)  # prints [0, 1, 2, 3, 4]
# print list(iterator)  # prints [] if iterable and iterator are the same object, it is consumed in a single iteration
#
# Generators simplifies creation of iterators. A generator is a function that produces a sequence of results instead of
# a single value.
#
# def generator_object(n):
#     i = 0
#     while i < n:
#         yield i
#         i += 1
#
# Each time the yield statement is executed the function generates a new value.
#
# gen = generator_object(3)
# print gen  # <generator object generator_object at 0x02454C10>
# print gen.next()  # 0
# print gen.next()  # 1
# print gen.next()  # 2
# print generator.next()  # StopIteration
#
# Generator is also an iterator. The word “generator” is sometimes confusingly used to mean both the function that
# generates and what it generates. I will use the word “generator” to mean the generated object and “generator function”
# to mean the function that generates it. Can you think about how it is working internally? When a generator function is
# called, it returns a generator object without even beginning execution of the function. When next() method is called
# for the first time, the function starts executing until it reaches yield statement. The yielded value is returned by
# the next call. The following example demonstrates the interplay between yield and call to next() method on generator
# object.
#
# def generator_function():
#     print "begin"
#     for i in range(3):
#         print "before yield", i
#         yield i
#         print "after yield", i
#     print "end"
#
# gen = generator_function()
# print gen.next()  # begin, before yield 0, 0
# print gen.next()  # after yield 0, before yield 1, 1
# print gen.next()  # after yield 1, before yield 2, 2
# print gen.next()  # after yield 2, end, StopIteration
#
#
# IF STATEMENT AND SIMPLE LOOPS EXAMPLES
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
# 8 example: for, zip(keys, values)
#
# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# dict_from_zip = {}
# for (k, v) in zip(keys, values):
#     dict_from_zip[k] = v
# print dict_from_zip
#
# 9 example: for, items()
#
# example_dict = {1: 1, 2: 2, 3: 3, 4: 4}
# for k, v in example_dict.items():
#     if example_dict[k] is v:
#         print 'objects are the same'
#     else:
#         print 'objects are different'
#
# 10 example: for, iteritems()
#
# example_dict = {1: 1, 2: 2, 3: 3, 4: 4}
# for k, v in example_dict.iteritems():
#     if example_dict[k] is v:
#         print 'objects are the same'
#     else:
#         print 'objects are different'
#
# 11 example: if, elif, else
#
# num = 5
# if num > 2:
#     print 'first if'
# elif num > 3:
#     print 'elif'
# if num > 4:
#     print 'second if'
# else:
#     print 'else'
#
# 12 example: for, else
#
# container = [1, 2, 3, 4, 5, 6, 7]  # container to execute else clause
# container = [1, 2, 3, 0, 5, 6, 7]  # container to not execute else clause
#
# for item in container:
#     if item == 0:
#         print "Finds zero!"
#         break
# The else clause executes when the loop completes normally. This means that the loop did not encounter any break.
# else:
#     print "Didn't find anything..."
#
#
# FUNCTIONS
#
# def len_string(word):
#     word = str(word)
#     len_str = len(word)
#     return len_str
#
# def substring(word, length, letter):
#     word = str(word)
#     letter -= 1
#     sub_str = word[letter:letter + length]
#     return sub_str
#
# import sys
# print sys.getrecursionlimit()  # default recursion limit in Python 1000
# sys.setrecursionlimit(1500)  # recursion limit can be changed
#
# def recursive_reverse(word):  # recursive function
#     word = str(word)
#     if len_string(word) == 0:
#         return ''
#     else:
#         a = substring(word, len_string(word) - 1, 1)
#         b = substring(word, 1, len_string(word))
#         return b + recursive_reverse(a)
#
# print(recursive_reverse('paulina'))
#
# def print_everything(*args):  # list of arguments
#     for count, thing in enumerate(args):
#         print '{0}. {1}'.format(count, thing)
#
# def table_things(**kwargs): # dict of arguments, in which keys = names of arguments, values = values of arguments
#     for name, value in kwargs.items():
#         print '{0} = {1}'.format(name, value)
#
# print_everything('apple', 'banana', 'cabbage')
# table_things(apple='fruit', cabbage='vegetable')
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
#
# print 'Beautiful english word list: Assemblage, Bucolic, Comely, Denouement, Ebullience, Forbearance, Gossamer, ' \
#       'Harbinger, Ineffable, Labyrinthine, Mellifluous, Nemesis, Opulent'
#
# example_list = ['one', 'two', 'three']
# del example_list[0]   # del statements - removes an object
# print example_list
#
# print sum([2, 2, 2, 2, 2], 2)  # sums value items in iterable object from start point
#
# print len('string_with_25_characters')  # return the length (the number of items) of an object
#
# print sorted([1, 2, 3, 4, 5])  # return a new sorted list from the items in iterable object
#
# range() creates a list object <type 'list'>, which all values are stored in memory and you can read from it item by
# item during iteration (in Python 3 range is supported, but the type of it is 'range' not 'list' and it is implemented
# like 'xrange' in Python 2)
# for num in range(2, 50, 4):
#     print num
#
# xrange() creates a generator object <type 'xrange'>, that is an iterator, which all values are not stored in the
# memory. They generate the values on the fly (in Python 3 xrange is not supported)
# for num in xrange(2, 50, 4):
#     print num
#
# xrange() is generally faster than range() and needs less memory. range() is generally slower than xrange() and needs
# more memory (to create array of integers). range() can be better if you iterate multiple times over the same range of
# values, because xrange has to generate an integer object every time you access an index, whereas range is a static
# list and the integers are already "there" to use. Examples:
#
# from time import time
#
# n = 1000
# lst = range(n)
# gen = xrange(n)
#
# def test_range(n):
#     for _ in range(n*n):
#         pass
#
# def test_xrange(n):
#     for _ in xrange(n*n):
#         pass
#
# def test_range_read_from_list(n):
#     for i in xrange(n):
#         for _ in lst:
#             pass
#
# def test_xrange_generate_integer(n):
#     for i in xrange(n):
#         for _ in gen:
#             pass
#
# start = time()
# test_range(n)
# print "Time of execution for test_range(n): ", time() - start
# start = time()
# test_xrange(n)
# print "Time of execution for test_xrange(n): ", time() - start
# start = time()
# test_range_read_from_list(n)
# print "Time of execution for test_range_read_from_list(n): ", time() - start
# start = time()
# test_xrange_generate_integer(n)
# print "Time of execution for test_xrange_generate_integer(n): ", time() - start
#
# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# print zip(keys, values)  # returns a list of tuples
#
# The lambda operator/lambda function is a expression using to create small anonymous functions (which do not need to
# bounded to a name) at runtime. These functions are throw-away functions - they are just needed where they have been
# created. Lambda functions are mainly used in combination with the functions filter(), map() and reduce().
#
# def moreThanFive(element):
#     return element > 5
#
# print filter(moreThanFive, range(0, 11))  # returns a list from elements of iterable for which function returns true
# print filter(lambda x: 30 < x < 70, [x ** 2 for x in range(1, 11)])
#
# print map(lambda x, y: x**y, range(1, 5), range(2, 6))  # apply function to every item of iterables and return a list
#
# print all([1, 2, 3, 0])  # return True if all elements of the iterable are true (or if the iterable is empty)
#
# print any([0, 0, 0, 1])  # return True if any element of the iterable is true. If the iterable is empty, return False
#
# print bool([1])  # return a Boolean value, x is converted using the standard truth testing procedure
#
# for byte in bytearray('example_string'):  # return a new array of bytes
#     print byte
#
# print unicode(97)  # return the Unicode string version of object
# print type(unicode(97))
#
# print unichr(97)  # return the Unicode string of one character whose Unicode code is the integer i
# print type(unichr(97))
#
# print chr(97)  # return a string of one character whose ASCII code is the integer i
#
# print ord('a')  # return an integer representing the Unicode code point of the character
#
# class Foobar(object):
#     att_1 = 'exist'
#
# print Foobar.att_1
#
# delattr(Foobar, 'att_1')  # equivalent to del Foobar.att_1
#
# print Foobar.att_1  # AttributeError: type object 'Foobar' has no attribute 'att_1'
#
# print hash('michal')  # return the hash value of the object (if it has one)
#
# print input()  # equivalent to eval(raw_input(prompt))
#
# print iter([1, 2, 3, 4, 5, 6])  # return an iterator object
#
# for i in reversed([1, 2, 3, 4, 5]):  # return a reverse iterator
#     print i
#
# def product(numbers):  # reduce apply function of two arguments cumulatively to the items of iterable, from the left
#     return reduce(lambda x, y: x * y, numbers)
#
# print product([1, 2, 3, 4, 5])
#
# print(vars(str))  # return __dict__ attribute for a module, class, instance, or any object with a __dict__ attribute
#
#
# UNIT TESTING
#
# import unittest
#
# def check_letter(word, letter):  # method to test
#     if letter in word:
#         return True
#     else:
#         return False
#
# class TestLetters(unittest.TestCase):
#     def test_letter_m_in(self):
#         x = check_letter('michal', 'm')
#         self.assertTrue(x)
#     def test_letter_i_in(self):
#         x = check_letter('michal', 'i')
#         self.assertTrue(x)
#     def test_letter_c_in(self):
#         x = check_letter('michal', 'c')
#         self.assertTrue(x)
#     def test_letter_f_not_in(self):
#         x = check_letter('michal', 'f')
#         self.assertFalse(x)
#
# class TestMath(unittest.TestCase):
#    def test_add(self):
#        self.assertEqual(2+3, 5)
#
# if __name__ == '__main__':
#     unittest.main()
#
#
# BUILT-IN EXCEPTIONS
#
# Built-in exceptions that are only used as base classes for other exceptions:
#
# BaseException - the base for all built-in exceptions. It is not meant to be directly inherited by user-defined classes
# Exception - all user-defined exceptions should be derived from this class
# StandardError, ArithmeticError, BufferError, LookupError, EnvironmentError
#
# Built-in exceptions that are actually raised:
#
# SyntaxError - also known as parsing errors
# AssertionError - raised when an assert statement fails
# AttributeError, GeneratorExit, IOError, ImportError, IndexError, KeyError, KeyboardInterrupt, MemoryError, NameError,
# NotImplementedError, OverflowError, ReferenceError, RuntimeError, StopIteration, IndentationError, SystemError,
# SystemExit, TypeError, UnicodeError, ValueError, ZeroDivisionError
#
# Built-in exceptions that are used as warning categories (all are used as base class for warnings:
#
# Warning, UserWarning, DeprecationWarning, PendingDeprecationWarning, SyntaxWarning, RuntimeWarning, FutureWarning,
# ImportWarning, UnicodeWarning
#
# Examples:
# print 10 * (1/0)  # ZeroDivisionError: integer division or modulo by zero
# print 4 + spam*3  # NameError: name 'spam' is not defined
# print '2' + 2  # TypeError: cannot concatenate 'str' and 'int' objects
#
#
# HANDLING AND RAISING EXCEPTIONS, USER-DEFINED EXCEPTIONS
#
# It is possible to write programs that handle selected exceptions.
#
# while True:
#     try:
#         x = int(raw_input("Please enter a number: "))
#         break
#     # if ValueError or MemoryError occur during execution of the try clause, the rest of the clause is skipped and the
#     # except clause is executed, and then execution continues after the try statement
#     except (ValueError, MemoryError):  # parentheses are required
#         print "Oops!  That was no valid number.  Try again..."
#
# sys module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter. It is always available.
# import sys
#
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# # except IOError, e:  # old syntax supported for backwards compatibility
# except IOError as e:  # modern Python syntax
#     # attributes of super class EnvironmentError: errno (error number) and strerror (associated error message)
#     print "I/O error({0}): {1}".format(e.errno, e.strerror)
# except ValueError:
#     print "Could not convert data to an integer."
# # the last except clause may omit the exception name(s), to serve as a wildcard;
# # it can also be used to print an error message and then re-raise the exception;
# # this syntax is not recommended since it is easy to mask a real programming error in this way
# except:
#     print "Unexpected error:", sys.exc_info()[0]
#     raise
#
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except IOError as e:
#     print "I/O error({0}): {1}".format(e.errno, e.strerror)
# except ValueError:
#     print "Could not convert data to an integer."
# # else clause will be executed if the try clause does not raise an exception
# else:
#     print i
#     f.close()
#
# When an exception occurs, it may have an associated value (exception’s argument). The except clause may specify a
# variable after the exception name (or tuple). The variable is bound to an exception instance with the arguments stored
# in instance.args. For convenience, the exception instance defines __str__() so the arguments can be printed directly
# without having to reference .args.
#
# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print type(inst.args)  # <type 'tuple'>
#     print type(inst)  # the exception instance: <type 'exceptions.Exception'>
#     print inst.args  # arguments stored in .args: ('spam', 'eggs')
#     print inst  # __str__ allows args to be printed directly: ('spam', 'eggs')
#     x, y = inst.args
#     print 'x =', x
#     print 'y =', y
#
# The raise statement allows the programmer to force a specified exception to occur. The sole argument to raise must be
# either an exception instance or an exception class:
#
# raise NameError('HiThere')
#
# If you need to determine whether an exception was raised but don’t intend to handle it, a simpler form of the raise
# statement allows you to re-raise the exception:
#
# try:
#     raise NameError('HiThere')
# except NameError:
#     print 'An exception flew by!'
#     raise
#
# Programs may name their own exceptions by creating a new exception class. Exceptions should typically be derived
# from the Exception class, either directly or indirectly.
#
# class MyError(Exception):
#
#     # The default __init__() of Exception has been overridden. The new behavior simply creates the value attribute.
#     # This replaces the default behavior of creating the args attribute.
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return repr(self.value)
#
# try:
#     raise MyError(2*2)
# except MyError as e:
#     print 'My exception occurred, value:', e.value
#
# In a module that can raise several distinct errors, a common practice is to create a base class for exceptions defined
# by that module, and subclass that to create specific exception classes for different error conditions.
#
# class Error(Exception):
#     """Base class for exceptions in this module."""
#     pass
#
# class TransitionError(Error):
#     """Raised when an operation attempts a state transition that's not
#     allowed.
#
#     Attributes:
#         prv -- state at beginning of transition
#         nxt -- attempted new state
#         msg  -- explanation of why the specific transition is not allowed
#     """
#
#     def __init__(self, prv, nxt, msg):
#         self.prv = prv
#         self.nxt = nxt
#         self.msg = msg
#
# try:
#     raise TransitionError(0, 2, "Transition from 0 state not allowed!")
# except TransitionError as error:
#     print 'A New Exception occurred: ', error.msg
#
# The try statement has another optional clause which is intended to define clean-up actions that must be executed under
# all circumstances.
#
# try:
#     raise KeyboardInterrupt
# finally:
#     print 'Clean-up action'
#
# The finally clause is always executed before leaving the try statement, whether an exception has occurred or not. When
# an exception has occurred in the try clause and has not been handled by an except clause (or it has occurred in an
# except or else clause), it is re-raised after the finally clause has been executed. The finally clause is also
# executed “on the way out” when any other clause of the try statement is left via a break/continue/return statement. As
# you can see, in a more complicated example below, the finally clause is executed in any event:
#
# def divide(x, y):
#     try:
#         result = x / y
#     # except TypeError:  # uncomment to cause unhandled exception
#     except ZeroDivisionError:
#         # print 1 / 0  # uncomment to cause exception in except clause
#         print "division by zero!"
#     else:
#         # print 1 / 0  # uncomment to cause exception in else clause
#         print "result is", result
#         # return
#     finally:
#         print "executing finally clause"
#
# divide(4, 0)
# divide(4, 2)
#
#
# PYTHON TRICKS AND TIPS
#
# False = True  # In Python 2 False can be assigned to True
#
# print "oblivion"[::-1]  # reversing a string in Python
#
# mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print zip(*mat)  # transposing a matrix
#
# x, y, z = [1, 2, 3]  # store all three values of the list in 3 new variables
# print x, y, z
#
# a = 7
# b = 2
# b, a = a, b  # swap two numbers with one line of code
# print a, b
#
# nums = [0, 1, 2, 3, 4, 5]
# last_three = slice(-3, None)  # naming slices (slice(start, end, step))
# print nums[last_three]
#
# a = [1, 2, 3]
# b = ['a', 'b', 'c']
# zipped = zip(a, b)  # zipping iterables by zip()
# unzipped = zip(*zipped)  # unzipping iterables by *
# print zipped
# print unzipped
#
# letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print letters.values(), letters.keys()
# print zip(letters.values(), letters.keys())
# inverted = dict(zip(letters.values(), letters.keys()))  # inverting a dictionary using zip
# print inverted
#
# letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# inverted = {v: k for k, v in letters.items()}  # inverting a dictionary using dit comprehension
# print inverted
#
# a = [[1, 2], [3, 4], [5, 6]]
# print sum(a, [])  # flattening list using sum() with start parameter equal to [], not default 0
# print [x for l in a for x in l]  # flattening list using list comprehension
# flatten = []  # flattening list using loop - compare syntax with code above
# for l in a:
#     for x in l:
#         flatten.append(x)
# print flatten
# a = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# def flatten(to_flat):  # flattening list using recursive function - can flat all kind of nested list
#     if type(to_flat) is list:
#         return [y for l in to_flat for y in flatten(l)]
#     else:
#         return [to_flat]
# print flatten(a)
#
# The "==" operator compares by checking for equality. The "is" operator, however, compares identities.
# Python uses the same object instance for numbers from -1 to 256
#
# print [1, 2, 3] == [1, 2, 3]
# print [1, 2, 3] is [1, 2, 3]
#
# An augmented assignment expression like x += 1 can be rewritten as x = x + 1 to achieve a similar, but not exactly
# equal effect. In the augmented version, x is only evaluated once. Also, when possible, the actual operation is
# performed in-place, meaning that rather than creating a new object and assigning that to the target, the old object is
# modified instead. It has no implication for integers or float as they are immutable, but for most mutable containers
# there is a difference between x += 1 and x = x + 1. For example if you have multiple variables all referring to the
# same list:
#
# x = []
# y = x
# x += [1]  # the interpreter treats it like x = x.__iadd__([1]); it extends an existing list
# print id(x), x
# print id(y), y
# x = x + [1]  # the interpreter treats it like x = x.__add__([1]); it returns a new list
# print id(x), x
# print id(y), y
#
# __iadd__ can be much more efficient because it does not necessarily need to make a copy of x
#
# import dis  # The dis module supports the analysis of CPython bytecode by disassembling it
#
# def test1(x):
#     x = x + 1
#
# def test2(x):
#     x += 1
#
# print dis.dis(test1)
# print dis.dis(test2)
#
# from copy import deepcopy
#
# num_lis = [1, 2, 3, 4, 5, 6, 7, 8]
# num_lis_2 = deepcopy(num_lis)
#
# for i in num_lis:
#     del num_lis[-1]  # modify the list over which we iterate
#     print i
#
# for j in num_lis_2:  # we iterate over deep copy of the original list
#     del num_lis[-1]  # modify the original list
#     print j
#
# def power(fun, x):  # passing function as parameter
#     return fun(x)
#
# print power(lambda x: x * x, 3)
#
# '__main__' is the name of the scope in which top-level code executes. A module’s __name__ is set equal to '__main__'
# when read from standard input, a script, or from an interactive prompt. When the file is imported by another module,
# __name__ is set to the module's name. A module can discover whether or not it is running in the main scope by checking
# its own __name__, which allows a common idiom for conditionally executing code in a module when it is run as a script
# or with python -m but not when it is imported. So if file is imported the following 'print' will be not executed:
#
# if __name__ == "__main__":
#     print __name__
#
# Python’s default arguments are evaluated once when the function is defined, not each time the function is called (like
#  it is in say, Ruby). This means that if you use a mutable default argument and mutate it, you will and have mutated
# that object for all future calls to the function as well.
#
# def append_to(element, to=[]):  # works like append_to_list_before
#     to.append(element)
#     return to
#
# Create a new object each time the function is called, by using a default arg to signal that no argument was provided.
# def append_to(element, to=None):  # works like append_to_list_inside
#     if to is None:
#         to = []
#     to.append(element)
#     return to
#
# to = []
# def append_to_list_before(element):
#     to.append(element)
#     return to
#
# def append_to_list_inside(element):
#     to = []
#     to.append(element)
#     return to
#
# my_list = append_to(12)
# print my_list  # [12]
# my_other_list = append_to(42)
# print my_other_list  # [12, 42] or [42]
#
# my_list = append_to_list_before(12)
# print my_list  # [12]
# my_other_list = append_to_list_before(42)
# print my_other_list  # [12, 42]
#
# my_list = append_to_list_inside(12)
# print my_list  # [12]
# my_other_list = append_to_list_inside(42)
# print my_other_list  # [42]
#
# Late binding closures - another common source of confusion is the way Python binds its variables in closures (or in
# the surrounding global scope). Python’s closures are late binding. This means that the values of variables used in
# closures are looked up at the time the inner function is called.
#
# def create_multipliers_with_lambda():
#     return [lambda x: i * x for i in range(5)]
#
# def create_multipliers_without_lambda():
#     multipliers = []
#     for i in range(5):
#         def multiplier(x):
#             return i * x
#         multipliers.append(multiplier)
#     return multipliers
#
# Here, in create_multipliers_with_lambda or create_multipliers_without_lambda methods, whenever any of the returned
# functions are called, the value of i is looked up in the surrounding scope at call time. By then, the loop has
# completed and i is left with its final value of 4.
#
# to change the behaviour you can create a closure that binds immediately to its arguments by using a default arg
# def create_multipliers_default_arg():
#     return [lambda x, n=i: n * x for i in range(5)]
#
# alternatively, you can use the functools.partial function
# from functools import partial
# from operator import mul
#
# def create_multipliers_partial_mul():
#     return [partial(mul, i) for i in range(5)]
#
# for multiplier in create_multipliers_with_lambda():
#     print multiplier(2)
#
# for multiplier in create_multipliers_without_lambda():
#     print multiplier(2)
#
# for multiplier in create_multipliers_default_arg():
#     print multiplier(2)
#
# for multiplier in create_multipliers_partial_mul():
#     print multiplier(2)
#
# LEGB is a set of rules for Python scope resolution. These rules are specific to variable names, not attributes. If you
# reference it without a period, these rules apply:
#
# L, Local - names assigned in any way within a function (def or lambda), and not declared global in that function.
# E, Enclosing-function locals - name in the local scope of any and all statically enclosing functions (def or lambda),
# from inner to outer.
# G, Global (module) - names assigned at the top-level of a module file, or by executing a global statement in a def
# within the file.
# B, Built-in (Python) - names preassigned in the built-in names module, like e.q.: open, range, list etc.
#
# For loop or if statement have not their own namespace.
#
# global_var = 0
# class ScopeClass(object):
#     # this will not affect global_var, but will create a new variable in inner scope
#     global_var = global_var + 1
#     def scope_method(self):
#         def_var = 2
#         for _ in range(10):
#             loop_var = 3
#             break
#         else:
#             loop_var = 6
#         print global_var, self.global_var  # prints 0, 1
#         print def_var, loop_var  # prints 2, 3
#
# ScopeClass().scope_method()
#
# def scope_function():
#     x = 4
#     def inside_function():
#         print x  # accesses x from scope_function scope
#     inside_function()  # prints 4
#     x = 5
#     inside_function()  # prints 5
#
# scope_function()
#
# Variables in scopes other than the local function's variables can be accessed, but can't be rebound to new parameters
# without further syntax. Instead, assignment will create a new local variable instead of affecting the variable in the
# parent scope. For example:
#
# global_var_1 = []
# global_var_2 = 1
#
# def scope_function():
#
#     # this will affect global_var_1 and will not create a new variable in inner scope
#     global_var_1.append(4)
#     print global_var_1  # prints [4]
#
#     # this will not affect global_var_2, but will create a new variable in inner scope
#     global_var_2 = 2  # shadow name 'global_var_2' from outer scope
#     print global_var_2  # prints 2
#
#     local_var_1 = 4
#     def inside_function():
#         # this will not affect local_var_1, but will create a new variable in inner scope
#         local_var_1 = 5  # shadow name 'local_var_1' from outer scope
#         print local_var_1
#
#     inside_function()  # prints 5
#     print local_var_1  # prints 4
#
# scope_function()
# print global_var_1  # prints [4]
# print global_var_2  # prints 1
#
# In order to actually modify the bindings of global variables from within a function scope, you need to specify that
# the variable is global with the global keyword. Currently there is no way to do the same for variables in enclosing
# function scopes, but Python 3 introduces a new keyword, "nonlocal" which will act in a similar way to global, but for
# nested function scopes.
#
# global_var = 1
#
# def change_global():
#     global global_var
#     global_var = global_var + 1
#
# change_global()
# print global_var  # prints 2
#
# There are some differences between Python 2 and 3 in namespaces rules. It is worth noticing that In Python 2 the list
# comprehensions do not create a variable scope (while generators and dict comprehensions do). Instead they leak the
# value in the function or the global scope. In Python 3 comprehension expressions do not leak variables.
#
# i = 0
# list_scope = [i for i in range(5)]
# print(i)  # in Python 2 prints 4, in Python 3 prints 0
#
# j = 0
# dict_scope = {j: str(j) for j in range(5)}
# print(j)  # prints 0
#
# READING AND WRITING FILES
#
# Python provides basic functions and methods necessary to manipulate files. You can do most of the file manipulation
# using a file object. Before you can read or write a file, you have to open it using Python's built-in open() function.
# This function creates a file object, which would be utilized to call other support methods associated with it.
#
# f = open('file_name', 'w+')
# f = open('file_name.txt', 'w+')
#
# The first argument is a string containing the file name. The second argument defines access mode in which the file has
# to be opened - this is optional parameter and the default file access mode is read (r). Available modes:
#
# - 'r' - opens a file for reading only. The file pointer is placed at the beginning of the file.
# - 'r+' - opens a file for both reading and writing. The file pointer placed at the beginning of the file.
# - 'w' - opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a
# new file for writing.
# - 'w+' - opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does
# not exist, creates a new file for reading and writing.
# -'a' - opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is
# - in the append mode. If the file does not exist, it creates a new file for writing.
# - 'a+' - opens a file for both appending and reading. The file pointer is at the end of the file if the file exists.
# The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
#
# The file object attributes:
#
# print f.closed  # returns true if file is closed, false otherwise
# print f.mode  # returns access mode with which file was opened
# print f.name  # returns name of the file
#
# write() method - writes any string to an open file. It is important to note that Python strings can have binary data
# and not just text. The write() method does not add a newline character ('\n') to the end of the string.
#
# read() method - reads a string from an open file. It is important to note that Python strings can have binary data.
# apart from text data. Note also, that when you write a file at first, a then you read a file, the line you begin
# reading from is the line when you finished writing.
#
# close() method - closes file and frees up any system resources taken up by the opened file. After calling close()
# any attempt to use the file object will automatically fail. Python automatically closes a file when the reference
# object of a file is reassigned to another file. It is a good practice to use the close() method explicitly.
#
# tell() method - returns an integer giving the file object’s current position in the file, measured in bytes from the
# beginning of the file.
#
# seek(offset, from_what) - changes the file object’s position. The position is computed by adding an offset to a
# reference point. The reference point is selected by the from_what argument. A from_what value of 0 measures from the
# beginning of the file (it is default value if from_what is omitted), 1 uses the current file position, and 2 uses the
# end of the file as the reference point.
#
# f = open('file_name', 'w+')
# f.write('This is the 1 line\nThis is the 2 line - before empty line\n\nThis is the 4 line - after empty line')
# f.seek(0)  # to read from the beginning of the file
# f.seek(8, 0)  # to read from the 8th position of he file
# f.seek(-8, 2)  # to read from the 8th position before the end
# print f.tell()
# print f.read()
# f.close()
# print f.read()  # ValueError: I/O operation on closed file
#
# Different kinds of reading file content:
#
# f = open('file_name', 'w+')
# f.write('This is the 1 line\nThis is the 2 line - before empty line\n\nThis is the 4 line - after empty line')
# f.seek(0)
# print "line 1:  " + f.readline()  # returns first line of file
# print "line 2:  " + f.readline()  # returns second line of file
# print "line 3:  " + f.readline()  # returns third line of file
# print "line 4:  " + f.readline()  # returns fourth line of file
# f.close()
#
# f = open('file_name', 'w+')
# f.write('This is the 1 line\nThis is the 2 line - before empty line\n\nThis is the 4 line - after empty line')
# f.seek(0)
# print list(f)
#
# f = open('file_name', 'w+')
# f.write('This is the 1 line\nThis is the 2 line - before empty line\n\nThis is the 4 line - after empty line')
# f.seek(0)
# for line in f:
#     print line
#
# Context manager - it is a good practice to use the with keyword when dealing with file objects. This has the advantage
# that the file is properly closed after its suite finishes, even if an exception is raised on the way. It is also much
# shorter than writing equivalent try-finally blocks.
#
# with open('file_name', 'w+') as f:
#     f.write('This is the 1 line\nThis is the 2 line - before empty line\n\nThis is the 4 line - after empty line')
#     f.seek(0)
#     read_data = f.read()
#     print read_data
#     print f.closed  # returns False
# print f.closed  # returns True
#
# DECORATORS
#
# A decorator is a function or a class that wraps (or decorates) a function or a method. The ‘decorated’ function or
# method will replace the original ‘undecorated’ function or method. Because functions are first-class objects in Python
# this can be done ‘manually’, but using the @decorator syntax is clearer and thus preferred. This mechanism is useful
# for separating concerns and avoiding external un-related logic ‘polluting’ the core logic of the function or method.
#
# def power(x):
#     return x ** 2
#
# def decorator_double(func):
#     print 'message from decorator'
#     def double(x):
#         doubled_value = 2 * func(x)
#         return doubled_value
#     return double
#
# power = decorator_double(power)  # manually decorated
#
# @decorator_double  # decorated by @
# def power(x):
#     return x ** 2
#
# print power(3)  # prints 18
#
# A good example of a piece of functionality that is better handled with decoration is memoization or caching: you want
# to store the results of an expensive function in a table and use them directly instead of recomputing them when they
# have already been computed. This is clearly not a part of the function logic. It is possible to easily optimize and
# speed up e.q. recursive method returning numbers of Fibonacci sequence using memoization, because during computing the
# same values are called a lot of time. In addiction every next call of this method will be faster, because values will
# be still in saved in memory and method will have access to them.
#
# Recursive, decorated fib method with memoization - implemented using def:
#
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
# def memoize(f):
#     memo = {}
#     def helper(x):
#         if x not in memo:
#             memo[x] = f(x)
#         return memo[x]
#     return helper
#
# fib = memoize(fib)  # names of variable and method must be the same
#
# @memoize
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
# Recursive, decorated fib method with memoization - implemented using class:
#
# class Memoize:
#     def __init__(self, fn):
#         self.fn = fn
#         self.memo = {}
#     def __call__(self, *args):
#         if args not in self.memo:
#             self.memo[args] = self.fn(*args)
#         return self.memo[args]
#
# @Memoize
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# from time import time
#
# start = time()
# print fib(50)
# print "Time of execution: ", time() - start
#
# start = time()
# print fib(100)  # saves a lot of counting
# print "Time of execution: ", time() - start
#
# start = time()
# print fib(70)  # no counting - value read directly from memory
# print "Time of execution: ", time() - start
