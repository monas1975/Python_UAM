#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Zad 4. Napisz funkcje oov(text, vocab), która zwraca listę wyrazów
(bez duplikatów), które występują w tekście text i nie występują w liście
znanych wyrazów vocab. Argumenty funkcji text i vocab to odpowiednio łańcuch
znakowy i lista łańuchów znakowych (oov = out of vocabulary)
"""
#rozwiazanie

#definicja funkcji
def oov(text, vocab):
    resultList =[]
    textList=text.split()   #"rozbijam" text na wyrazy, znak rozdzialu spacja, i umieszczam w liscie
    for item in textList:   # przeszukuje liste
       if item not in vocab:  #sprawdzam czy wyraz jest w slowniku
           if item not in resultList:   #jesli nie jest oraz jesli juz nie zostal dodany do  wyniku to dodaje do listy z wynikami
             resultList.append(item)
    resultList.sort()  #sortuje rosnaco
    return resultList

# wywolanie funkcji
input = "this is a string , which i will use for string testing"
vocab = [',', 'this', 'is', 'a', 'which', 'for', 'will', 'i']
#output = ['string', 'testing', 'use']

output = oov(input,vocab)   #wywolanie funkcji i przypisanie do zmiennej
print(output)               #wynik wypisuje na konsoli
