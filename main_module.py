# #!/usr/bin/env python
# # encoding: utf-8
#
# # 'return' exits the current function/method and return None
# # 'pass' is a null operation and allows execution to continue at the next statement
#
# # if this is True we return/end the function
#
#
# def both():
#     """Executes both blocks."""
#     if True:
#         print 'First sentence'
#         pass
#     if True:
#         print 'Second sentence'
#         pass
#
#
# def first():
#     """Executes only the first block."""
#     if True:
#         print 'First sentence'
#         return
#     if True:
#         print 'Second sentence'
#         return
#
# both()
# first()
#
#
# def KelvinToFahrenheit(Temperature):
#     assert (Temperature >= 0), 'Colder than absolute zero!'
#     return ((Temperature-273)*1.8)+32
#
# print KelvinToFahrenheit(273)
# print int(KelvinToFahrenheit(505.78))
# # print KelvinToFahrenheit(-5)
#
# # In object-oriented programming, the decorator pattern (also known as Wrapper, an alternative naming shared with
# # the Adapter pattern) is a design pattern that allows behavior to be added to an individual object, either statically
# # or dynamically, without affecting the behavior of other objects from the same class. The decorator pattern is
# # often useful for adhering to the Single Responsibility Principle, as it allows functionality to be divided between
# # classes with unique areas of concern.
# # The "decorators" we talk about with concern to Python are not exactly the same thing as the DecoratorPattern described
# # above. A Python decorator is a specific change to the Python syntax that allows us to more conveniently alter
# # functions and methods (and possibly classes in a future version). This supports more readable applications of the
# # DecoratorPattern but also other uses as well.
#
# # 3 kinds of methods in Python: instance methods, static methods, class methods. Obiekty mają 3 rodzaje metod w Pythonie
# # - domyślne są metody instancyjne (charakterystyczne jest 'self' reprezentuje instancję obiektu, na rzecz której
# # wywoływana jest metoda).
#
#
# class Counter(object):
#     def __init__(self, value=0):
#         self.value = value
#
#     def increment(self, add=1):
#         self.value += add
#
#     @staticmethod
#     def string_number(num):
#         return 'Staticmethod ' + str(num)
#
#     # @classmethod
#     # def from_other(cls, number):
#     #     return cls(counter._value)
#
# print Counter.string_number(9)
# print Counter().string_number(9)


class A(object):
    def __init__(self):
        print "I'm class A"

class B(object):
    def __init__(self):
        print "I'm class B"

    def test(self):
        print 'B'

class C(A, B):
    def __init__(self):
        super(C, self).__init__()
        B.__init__(self)
        print "I'm class C"

    def test(self):
        super(C, self).test()
        print 'C'

c = C()
c.test()
