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
# print dir(int)
# print dir(float)
# print dir(str)
# print dir(tuple)
# print dir(list)
# print dir(dict)
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
# print example_dict.items()  # list of dict's (key, value) tuple pairs
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
# SIMPLE LOOPS EXAMPLES
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
# '''General build-in methods and expressions like del, sum, len, sorted, print, pprint etc, yield, range, zip'''
# print 'To jest {0} i {1}'.format('first','second')
# print 'To jest %s i %s' % ('first', 'second')
# # w Pythonie 2.x. True może mieć przypisaną wartość False


# d = {1:'one',2:'two',3:'three'}
#
# # Creates a real list of tuples and returns that. Probably takes more memory and time initially but accessing
# each element is fast
# print 'Value : %s' %  d.items()
#
# # Returns a generator - object that 'creates' one item at a time every time next() is called on it. Probably takes
# less space and time initially, but a bit more time in generating each element.
# print 'Value : %s' %  d.iteritems()
#
# # In loop d.iteritems() and d.items() works the same way
# print 'd.items():'
# for k, v in d.items():
#     if d[k] is v: print '\tthey are the same object'
#     else: print '\tthey are different'
#
# print 'd.iteritems():'
# for k, v in d.iteritems():
#     if d[k] is v: print '\tthey are the same object'
#     else: print '\tthey are different'
#

# # *args = list of arguments
# # **kwargs = dictionary of arguments, in which keys = names of argument, values = values of argument
# # it is used when you are not sure how many named/unnamed arguments might be passed to your function
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
# table_things(apple = 'fruit', cabbage = 'vegetable')
#
# # list(iterable) - is one of built-in function, which returns a list whose items are the same and in the same order
# as iterable's items
# print list('michal')
#
# # enumerate(sequence, start=0) - is one of the built-in Python functions - it returns an enumerate object
# choices = ['pizza', 'pasta', 'salad', 'nachos']
# print enumerate(choices) # it prints nothing interesting for you
# print list(enumerate(choices, 2))
# for index, item in enumerate(choices, 1):
#     print index, item
#
#
#
#
# # Klasy w Pythonie:
# # - każda klasa, która nie dziedziczy po innej, powinna dziedziczyć po klasie object
# # - nie każda klasa musi mieć metodę __init__
#
# # list comprehension
#
# evens_to_50 = [i for i in range(51) if i % 2 == 0]
#
# # dict comprehension
#
# squares = {x: x**2 for x in [1,2,3,4,5]}
#
# # zip
#
# keys = ['a','b','c']
# values = [1,2,3]
# print zip(keys,values)
#
# dict_from_zip = {}
# for (k,v) in zip(keys, values):
#     dict_from_zip[k] = v
# print dict_from_zip
#
#
# # introspekcja kodu: dir, callable, getattr
#
# #
# dir
#
# # sprawdza czy jest wywoływalne?
# callable
#
# # wyciąga dany atrybut z obiektu?
# getattr
#
# # xrange - generator - wczytuje i zwraca po jednym elemencie z listy
# # range - iterator - wczytuje od razu całą listę
# # w Pythonie 3 jest tylko xrange
#
# # pylint - sprawdza powielające się zmienne, ich nazwy, funkcje itp. wyświetla jakość kodu w skali 1-10,
# # brakujące docstringi, białe znaki itp., hierarchia importów - podpowiada bo będzie bardziej czytelne
#
# # isort
# # coverage
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
#
#
# import string
#
# def alfabet():
#     litery = list(string.ascii_lowercase)
#     for i in litery:
#         print i
#
# alfabet()
#
# '''slicem żeby przechodzić co drugą literę'''
# def alfabet_2():
#     litery = list(string.ascii_lowercase)
#     for i in range(len(litery)):
#         if i % 2 == 0:
#             print litery[i]
#
# alfabet_2()
#
# '''można funkcją reverse'''
# def palindrom(a):
#     if a == a[::-1]:
#         print 'To jest palindrom'
#     else:
#         print 'To nie jest palindrom'
#
# palindrom('atata')
# palindrom('tonie')
#
# '''można było użyć funkcji filter'''
# def filtr(*args):
#     odfiltrowane = []
#     for i in args:
#         if i not in list(string.ascii_lowercase):
#             odfiltrowane.append(i)
#     print odfiltrowane
#
# filtr('a', 'c', 2, 5)
#
# '''Przy użyciu filter napisać funkcję, który z podanej listy odfiltrowuje
# wyrazy dłuższe niż n'''
#
# #def filtr_2(*args):
# #    odfiltrowane = []
# #    for i in args:
#
# to_100 = [i for i in range(0,101)]
# evens_to_100 = [i for i in range(0,101) if i % 2 == 0]
#
# print to_100
# print evens_to_100
#
# # liste liter alfabetu
# lista_liter = [i for i in string.ascii_lowercase]
# print lista_liter
#
# # slownik liter alfabetu z kluczami
#
# slownik = {i: ord(i) for i in string.ascii_lowercase}
#
# print slownik
#
# # odfiltrować krótsze niż 5
#
# lista_slow = ['michalem', 'michalowi', 'ani']
# shorts = [i for i in lista_slow if len(i) < 5]
#
# print shorts
#
# # list_c + lambda żeby kwadraty liczy od 1 do 50
#
# # lambdą i list comprehensions zrobić kwadraty od 1 do 50
# kwadrat = lambda x: x**2
# sqr_to_50 = [kwadrat(i) for i in range(51)]
# print sqr_to_50
#
# print map(lambda x: x**2, range(51)) # dla każdego argumentu z listy wykona się funkcja
#
#
# #def squares():
# #    x = 1
# #    while True:
# #        yield x
# #        yield x ** 2
# #        x = x + 1
# #
# #sq = squares()
# #for x in range(100):
# #   import pdb; pdb.set_track() # put pdb here ane step into functions
# #    print 'number %s' (sq.next())
# #    print 'number %s' (sq.next())
#
# # napisz generator zwracająćy n liczb ciągu F
#
# a,b = 0,1
# def fibI():
#     global a,b
#     while True:
#         yield a
#         a,b = b, a+b  # nie można tego rozbić na 2 linijki!!!!!!
#
# f=fibI()
# lista = []
# for i in range (10):
#     lista.append(f.next())
# print lista
#
# # następnie użyj list_c aby wypisać tylko parzyste
#
# parzyste = [i for i in lista if i % 2 == 0]
# print parzyste
#
# #print dir(str)
# #print getattr(str, 'upper')
# #print callable('find')
#
# # przefiltruj wywoływalne metody obiektu
# def atrybuty(obj):
#     atrybuty = dir(obj)
#     for i in atrybuty:
#         a = getattr(obj, str(i))
#         if callable(a) == True:
#             print i
#
# atrybuty(list)
#
# #Testy jednostkowe i asercja
# #
# #import unittest
# #
# #class MathTest(unittest, TestCase):
# #
# #    def test_add(self):
# #        self.assertEqual(2+3, 5)
# #
# # KLASY/METODY DO TESTOWANIA
#
#






# print 'This isn\'t flying, this is falling with style!'
# how_much = raw_input('How much whisky is he going to drink?')
# print 'I'm %s years old. I have %s litres of whisky... I'm going to drink %s \
# litres today!' % (my_int, my_float, how_much)







# '''Importowanie'''
# Kolejność importowania w Pythonie:
#   - biblioteki standardowe
#   - zewnętrzne frameworki/narzędzia
#   - lokalnie np. moduły naszej aplikacji
#
# import math
# from math import exp
# from math import *
# print math.sqrt(25)
#
# print exp(4)
# print sqrt(16)
#
# you can change the name of imported function
#
# from time import sleep as wait


# '''Comparators and booleans'''
#
# bool_1 = 3 < 5
# bool_2 = 5 < 4
# bool_3 = 5 == 5
# bool_4 = 5 != 2.5 * 2
# bool_5 = 5 >= 5
#
# print bool_1, bool_2, bool_3, bool_4, bool_5
#
# '''
# True and True is True
# True and False is False
# False and True is False
# False and False is False
#
# True or True is True
# True or False is True
# False or True is True
# False or False is False
#
# Not True is False
# Not False is True
#
# 'not' is evaluated first
# 'and' is evaluated next
# 'or' is evaluated last
#
# Parentheses () ensure your expressions are evaluated in the order you want.
# Anything in parentheses is evaluated as its own unit.
#
# '''
#
# bool_6 = (True or 7 > 6) and (not 6 ** 2 != 36) or (5 == 'Alpha')
#
# print bool_6
#
# '''Funkcje i instrukcja warunkowa if'''
#
#
# def greater_less_equal_5(answer):
#    if answer > 5:
#       return 1
#    elif answer < 5:
#       return -1
#    else:
#       return 0
#
#
# print greater_less_equal_5(4)
#
#
# def biggest_number(*args):
#    print max(args)
#    return max(args)
#
#
# def smallest_number(*args):
#    print min(args)
#    return min(args)
#
#
# def distance_from_zero(arg):
#    print abs(arg)
#    return abs(arg)
#
#
# biggest_number(-10, -5, 5, 10)
# smallest_number(-10, -5, 5, 10)
# distance_from_zero(-10)
#
#
# def hotel_cost(nights):
#    return 140 * nights
#
#
# def plane_ride_cost(city):
#    if city == 'Charlotte':
#       return 183
#    elif city == 'Tampa':
#       return 220
#    elif city == 'Pittsburgh':
#       return 222
#    elif city == 'Los Angeles':
#       return 475
#
#
# def rental_car_cost(days):
#    if days < 3:
#       return 40 * days
#    elif days >= 7:
#       return 40 * days - 50
#    elif days >= 3:
#       return 40 * days - 20
#
#
# def trip_cost(city, days, spending_money):
#    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money
#
#
# print trip_cost('Los Angeles', 5, 600)
#











# '''Dictionaries'''
#
# d = {'key1': 777, 'key2': 888, 'key3': [1, 4, 7, 11, 13]}
# print d['key1']
# d['key1'] = 'new1'
# d['key4'] = 'new2'
# del d['key2']
# print d
# print d['key3'][0]
# print d.items()
#
# '''Pętla for'''
#
# my_list = [1, 9, 3, 8, 5, 7]
# for number in my_list:
#    print 2 * number
#
# choices = ['pizza', 'pasta', 'salad', 'nachos']
# for index, item in enumerate(choices):
#    print index + 1, item
#
# list_a = [3, 9, 17, 15, 19]
# list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
# for a, b in zip(list_a, list_b):
#    if a > b:
#       print a
#    else:
#       print b
#
# grades = {
#    'Michal': 3.5,
#    'Piotr': 2.0,
#    'Filip': 5.0,
#    'Janusz': 4.5
# }
#
# for key in grades:
#    print key
#    print grades[key]
#
# word = 'Programming is fun!'
# for letter in word:
#    if letter not in ['o', 'a', 'i', 'u', 'y', 'e']:
#       print letter
#
#
# def digit_sum(n):
#    x = str(n)
#    suma = 0
#    for i in x:
#       suma = suma + int(i)
#    return suma
#
#
# def is_prime(x):
#    if x < 2:
#       return False
#    for n in range(2, x):
#       if x % n == 0:
#          return False
#    else:
#       return True
#
#
# '''Pętla while'''
#
# loop_condition = True
# while loop_condition:
#    print 'I am a loop, formally'
#    loop_condition = False
#
# import random
#
# print 'Lucky Numbers! 3 numbers will be generated.'
# print 'If one of them is a '5', you lose!'
# count = 0
# while count < 3:
#    num = random.randint(1, 6)
#    print num
#    if num == 5:
#       print 'Sorry, you lose!'
#       break
#    count += 1
# else:
#    print 'You win!'
#
# count = 0
# while True:
#    print count
#    count += 1
#    if count >= 10:
#       break
#
# guesses_left = 3
# while guesses_left > 0:
#    guess = int(raw_input('Your guess: '))
#    if guess == guesses_left:
#       print 'You win'
#       break
#    guesses_left = guesses_left - 1
# else:
#    print 'You lose'
#
# '''list comprehension - dobry sposób do generowania list'''
#
# evens_to_50 = [i for i in range(51) if i % 2 == 0]
#
# doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
#
# even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
#
# cubes_by_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0]
#
# threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]
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
