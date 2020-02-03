#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Napisz funkcję char_sum, która dla zadanego łańcucha zwraca
sumę kodów ASCII znaków. Wykorzystaj funkcję ord()
"""

def char_sum(text):
    sum=0
    temp = list(text)  # dziele na znaki i zapisuje do listy

    for item in temp:
        sum+=ord(item)  #w petli konwertuje znaki do kodow ASCII i sumuje
    return sum

input = "this is a string"
#output = 1516

print(char_sum(input))

