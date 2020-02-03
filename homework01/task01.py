#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Zad 2. Napisz funkcję even_elements zwracającą listę,
która zawiera tylko elementy z list o parzystych indeksach.
"""


#definicja funkcji
def even_elements(lista):
    result=[]
    for i in range(len(lista)):
        if (i % 2 == 0):          # modulo 2 - sprawdzenie parzystosci
            result.append(lista[i])  #dlaczenie do listy
    return result


#input = [1, 2, 3, 4, 5, 6]
#output = [1, 3, 5]

#wywolanie funkcji
input = [1, 2, 3, 4, 5, 6]
output = even_elements(input) #wywolanie funkcji i wynik przypisany do zmiennej
print(output)                 # "wydrul" wyniku na konsoli
