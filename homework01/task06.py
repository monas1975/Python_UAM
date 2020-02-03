#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Napisz funkcję big_no zwracającej tzw. "Big 'NO!'"
(zob. http://tvtropes.org/pmwiki/pmwiki.php/Main/BigNo)
dla zadanej liczby tj. napis typu "NOOOOOOOOOOOOO!", gdzie liczba 'O' ma być
równa podanemu argumentem, przy czym jeśli argument jest mniejszy niż 5,
ma być zwracany napis "It's not a Big 'No!'".
"""

def big_no(n):
    temp=""
    if (n<5):       #sprawdzam czy mniejsze od 5
        text = "It's not a Big 'No!'"
    else:
        for i in range(n):  # w przeciwnym razie przechodze do petli
            temp+="O"         #"sklejam "O"
            text="N"+temp+"!"
    return text


input = 2
#output = "It's not a Big 'No!'"

print(big_no(2))
print(big_no(5))
print(big_no(50))
