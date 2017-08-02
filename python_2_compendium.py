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







# w Pythonie 2.x. True może mieć przypisaną wartość False
# False - jest to 0, pusty słownik, None, pusta sekwencja np. string
# nie używać str, list, dict jako zmiennych

my_dict = {'key_1': 'value_1', 'key_2': 'value_2', 'key_3': 'value_3'}

# print my_dict.get('key_4') # nie wyrzuca wyjątków tylko None
# print my_dict['key_4']     # wyrzuca wyjątki

lista_extend = ['a', 'b', 'c', 1, 2, 3]
lista_append = ['a', 'b', 'c', 1, 2, 3]

lista_extend.extend([4, 5, 6])
lista_append.append([4, 5, 6])

print lista_extend
print lista_append

print "To jest {0} i {1}".format('first','second')
print "To jest %s i %s" % ('first', 'second')

d = {1:'one',2:'two',3:'three'}

# Creates a real list of tuples and returns that. Probably takes more memory and time initially but accessing each element is fast
print "Value : %s" %  d.items()

# Returns a generator - object that "creates" one item at a time every time next() is called on it. Probably takes less space and time initially, but a bit more time in generating each element.
print "Value : %s" %  d.iteritems()

# In loop d.iteritems() and d.items() works the same way
print 'd.items():'
for k, v in d.items():
    if d[k] is v: print '\tthey are the same object'
    else: print '\tthey are different'

print 'd.iteritems():'
for k, v in d.iteritems():
    if d[k] is v: print '\tthey are the same object'
    else: print '\tthey are different'

# Jednoelementowa tupla bez przecinka przyjmuje w Pythonie typ elementu znajdującego się wewnątrz

print type(('napis', ))
print type((12345, ))

print type(('napis'))
print type((12345))

# Mutability of Common Types. Some objects are mutable, meaning they can be altered and some are immutable.
# The following are immutable objects:
# - numeric types (int, float, complex)
# - string
# - tuple
# - frozen set
# - bytes
# The following objects are mutable:
# - list
# - dict
# - set
# - byte array
# Note that! What if I need a mutable string to do something like character swapping? Well then use a byte array!

# The data type "set" is a collection type, like list or tuple. A set contains an unordered collection of unique and immutable objects. It is like dictionary with no values.
# The data typ "frozenset" is like set except that it cannot be changed, i.e. it is immutable (so as you should remember it can be a dictionary key)

# 2 ways of creation a set
items_set = {"arrow", "spear", "arrow", "arrow", "rock"}
numbers_set = set([1, 2, 2, 3, 3, 4])
letters_set = set("A Python Tutorial")

print items_set
print len(items_set)
print type(items_set)

print numbers_set
print len(numbers_set)
print type(numbers_set)

print letters_set
print len(letters_set)
print type(letters_set)

# Use in and not-in keywords
if "rock" in items_set:
    print("Rock exists")

if "clock" not in items_set:
    print("Cloak not found")

# We can't create a set of mutable elements like lists
list_of_languages = ["Python","Perl"]
list_of_cities = ["Paris", "Berlin"]
# impossible_set = set((list_of_languages, list_of_cities))

# Examples of set operations

set_1 = {"red","green"}
set_1.add("yellow")
set_1.remove("red")
print set_1

set_2 = {"Stuttgart", "Konstanz", "Freiburg"}
set_2.clear()
print set_2

set_3 = {"a","b","c","d","e"}
set_4 = {"b","c"}
set_5 = {"c","d"}

print set_3.difference(set_4)
print set_3.difference(set_4).difference(set_5)

set_6 = {"a","b","c","d","e"}
set_7 = {"c","d"}
print set_6.issubset(set_7)
print set_7.issubset(set_6)
print set_6.issubset(set_6)
print set_6 > set_7
print set_7 < set_6
print set_6 < set_6
print set_7 <= set_6

set_8 = {"a","b","c","d","e"}
set_9 = {"c","d"}
print set_8.issuperset(set_9)
print set_9.issuperset(set_8)
print set_8.issuperset(set_8)
print set_8 > set_9
print set_8 >= set_9
print set_8 >= set_8
print set_8 > set_8

# 2 ways of creation a frozenset

list_to_frozen = ["bird", "plant", "fish"]
icecube = frozenset(list_to_frozen)
print(icecube)

# *args = list of arguments
# **kwargs = dictionary of arguments, in which keys = names of argument, values = values of argument
# it is used when you are not sure how many named/unnamed arguments might be passed to your function

def print_everything(*args):
    for count, thing in enumerate(args):
        print '{0}. {1}'.format(count, thing)

def table_things(**kwargs):
    for name, value in kwargs.items():
        print '{0} = {1}'.format(name, value)

print_everything('apple', 'banana', 'cabbage')
table_things(apple = 'fruit', cabbage = 'vegetable')

# list(iterable) - is one of built-in function, which returns a list whose items are the same and in the same order as iterable's items
print list('michal')

# enumerate(sequence, start=0) - is one of the built-in Python functions - it returns an enumerate object
choices = ['pizza', 'pasta', 'salad', 'nachos']
print enumerate(choices) # it prints nothing interesting for you
print list(enumerate(choices, 2))
for index, item in enumerate(choices, 1):
    print index, item




# Kolejność importowania w Pythonie:
#   - biblioteki standardowe
#   - zewnętrzne frameworki/narzędzia
#   - lokalnie np. moduły naszej aplikacji

# you can change the name of imported function

from time import sleep as wait

# Klasy w Pythonie:
# - każda klasa, która nie dziedziczy po innej, powinna dziedziczyć po klasie object
# - nie każda klasa musi mieć metodę __init__

# list comprehension

evens_to_50 = [i for i in range(51) if i % 2 == 0]

# dict comprehension

squares = {x: x**2 for x in [1,2,3,4,5]}

# zip

keys = ['a','b','c']
values = [1,2,3]
print zip(keys,values)

dict_from_zip = {}
for (k,v) in zip(keys, values):
    dict_from_zip[k] = v
print dict_from_zip


# introspekcja kodu: dir, callable, getattr

#
dir

# sprawdza czy jest wywoływalne?
callable

# wyciąga dany atrybut z obiektu?
getattr

# xrange - generator - wczytuje i zwraca po jednym elemencie z listy
# range - iterator - wczytuje od razu całą listę
# w Pythonie 3 jest tylko xrange

# pylint - sprawdza powielające się zmienne, ich nazwy, funkcje itp. wyświetla jakość kodu w skali 1-10,
# brakujące docstringi, białe znaki itp., hierarchia importów - podpowiada bo będzie bardziej czytelne

# isort
# coverage

"""do funkcji check_letter piszemy testy"""

import unittest

def check_letter(word, letter):
    if letter in word:
        return True
    else:
        return False

class Test1(unittest.TestCase):
    def test_letter(self):
        x = check_letter('michal', 'i')
        self.assertTrue(x)

if __name__ == '__main__':
    unittest.main()



import string

def alfabet():
    litery = list(string.ascii_lowercase)
    for i in litery:
        print i

alfabet()

"""slicem żeby przechodzić co drugą literę"""
def alfabet_2():
    litery = list(string.ascii_lowercase)
    for i in range(len(litery)):
        if i % 2 == 0:
            print litery[i]

alfabet_2()

"""można funkcją reverse"""
def palindrom(a):
    if a == a[::-1]:
        print "To jest palindrom"
    else:
        print "To nie jest palindrom"

palindrom('atata')
palindrom('tonie')

"""można było użyć funkcji filter"""
def filtr(*args):
    odfiltrowane = []
    for i in args:
        if i not in list(string.ascii_lowercase):
            odfiltrowane.append(i)
    print odfiltrowane

filtr('a', 'c', 2, 5)

"""Przy użyciu filter napisać funkcję, który z podanej listy odfiltrowuje
wyrazy dłuższe niż n"""

#def filtr_2(*args):
#    odfiltrowane = []
#    for i in args:

to_100 = [i for i in range(0,101)]
evens_to_100 = [i for i in range(0,101) if i % 2 == 0]

print to_100
print evens_to_100

# liste liter alfabetu
lista_liter = [i for i in string.ascii_lowercase]
print lista_liter

# slownik liter alfabetu z kluczami

slownik = {i: ord(i) for i in string.ascii_lowercase}

print slownik

# odfiltrować krótsze niż 5

lista_slow = ['michalem', 'michalowi', 'ani']
shorts = [i for i in lista_slow if len(i) < 5]

print shorts

# list_c + lambda żeby kwadraty liczy od 1 do 50

# lambdą i list comprehensions zrobić kwadraty od 1 do 50
kwadrat = lambda x: x**2
sqr_to_50 = [kwadrat(i) for i in range(51)]
print sqr_to_50

print map(lambda x: x**2, range(51)) # dla każdego argumentu z listy wykona się funkcja


#def squares():
#    x = 1
#    while True:
#        yield x
#        yield x ** 2
#        x = x + 1
#
#sq = squares()
#for x in range(100):
#   import pdb; pdb.set_track() # put pdb here ane step into functions
#    print "number %s" (sq.next())
#    print "number %s" (sq.next())

# napisz generator zwracająćy n liczb ciągu F

a,b = 0,1
def fibI():
    global a,b
    while True:
        yield a
        a,b = b, a+b  # nie można tego rozbić na 2 linijki!!!!!!

f=fibI()
lista = []
for i in range (10):
    lista.append(f.next())
print lista

# następnie użyj list_c aby wypisać tylko parzyste

parzyste = [i for i in lista if i % 2 == 0]
print parzyste

#print dir(str)
#print getattr(str, 'upper')
#print callable('find')

# przefiltruj wywoływalne metody obiektu
def atrybuty(obj):
    atrybuty = dir(obj)
    for i in atrybuty:
        a = getattr(obj, str(i))
        if callable(a) == True:
            print i

atrybuty(list)

#Testy jednostkowe i asercja
#
#import unittest
#
#class MathTest(unittest, TestCase):
#
#    def test_add(self):
#        self.assertEqual(2+3, 5)
#
# KLASY/METODY DO TESTOWANIA



# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""W ten sposób dodajemy dłuższe komentarze wielolinijkowe. Poniżej znajduje
się streszczenie najważniejszych zagadnień z kursu na codeacademy.com."""

# Krótkie komentarze jednolinijkowe dodajemy tak

"""Podstawowe typy i proste instrukcje"""

print "Welcome to Python!"
print 'Welcome to' + 'Python!'
print 'This isn\'t flying, this is falling with style!'

my_int = -10
my_int = abs(my_int)
my_int = 11 % 3
my_int = 7 ** 2
my_string = str(my_int)
my_int = int(my_string)
WAZNE = 5 / 2
print WAZNE
my_float = 9.23
my_bool = True
how_much = raw_input("How much whisky is he going to drink?")
zm1, zm2, zm3 = 1, 2, "john"

print "I'm %s years old. I have %s litres of whisky... I'm going to drink %s \
litres today!" % (my_int, my_float, how_much)

"""Stringi"""

napis = "Przykladowy string"
dwa_napisy = napis + " oraz kolejny string"
print dwa_napisy.split()
fifth_letter = napis[4]
a_few_letters = napis[0:5]
len(napis)
str(my_int)
napis.lower()
napis.upper()

"""Importowanie"""

from datetime import datetime

now = datetime.now()
print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour,
                             now.minute, now.second)

import math

print math.sqrt(25)

print dir(math)

from math import exp

print exp(4)

from math import *

print sqrt(16)

"""Comparators and booleans"""

bool_1 = 3 < 5
bool_2 = 5 < 4
bool_3 = 5 == 5
bool_4 = 5 != 2.5 * 2
bool_5 = 5 >= 5

print bool_1, bool_2, bool_3, bool_4, bool_5

"""
True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

'not' is evaluated first
'and' is evaluated next
'or' is evaluated last

Parentheses () ensure your expressions are evaluated in the order you want.
Anything in parentheses is evaluated as its own unit.

"""

bool_6 = (True or 7 > 6) and (not 6 ** 2 != 36) or (5 == "Alpha")

print bool_6

"""Funkcje i instrukcja warunkowa if"""


def greater_less_equal_5(answer):
   if answer > 5:
      return 1
   elif answer < 5:
      return -1
   else:
      return 0


print greater_less_equal_5(4)


def biggest_number(*args):
   print max(args)
   return max(args)


def smallest_number(*args):
   print min(args)
   return min(args)


def distance_from_zero(arg):
   print abs(arg)
   return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)


def hotel_cost(nights):
   return 140 * nights


def plane_ride_cost(city):
   if city == "Charlotte":
      return 183
   elif city == "Tampa":
      return 220
   elif city == "Pittsburgh":
      return 222
   elif city == "Los Angeles":
      return 475


def rental_car_cost(days):
   if days < 3:
      return 40 * days
   elif days >= 7:
      return 40 * days - 50
   elif days >= 3:
      return 40 * days - 20


def trip_cost(city, days, spending_money):
   return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money


print trip_cost("Los Angeles", 5, 600)

"""Listy"""

numbers = [8, 7, 6, 5, 'slowo', [3, 2, 1]]
suma_list = numbers + [11, 12, 13]
print sorted(numbers)
print sum(numbers[5])
print numbers[0] + numbers[2]
print numbers[1:3]
print numbers[2:]
print numbers[:2]
print numbers[::-1]
index = numbers.index(8)
print index
numbers.insert(index, "wrzutka")
print numbers
numbers.append([4, 5])
numbers.extend([200, 99])
numbers.remove(8)
print numbers
print len(numbers)
numbers.sort()
print numbers
del numbers[0]
letters = ['a', 'b', 'c', 'd']
print " ".join(letters)
print "---".join(letters)
ex_list = [4, 16, 17]
[cc, dd, ee] = ex_list
ff, gg, hh = ex_list
print cc, ff
print dd, gg
print ee, hh

range(6)  # => [0,1,2,3,4,5]
range(1, 6)  # => [1,2,3,4,5]
range(1, 6, 3)  # => [1,4]

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
list_c = zip(list_a, list_b)
print list_c

"""Dictionaries"""

d = {'key1': 777, 'key2': 888, 'key3': [1, 4, 7, 11, 13]}
print d['key1']
d['key1'] = 'new1'
d['key4'] = 'new2'
del d['key2']
print d
print d['key3'][0]
print d.items()

"""Pętla for"""

my_list = [1, 9, 3, 8, 5, 7]
for number in my_list:
   print 2 * number

choices = ['pizza', 'pasta', 'salad', 'nachos']
for index, item in enumerate(choices):
   print index + 1, item

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for a, b in zip(list_a, list_b):
   if a > b:
      print a
   else:
      print b

grades = {
   "Michal": 3.5,
   "Piotr": 2.0,
   "Filip": 5.0,
   "Janusz": 4.5
}

for key in grades:
   print key
   print grades[key]

word = "Programming is fun!"
for letter in word:
   if letter not in ['o', 'a', 'i', 'u', 'y', 'e']:
      print letter


def digit_sum(n):
   x = str(n)
   suma = 0
   for i in x:
      suma = suma + int(i)
   return suma


def is_prime(x):
   if x < 2:
      return False
   for n in range(2, x):
      if x % n == 0:
         return False
   else:
      return True


"""Pętla while"""

loop_condition = True
while loop_condition:
   print "I am a loop, formally"
   loop_condition = False

import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"
count = 0
while count < 3:
   num = random.randint(1, 6)
   print num
   if num == 5:
      print "Sorry, you lose!"
      break
   count += 1
else:
   print "You win!"

count = 0
while True:
   print count
   count += 1
   if count >= 10:
      break

guesses_left = 3
while guesses_left > 0:
   guess = int(raw_input("Your guess: "))
   if guess == guesses_left:
      print "You win"
      break
   guesses_left = guesses_left - 1
else:
   print "You lose"

"""list comprehension - dobry sposób do generowania list"""

evens_to_50 = [i for i in range(51) if i % 2 == 0]

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]

cubes_by_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0]

threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]

"""Anonymous function - gdy użyjemy razem funkcji filter oraz lambda, funkcja
filter użyji lambdy, aby określić co ma filtrować z listy"""

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)

squares = [x ** 2 for x in range(1, 11)]
print filter(lambda x: 30 < x < 70, squares)
