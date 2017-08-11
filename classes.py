#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python is a language supporting various programming paradigms:
#     - object oriented programming,
#     - imperative programming,
#     - functional programming (to a lesser extent).
#
# Python is dynamically typed, which means that variables does not have types assigned statically, before program
# execution. Type of variable is a consequence of the value that is stored by variable. It makes operations on variables
# easier, but on the other hand makes control of the integrity harder. Variable can have different type in various
# moments of program execution.
#
# Object oriented programming (OOP) based on connecting data and behaviours and closing them in something that is called
# object. Functions of objects are called methods. For example after using:
#
# len("Python")
#
# Python checks if string object "Python" has length and if has than returns value related to this attribute. For
# example after using:
#
# my_dict.items()
#
# Python checks if my_dict has method item() and if has than execute them. What does cause that "Python" is a string and
# my_dict is a dictionary? The reason is that they are instances of classes str and dict. Class is a way of organizing
# and producing objects with similar attributes (fields and methods).
#
# Class can (but it is not obligatory) contain first methods named __init__(), which is used to initialize objects, that
# are created by class. __init__(), like all instance methods, takes at least one argument, which refers to the created
# instance object for which method is called. According to the convention this argument should be named 'self' and
# should be the first from all arguments. We can say that 'self' gives identity to the object. Next arguments (e.q.
# parameter_1, parameter_2) of __init__() and the rest of the instance methods should be assigned in methods bodies to
# variables with prefix self (e.q. self.parameter_1, self.parameter_2). It causes that during creating instance object
# of the class, variables will be related to the created instance. More about methods and variables of Python classes
# is in examples below.
#
# Inheritance is a process which allows one class to have attributes of other classes. This is a relationship like:
# 'square is an rectangle'. All classes that do not inherit from any other class, should inherit from 'object' class.
#
# 1 example: global and local variables
#
# var = 1
#
# class ClassWithLocal(object):  # according to the convention the names of classes should use PascalCase convention
#
#     def __init__(self, num):
#         self.num = num
#
#     def function_with_local(self):
#         var = 2 * self.num  # new local var
#         return var
#
# ClassWithLocal(2).function_with_local()
# print var
#
# class ClassWithGlobal(object):
#
#     def __init__(self, num):
#         self.num = num
#
#     def function_with_global(self):
#         global var
#         var = 2 * self.num  # changes the value of the global var
#         return var
#
# ClassWithGlobal(2).function_with_global()
# print var









# FINISH HERE
# metaclass
# @staticmethod


# 2 example: instance and class methods, instance and class variables


class Counter(object):

    counter_results = {}  # class variable shared by all instances, accessible only for class
    x = 0

    def __init__(self, value=0):
        self.value = value  # instance variable unique to each instance, accessible only for instance

    def increment(self, add=1):  # instance method, accessible only for instance -
        self.value += add
        x += 1
        return self.value

    @classmethod  # class method, accessible only for class
    def class_number(cls, number):
        return number

counter_1 = Counter(0)
counter_2 = Counter(0)
counter_1.increment(3)
counter_2.increment(3)
counter_1
counter_2


# my_counter = Counter()

# print Counter.increment()
# print Counter.string_number(9)
# print Counter.class_number(5)
# print my_counter.increment()
# print my_counter.string_number(9)
# print my_counter.class_number(5)


# print Counter.class_variable
# print Counter.class_variable
# print Counter.class_variable
# print my_counter.class_variable
# print my_counter.class_variable
# print my_counter.class_variable


# class A(object):
#     def __init__(self):
#         print "I'm class A"
#
# class B(object):
#     def __init__(self):
#         print "I'm class B"
#
#     def test(self):
#         print 'B'
#
# class C(A, B):
#     def __init__(self):
#         super(C, self).__init__()
#         B.__init__(self)
#         print "I'm class C"
#
#     def test(self):
#         super(C, self).test()
#         print 'C'
#
# c = C()
# c.test()


#
# """
# Pycharm would not suggest using private methods from one module in other module
# """
# from time import sleep
#
# class Computer(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     # private method - only for module
#     @staticmethod
#     def _power_of_2(number):
#         return number**2
#
#     # private method - only for class
#     @staticmethod
#     def __power_of_3(number):
#         return number**3
#
#     @staticmethod
#     def __power_of_4(number):
#         return number**4
#
#     def return_name(self):
#         return self.name
#
#     def full_computer_ability(self, number):
#         print 'Computer named {} will show its power!'.format(self.name)
#         sleep(2)
#         print self._power_of_2(number)
#         print self.__power_of_3(number)
#         print self.__power_of_4(number)
#
# PC = Computer('Lenovo')
# PC.full_computer_ability(5)















# """Przykład 1. Każde konkretne zwierze ma własne imię (bo jest inicjalizowane
# indywidualnie). Ich imiona są to instance variables. Ale każde zwierze ma dostęp
# do member variable is_alive, bo wszystkie one są członami klasy Animal. Klasa
# Animal dziedziczy po wbudowanej klasie object."""
#
#
# class AnimalProducer(object):
#     is_alive = True
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# zebra = Animal("Jeffrey", 2)
# giraffe = Animal("Bruce", 1)
# panda = Animal("Chad", 7)
#
# print zebra.name, zebra.age, zebra.is_alive
# print giraffe.name, giraffe.age, giraffe.is_alive
# print panda.name, panda.age, panda.is_alive
#
# """Przykład 2."""
#
# class Koszyk(object):
# 	def __init__ (self, login):
# 		self.koszyk = []
# 		self.login = login
# 	def dodaj(self,obiekt):
# 		self.koszyk.append(obiekt)
# 	def rozmiar(self):
# 		return len(self.koszyk)
#
# a = Koszyk('cyryl')
# print a
# a.dodaj(1)
# a.dodaj(2)
# a.dodaj('A')
# a.dodaj('B')
# a.atrybut = 3
#
# print a.rozmiar()
# print Koszyk('gustaw').rozmiar()
#
# print a.__dict__
# print dir(a)
#
# """Przykład 3. Dziedziczenie."""
#
# class Customer(object):
#     """Produces objects that represent customers."""
#     def __init__(self, customer_id):
#         self.customer_id = customer_id
#
#     def display_cart(self):
#         print "I'm a string that stands in for the contents of your shopping cart!"
#
# class ReturningCustomer(Customer):
#     """For customers of the repeat variety."""
#     def display_order_history(self):
#         print "I'm a string that stands in for your order history!"
#
# monty_python = ReturningCustomer("ID: 12345")
# monty_python.display_cart()
# monty_python.display_order_history()
#
# """Przykład 4. Dziedziczenie."""
#
# class Produkt1(object):
# 	ilosc = 0
# 	def ustaw_ilosc(self, ilosc):
# 		self.ilosc = ilosc
#
# class Pomidor1(Produkt1):
# 	opis = u'Pomidory krojone z bazylią'
#
# p = Pomidor1()
# p.ustaw_ilosc(80)
# print p.ilosc
# print p.opis
#
# """Przykład 5 - należy pamiętać, że podczas inicjalizowania instancji klasy
# pochodnej nie jest wywoływana metoda __init__ klasy bazowej. Jeżeli musimy
# wykonać tę metodę wystarczy skorzystać ze składni pokazanej poniżej."""
#
# class Produkt2:
# 	ilosc = 0
# 	def __init__(self):
# 		self.ilosc = 120
# 	def ustaw_ilosc(self, ilosc):
# 		self.ilosc = ilosc
#
# class Pomidor2(Produkt2):
# 	def __init__(self):
# 		Produkt2.__init__(self)
# 	opis = u'Pomidory krojone z bazylią'
#
# p = Pomidor2()
# print p.ilosc
# print p.opis
#
# """Przykład 6 - ukrywanie danych. Domyślnie wszystkie atrybuty są "publiczne" i
# dostępne są bez ograniczeń. Czasami, np. w przypadku dziedziczenia, może dojść
# do konfliktu nazw. By temu zaradzić wszystkie nazwy atrybutów zaczynających się
# od "__" przekształcane są na nowe nazwy o postaci: _NazwaKlasy__NazwaAtrybutu.
# W przykładzie atrybut "ilosc" występuje w obu klasach i zastosowanie "__"
# uchroniło nas przed nadpisaniem atrybutu/wartości z klasy bazowej."""
#
# class Produkt3:
# 	__ilosc = 0
# 	def __init__(self):
# 		self.__ilosc = 120
# 	def ustaw_ilosc(self, ilosc):
# 		self.__ilosc = ilosc
#
# class Pomidor3(Produkt3):
# 	def __init__(self):
# 		Produkt3.__init__(self)
# 		self.ilosc = 10
# 	opis = u'Pomidory krojone z bazylią'
#
# p = Pomidor3()
# print p._Produkt3__ilosc
# print p.ilosc
# print p.opis
#
# """Przykład 7. Wszystkie definicje są typu "ClassType", a wszystkie instancje
# "InstanceType". Aby sprawdzić przynależność obiektu do jakiejś klasy można użyć
# funkcji isinstance(obiekt,klasa), która zwróci wartość True jeżeli "obiekt" należy
# do "klasy". Funkcja issubclass(A,B) zwróci wartość True, jeżeli klasa A jest
# podklasą klasy B."""
#
# print isinstance(p,Pomidor3)
# print issubclass(Pomidor3,Produkt2)
#
# """Przykład 8. Przeważanie/nadpisywanie (override) - czasami chcemy nie tylko
# przejąć przez klasę pochodną od klasy podstawowej jakieś atrybuty, ale również
# nadpisać je. Na przykład ElectricCar jest bardziej wyspecjalizowaną klasą niż Car,
# więc możemy dać ElectricCar jego własną metodę drive_car(), która będzie inna niż
# oryginalna metoda klasy Car."""
#
# class Car(object):
#     condition = "new"
#     def __init__(self, model, color, mpg):
#         self.model = model
#         self.color = color
#         self.mpg = mpg
#     def display_car(self):
#         return "This is a %s %s with %s MPG." % (self.color, self.model, self.mpg)
#     def drive_car(self):
#         self.condition = "used"
#
# my_car = Car("DeLorean", "silver", 88)
# print my_car.condition
# my_car.drive_car()
# print my_car.condition
#
# class ElectricCar(Car):
#     def __init__(self, model, color, mpg, battery_type):
#         self.model = model
#         self.color = color
#         self.mpg = mpg
#         self.battery_type = battery_type
#     def drive_car(self):
#         self.condition = "like new"
#
# my_car = ElectricCar("Audi", "Green", 99, "molten salt")
# print my_car.condition
# my_car.drive_car()
# print my_car.condition
#
# """Przykład 9. Przeważanie/nadpisywanie (override)"""
#
# class Employee(object):
#     def __init__(self, name):
#         self.name = name
#     def greet(self, other):
#         print "Hello, %s" % other.name
#
# class CEO(Employee):
#     def greet(self, other):
#         print "Get back to work, %s!" % other.name
#
# ceo = CEO("Emily")
# emp = Employee("Steve")
# emp.greet(ceo)
# ceo.greet(emp)
#
# """Przykład 10. Przeważanie/nadpisywanie (override)"""
#
# class Employee(object):
#     """Models real-life employees!"""
#     def __init__(self, employee_name):
#         self.employee_name = employee_name
#
#     def calculate_wage(self, hours):
#         self.hours = hours
#         return hours * 20.00
#
# class PartTimeEmployee(Employee):
#     def calculate_wage(self, hours):
#         self.hours = hours
#         return hours * 12.00
#     def full_time_wage(self, hours):
#         return super(PartTimeEmployee, self).calculate_wage(hours)
#
# milton = PartTimeEmployee("Michal")
# print milton.full_time_wage(10)
#
# """Przykład 11. Jedną z użytycznych metod specjalnych jest wbudowana metoda
# __repr__(). Poprzez zapewnienie tej metodzie wartości zwrotnej, możemy powiedziecieć
# Pythonowi jak reprezentować dany object naszej klasy (na przykład, gdy używamy
# komendy print)"""
#
# class Point3D(object):
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#     def __repr__(self):
#         return "(%d, %d, %d)" % (self.x, self.y, self.z)
#
# my_point = Point3D(1, 2, 3)
#
# print my_point
#
# """Przykład 12. Mały program napisany klasami"""
#
# class SchoolMember:
#     '''Reprezentuje człowieka związanego z uczelnią.'''
#     def __init__(self, imie, wiek):
#         self.imie = imie
#         self.wiek = wiek
#         print '(Inicjalizacja SchoolMember: %s)' % self.imie
#
#     def powiedz(self):
#         '''Opowiedz o sobie.'''
#         print u'Imię:"%s" Wiek:"%s"' % (self.imie, self.wiek),
#
# class Wykladowca(SchoolMember):
#     '''Reprezentuje wykładowcę.'''
#     def __init__(self, imie, wiek, pensja):
#         SchoolMember.__init__(self, imie, wiek)
#         self.pensja = pensja
#         print '(Inicjalizacja Wykladowcy: %s)' % self.imie
#
#     def powiedz(self):
#         SchoolMember.powiedz(self)
#         print 'Pensja: "%d"' % self.pensja
#
# class Student(SchoolMember):
#     '''Reprezentuje studenta.'''
#     def __init__(self, imie, wiek, oceny):
#         SchoolMember.__init__(self, imie, wiek)
#         self.oceny = oceny
#         print '(Inicjalizacja Studenta: %s)' % self.imie
#
#     def powiedz(self):
#         SchoolMember.powiedz(self)
#         print 'Oceny: "%d"' % self.oceny
#
# w = Wykladowca('Mrs. Shrividya', 40, 30000)
# s = Student('Swaroop', 25, 75)
#
# print # wypisuje pustą linię
#
# osoby = [w, s]
# for osoba in osoby:
#     osoba.powiedz() # działa zarówno dla Wykładowców, jak i Studentów
