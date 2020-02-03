#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Napisz funkcję sum_div35(n), która zwraca sumę wszystkich liczb podzielnych
przez 3 lub 5 mniejszych niż n.
"""

def sum_div35(n):
    sum =0
    for i in range(n):                #sprawdzam w petli:
        if (i%3==0 or i%5==0):        #sprwdzam czy liczba jest podzielna przez 3 lub 5
            sum+=i                    #jesli tak to sumuje
    return sum

input = 100
#output = 2318


print(sum_div35(input))
