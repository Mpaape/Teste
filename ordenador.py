# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:21:19 2020

@author: Pichau
"""
from random import random
lista = []
tamanho = int((random()*10))
for i in range(tamanho):
    lista.append(round(random()*10,1))
print(lista)


print(lista)
for i in range(len(lista)):
   menor = i
   print("o menor" + str(lista[menor]))
   for j in range(i+1,len(lista)):        
      if lista[j] < lista[menor]:          
          menor = j         
   if lista[i] != lista[menor]:
        memoria = lista[i]
        lista[i] = lista[menor]
        lista[menor] = memoria
   print(lista)
print("lista final " + str(lista))
        
 