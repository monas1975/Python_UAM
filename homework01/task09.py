#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Napisz funkcję leet_speak, która podmienia w podanym napisie niektóre litery
na podobnie wyglądające cyfry: 'e' na '3', 'l' na '1', 'o' na '0', 't' na '7'.
Np. leet('leet') powinno zwrócić '1337'.
"""


def leet_speak(text):
    tempList =[]
    toReplaceVocab = [['e','3'],['l','1'],['O','0'],['t','7']] #tworze slownik

    for item in toReplaceVocab:    # w petli przechodze przez slownik
        #print(item)
        tempList = item            #zmiennna item przypisuje do zmiennej tymczasowej
        text=text.replace(tempList[0],tempList[1])  #wyszukuje znak i zamieniam

    return text

#wywolanie funkcji:
input = 'leet'
input2 = 'teelleet'
print("to jest:  ",leet_speak(input2))
print("to jest:  ",leet_speak(input))
#output = '1337'

