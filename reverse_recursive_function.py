#!/usr/bin/env python
# -*- coding: utf-8 -*-


def len_string(word):
    word = str(word)
    len_str = len(word)
    return len_str


def substring(word, length, letter):
    word = str(word)
    letter -= 1
    sub_str = word[letter:letter+length]
    return sub_str


def reverse(word):
    word = str(word)
    if len_string(word) == 0:
        return ''
    else:
        a = substring(word, len_string(word)-1, 1)
        b = substring(word, 1, len_string(word))
        return b + reverse(a)
        
print(reverse('paulina'))
