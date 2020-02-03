#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Napisz funkcję days_in_year zwracającą liczbę dni w roku (365 albo 366).
"""

# Formalnie sprawdzenie czy dany rok jest rokiem przestępnym możemy zapisać następująco:
# ((rok mod 4 = 0) and (rok mod 100 <> 0)) or (rok mod 400 = 0)

#Rozwiazanie

#definicja funkcji
def days_in_year(year):
    if ((year%4==0 and year%100 !=0) or (year%400==0)):  #sprawdzanie przystepnosci roku
        amount_of_days = 366
    else:
        amount_of_days = 365
    return amount_of_days

#wywolanie
input = 2019
#output = 365

output = days_in_year(input) #wywloani funkcji i przypisanie do zmiennej
print(output)                #wypisanie na konsoli

for i in range(1999,2020):   #sprawdzam w petli 20 lat
    print("rok: ",i,"ma ",days_in_year(i)," dni")