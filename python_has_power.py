#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
