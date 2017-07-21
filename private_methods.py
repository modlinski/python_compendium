#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pycharm would not suggest using private methods from one module in other module
"""
from time import sleep


class Computer(object):

    def __init__(self, name):
        self.name = name

    # private method - only for module
    @staticmethod
    def _power_of_2(number):
        return number**2

    # private method - only for class
    @staticmethod
    def __power_of_3(number):
        return number**3

    @staticmethod
    def __power_of_4(number):
        return number**4

    def return_name(self):
        return self.name

    def full_computer_ability(self, number):
        print 'Computer named {} will show its power!'.format(self.name)
        sleep(2)
        print self._power_of_2(number)
        print self.__power_of_3(number)
        print self.__power_of_4(number)

PC = Computer('Lenovo')
PC.full_computer_ability(5)
