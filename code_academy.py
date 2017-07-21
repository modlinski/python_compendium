#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""W ten sposób dodajemy dłuższe komentarze wielolinijkowe. Poniżej znajduje
się streszczenie najważniejszych zagadnień z kursu na codeacademy.com."""

#Krótkie komentarze jednolinijkowe dodajemy tak

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
WAZNE = 5/2
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
bool_4 = 5 != 2.5*2
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

bool_6 = (True or 7 > 6) and (not 6**2 != 36) or (5 == "Alpha")

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
    return 140*nights

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
        return 40*days
    elif days >= 7:
        return 40*days-50
    elif days >= 3:
        return 40*days-20
        
def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money
    
print trip_cost("Los Angeles", 5, 600)

"""Listy"""

numbers = [8, 7, 6, 5, 'slowo', [3, 2, 1]]
suma_list = numbers + [11, 12, 13]
print sorted(numbers)
print sum(numbers[5])
print numbers[0]+numbers[2]
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

range(6) # => [0,1,2,3,4,5]
range(1,6) # => [1,2,3,4,5]
range(1,6,3) # => [1,4]

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
list_c = zip(list_a, list_b)
print list_c

"""Dictionaries"""

d = {'key1' : 777, 'key2' : 888, 'key3' : [1, 4, 7, 11, 13]}
print d['key1']
d['key1'] = 'new1'
d['key4'] = 'new2'
del d['key2']
print d
print d['key3'][0]
print d.items()

"""Pętla for"""

my_list = [1,9,3,8,5,7]
for number in my_list:
    print 2*number

choices = ['pizza', 'pasta', 'salad', 'nachos']
for index, item in enumerate(choices):
    print index+1, item

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for a, b in zip(list_a, list_b):
    if a > b:
        print a
    else:
        print b

grades = {
    "Michal" : 3.5,
    "Piotr" : 2.0,
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
    for n in range(2,x):
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

doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]

even_squares = [x**2 for x in range (1,11) if x%2 == 0]

cubes_by_four = [x**3 for x in range(1,11)  if (x**3)%4==0]

threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]

"""Anonymous function - gdy użyjemy razem funkcji filter oraz lambda, funkcja 
filter użyji lambdy, aby określić co ma filtrować z listy"""

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)

squares = [x**2 for x in range(1,11)]
print filter(lambda x: 30 < x < 70, squares)
