#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Napisz funkcję sum_from_one_to_n zwracającą sume liczb od 1 do n.
Jeśli podany argument jest mniejszy od 1 powinna być zwracana wartość 0.
"""
#definicja
def sum_from_one_to_n(n):
    sum=0
    if (n>=1):      # jesli > 1 przechodze do petli
        for i in range(n+1):
            sum+=i            #sumuje w petli
    else: sum=0  #w przeciwnym razie rowne 0
    return sum


input = 999
#output = 499500

#wywolanie
print(sum_from_one_to_n(input))