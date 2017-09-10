# !/usr/bin/env python
# -*- coding: utf-8 -*-
from platform import python_version

# 1. The __future__ module
#
# Python 3.x introduced some Python 2-incompatible keywords and features that can be imported via the in-built
# __future__ module in Python 2. It is recommended to use __future__ imports it if you are planning Python 3.x
# support for your code. For example:
#
# from __future__ import division
# from __future__ import nested_scopes
# from __future__ import generators
# from __future__ import division
# from __future__ import absolute_import
# from __future__ import with_statement
# from __future__ import print_function
# from __future__ import unicode_literals
#
# 2. The print function
#
# Python 2
#
# print 'Python', python_version()
# print 'Hello World!'
# print('Hello World!')
# print "text", ; print 'print more text on the same line'  # not recommended by PEP8, but syntactically correct
# print 'a', 'b'  # strings are printed
# print('a', 'b')  # tuple is printed, since print is a “statement” in Python 2, not a function call
#
# Python 3
#
# print('Python', python_version())
# print('Hello, World!')
# print("some text,", end="")
# print(' print more text on the same line')
# print 'Hello, World!'  # SyntaxError: invalid syntax
#
# 3. Integer division
#
# Python 2
#
# print 'Python', python_version()
# print '3 / 2 =', 3 / 2  # = 1
# print '3 // 2 =', 3 // 2  # = 1
# print '3 / 2.0 =', 3 / 2.0  # = 1.5
# print '3 // 2.0 =', 3 // 2.0  # = 1.0
#
# Python 3
#
# print('Python', python_version())
# print('3 / 2 =', 3 / 2)  # = 1.5
# print('3 // 2 =', 3 // 2)  # = 1
# print('3 / 2.0 =', 3 / 2.0)  # = 1.5
# print('3 // 2.0 =', 3 // 2.0)  # = 1.0
#
# 4. Unicode
#
# Python 2
#
# print 'Python', python_version()
# print type(unicode('this is like a python3 str type'))
# print type(b'byte type does not exist')
# print 'they are really' + b' the same'
# print type(bytearray(b'bytearray oddly does exist though'))
#
# Python 3
#
# print('Python', python_version())
# print('strings are now utf-8 \u03BCnico\u0394é!')
# print('Python', python_version(), end="")
# print(' has', type(b' bytes for storing data'))
# print('and Python', python_version(), end="")
# print(' also has', type(bytearray(b'bytearrays')))
# 'note that we cannot add a string' + b'bytes for data'  # TypeError: Can't convert 'bytes' object to str implicitly
#
# 5. xrange and range
#
# Python 2
#
# for x in range(1000):  # creates a list
#     pass
#
# for y in xrange(1000):  # creates a generator
#     pass
#
# Python 3
#
# for z in range(1000):  # creates a generator
#     pass
#
# 6. Raising exceptions
#
# Python 2
#
# print 'Python', python_version()
# raise IOError, "file error"  # not recommended by PEP8, but syntactically correct
# raise IOError("file error")
#
# Python 3
#
# print('Python', python_version())
# raise IOError("file error")
#
# 7. Handling exceptions
#
# Python 2
#
# print 'Python', python_version()
# try:
#     let_us_cause_a_NameError
# except NameError, err:
#     print err, '--> our error message'
#
# Python 3
#
# print('Python', python_version())
# try:
#     let_us_cause_a_NameError
# except NameError as err:
#     print(err, '--> our error message')
#
# 8. The next() function and .next() method
#
# Python 2
#
# print 'Python', python_version()
# my_generator = (letter for letter in 'abcdefg')
# print next(my_generator)
# print my_generator.next()
#
# Python 3
#
# print('Python', python_version())
# my_generator = (letter for letter in 'abcdefg')
# print(next(my_generator))
# print(my_generator.next())  # AttributeError: 'generator' object has no attribute 'next'
#
# 9. For-loop variables and the global namespace leak
#
# In Python 3 for-loop variables do not leak into the global namespace anymore.
#
# Python 2
#
# print 'Python', python_version()
# i = 1
# print 'before: i =', i
# print 'comprehension: ', [i for i in range(5)]
# print 'after: i =', i
#
# Python 3
#
# print('Python', python_version())
# i = 1
# print('before: i =', i)
# print('comprehension:', [i for i in range(5)])
# print('after: i =', i)
#
# 10. Comparing unorderable types
#
# Python 2
#
# print 'Python', python_version()
# print "[1, 2] > 'foo' = ", [1, 2] > 'foo'
# print "(1, 2) > 'foo' = ", (1, 2) > 'foo'
# print "[1, 2] > (1, 2) = ", [1, 2] > (1, 2)
#
# Python 3
#
# print('Python', python_version())
# print("[1, 2] > 'foo' = ", [1, 2] > 'foo')  # TypeError: unorderable types: list() > str()
# print("(1, 2) > 'foo' = ", (1, 2) > 'foo')  # TypeError: unorderable types: tuple() > str()
# print("[1, 2] > (1, 2) = ", [1, 2] > (1, 2))  # TypeError: unorderable types: list() > tuple()
#
# 11. Parsing user inputs via input()
#
# Python 2
#
# print 'Python', python_version()
#  my_input = input('enter a number: ')  # enter 123
# print type(my_input)  # <type 'int'>
# my_raw_input = raw_input('enter a number: ')  # enter 123
# print type(my_raw_input)  # <type 'str'>
#
# Python 3
#
# print('Python', python_version())
# my_input = input('enter a number: ')  # enter 123
# print(type(my_input))  # <class 'str'>
#
# 12. Returning iterable objects instead of lists
#
# Python 2
#
# print 'Python', python_version()
# print type(range(3))  # <type 'list'>
# print type(zip([1, 2], [3, 4]))  # <type 'list'>
# print type(map(lambda x: x**2, [1, 2, 3, 4, 5]))  # <type 'list'>
# print type(filter(lambda x: 30 < x < 70, [x ** 2 for x in range(1, 11)]))  # <type 'list'>
# print type({1: 'a'}.keys())  # <type 'list'>
# print type({1: 'a'}.values())  # <type 'list'>
# print type({1: 'a'}.items())  # <type 'list'>
#
# Python 3
#
# print('Python', python_version())
# print(type(range(3)))  # <class 'range'>
# print(type(zip([1, 2], [3, 4])))  # <class 'zip'>
# print(type(map(lambda x: x**2, [1, 2, 3, 4, 5])))  # <class 'map'>
# print(type(filter(lambda x: 30 < x < 70, [x ** 2 for x in range(1, 11)])))  # <class 'filter'>
# print(type({1: 'a'}.keys()))  # <class 'dict_keys'>
# print(type({1: 'a'}.values()))  # <class 'dict_values'>
# print(type({1: 'a'}.items()))  # <class 'dict_items'>
#
# 13. Banker’s Rounding
#
# In Python 3 decimals are rounded to the nearest even number.
#
# Python 2
#
# print 'Python', python_version()
# print round(15.5)  # 16.0
# print round(16.5)  # 17.0
#
# Python 3
#
# print('Python', python_version())
# print(round(15.5))  # 16
# print(round(16.5))  # 16
