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
# 1 example: instance, class and static methods, instance and class variables
#
# class Counter(object):
#
#     # class variable shared by all instances, accessible only for class
#     cls_var = 0
#
#     def __init__(self, ins_val=0):
#         # instance variable unique to each instance, accessible only for instance (for all instance methods)
#         self.ins_val = ins_val
#
#     # instance method, can be invoked by instance object and instance is passed as a first argument
#     def ins_add(self, number=1):
#         # can access instance variables, like ins_val
#         # cannot access class variables, like cls_var (can access cls_var but in relation to specific instance)
#         self.ins_val = self.ins_val + self.cls_var + number
#         return self.ins_val
#
#     # class method, can be invoked by class name or instance object and class is passed as a first argument
#     @classmethod
#     def cls_add(cls, number):
#         # can access class variables, like cls_var
#         # cannot access instance variables, like ins_val
#         cls.cls_var = cls.cls_var + number
#         return cls.cls_var
#
#     # static method, can be invoked by class name or instance object - has no interaction with instance or class,
#     # technically it is a common function that is only placed inside class instead of in the global namespace
#     @staticmethod
#     def stc_print(string):
#         # cannot access class variables, like cls_var
#         # cannot access instance variables, like ins_val
#         return string
#
# counter_1 = Counter(0)  # first instance of Counter
# counter_2 = Counter(0)  # second instance of Counter
#
# print dir(counter_1)  # contains 'cls_add', 'cls_var', 'ins_add', 'ins_val', 'stc_print'
# print dir(counter_2)  # contains 'cls_add', 'cls_var', 'ins_add', 'ins_val', 'stc_print'
# print dir(Counter)  # contains 'cls_add', 'cls_var', 'ins_add', 'stc_print'
#
# checking accessibility of cls_var
#
# counter_1.cls_var = 1  # change value of cls_var, but only for first instance
# counter_2.cls_var = 1  # change value of cls_var, but only for second instance
# Counter.cls_var = 1  # change value of cls_var for all instances
#
# print counter_1.cls_var  # value for first instance
# print counter_2.cls_var  # value for second instance
# print Counter.cls_var  # value for class
#
# checking accessibility of ins_val
#
# print counter_1.ins_val  # value for first instance
# print counter_2.ins_val  # value for first instance
#
# checking accessibility of ins_add
#
# print counter_1.ins_add(3)  # change value of ins_val for first instance
# print counter_2.ins_add(3)  # change value of ins_val for second instance
# print Counter.ins_add(counter_2, 3)  # change value of ins_val for second (Counter instance as first argument)
#
# checking accessibility of cls_add
#
# print counter_1.cls_add(3)  # change value of cls_var for all instances (because cls.cls_var is returned)
# print counter_2.cls_add(3)  # change value of cls_var for all instances (because cls.cls_var is returned)
# print Counter.cls_add(3)  # change value of cls_var for all instances (because cls.cls_var is returned)
#
# checking accessibility of stc_print
#
# print counter_1.stc_print('static method')
# print counter_2.stc_print('static method')
# print Counter.stc_print('static method')
#
# 2 example: global and local variables
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
#
# 3 example: new style and old style classes
#
# class OldStyle():
#     pass
#
# class NewStyle(object):
#     pass
#
# old = OldStyle()
# new = NewStyle()
#
# In the old style classes (up to Python 2.1. the only available kind of class) a user defined classes are objects of
# the type 'classobj' and each instance of any class is an object of type 'instance'.
#
# print type(OldStyle)  # <type 'classobj'>
# print type(old)  # <type 'instance'>
# print old  # <__main__.OldStyle instance at 0x7f211dad67a0>
#
# In the new style classes (introduced in Python 2.2 to unify the concepts of class and type) a user defined classes are
# actually new type objects (their type is 'type', not 'classobj') and when you create instances of them, the type() of
# each instance is the class object, so objects of different user-defined classes have distinct types and classes are on
# basically the same footing as all builtin types.
#
# print type(NewStyle)  # <type 'type'> like for e.q. type(int)
# print type(new)  # <class '__main__.NewStyle'>
# print new  # <__main__.NewStyle object at 0x7f211dbc4450>
#
# With old classes there is a separate structure for instance->class and object->type and new classes use object->type
# for both.
#
# 4 example: static methods
#
# class WithStatics(object):
#
#     # Static methods are often used as alternate constructors
#     @staticmethod
#     def default_with_statics():
#         return WithStatics()
#
#     def defined_other_way():
#         return 'defined_other_way method'
#     defined_other_way = staticmethod(defined_other_way)
#
# instance = WithStatics.default_with_statics()
# print instance.defined_other_way()
#
# 5 example: private methods
#
# Pycharm will not suggest using private methods from one module in other module.
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
#     def full_computer_ability(self, number):
#         print 'Computer named {} will show its power!'.format(self.name)
#         print self._power_of_2(number)
#         print self.__power_of_3(number)
#
# PC = Computer('Lenovo')
# PC.full_computer_ability(5)
#
# 6 example: inheritance
#
# class Customer(object):
#
#     def __init__(self, customer_id):
#         self.customer_id = customer_id
#
#     def display_cart(self):
#         print "I'm a string that stands in for the contents of your shopping cart!"
#
# class ReturningCustomer(Customer):
#
#     def display_order_history(self):
#         print "I'm a string that stands in for your order history!"
#
# monty_python = ReturningCustomer("ID: 12345")
# monty_python.display_cart()
# monty_python.display_order_history()
#
# 7 example: inheritance and private attributes
#
# To avoid naming conflict, if attributes of parent and child classes have the same names, '__' is used. All attributes
# names which starts with '__' are translated to new names '_ClassName__AttributeName'.
#
# class Parent(object):
#
#     amount = 0
#
#     def __init__(self):
#         self.__amount = 120
#
# class Child(Parent):
#
#     def __init__(self):
#         super(Child, self).__init__()
#         self.__amount = 10
#
# p = Child()
# print p._Parent__amount  # Pycharm does not recognize it, but is printed
# print p._Child__amount  # Pycharm does not recognize it, but is printed
#
# 8 example: overriding
#
# class Employee(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def greet(self, other):
#         print "Hello, %s" % other.name
#
# class CEO(Employee):
#
#     def greet(self, other):
#         print "Get back to work, %s!" % other.name
#
# ceo = CEO("Emily")
# emp = Employee("Steve")
# emp.greet(ceo)  # Hello, Emily
# ceo.greet(emp)  # Get back to work, Steve!
#
# 9 example: __repr__ method
#
# class Point3D(object):
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __repr__(self):  # return a string containing a printable representation of an object
#         return "(%d, %d, %d)" % (self.x, self.y, self.z)
#
# my_point = Point3D(1, 2, 3)
#
# print my_point
#
# 10 example: property() as decorator
#
# class property([fget[, fset[, fdel[, doc]]]]) - returns a property attribute for new-style classes (classes that
# derive from object):
#
#     - fget is a function for getting an attribute value
#     - fset is a function for setting an attribute value
#     - fdel is a function for deleting an attribute value
#     - doc creates a docstring for the attribute.
#
# A typical use is to define a managed attribute x:
#
# class C(object):
#     def __init__(self):
#         self._x = 0
#
#     def getx(self):
#         """Getx method."""
#         return self._x
#
#     def setx(self, value):
#         self._x = value
#
#     def delx(self):
#         del self._x
#
#     x = property(getx, setx, delx, "I'm the 'x' property.")
#
# print C.x.__doc__  # if given, returns property's docstring, otherwise returns fget’s docstring
# c = C()
# print c.x  # will invoke the getter
# c.x = 50  # will invoke the setter
# del c.x  # will invoke the deleter
#
# A property object has getter, setter, and deleter methods usable as decorators that create a copy of the property with
# the corresponding accessor function set to the decorated function. This is best explained with an example that is
# exactly equivalent to the first example.
#
# class C(object):
#     def __init__(self):
#         self._x = None
#
#     @property
#     def x(self):
#         """I'm the 'x' property."""
#         return self._x
#
#     @x.setter
#     def x(self, value):
#         self._x = value
#
#     @x.deleter
#     def x(self):
#         del self._x
#
# print C.x.__doc__
# c = C()
# print c.x
# c.x = 50
# del c.x
