#!/usr/bin/env python
# -*- coding: utf-8 -*-


def lenstring(word):
    word = str(word)
    lenstr = len(word)
    return lenstr


def substring(word, length, letter):
    word = str(word)
    letter -= 1
    substr = word[letter:letter+length]
    return substr


def reverse(word):
    word = str(word)
    if lenstring(word) == 0:
        return ''
    else:
        a = substring(word, lenstring(word)-1, 1)
        b = substring(word, 1, lenstring(word))
        return b + reverse(a)
        
print(reverse('paulina'))
