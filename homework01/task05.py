#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Napisz funkcję euclidean_distance obliczającą odległość między
dwoma punktami przestrzeni trójwymiarowej. Punkty są dane jako
trzyelementowe listy liczb zmiennoprzecinkowych.
np. odległość pomiędzy punktami (0, 0, 0) i (3, 4, 0) jest równa 5.
"""

#rozwiazanie
#wzor naodeglosc 2 punktow :
#d= sqrt([x2-x1]^2 + [y2-y1]^2 + [z2-z1]^2)


import math
def euclidean_distance(x, y):

    return math.sqrt((y[0]-x[0])**2+(y[1]-x[1])**2+(y[2]-x[2])**2)


input  = [[2.3, 4.3, -7.5], [2.3, 8.5, -7.5]]
input2 = [[0, 0, 0], [3, 4, 0]]
#output = 4.2
#wywolanie funkcji
output = euclidean_distance(input[0],input[1])
print(output)

output2 = euclidean_distance(input2[0],input2[1])
print(output2)



