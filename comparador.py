# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 13:34:41 2020

@author: Mateus Paape
"""
listao = []





produto ="Cafeteira Expresso Arno Dolce Gusto Mini Me Preta e Vermelha 220v"
produto2 ="Cafeteira Expresso Arno Nescafé Dolce Gusto Lumio 15 BAR - Vermelha 220v"
produto_limpo = "Cafeteira Expresso Arno Dolce Gusto Mini Me Preta e Vermelha 220v"


numeros = []
#restrições
for i in range(10000):
    numeros.append(i)
    
prep = ["de", "entre", "com", "em", "da", "do", "-", "um", "ou", "sem" ]
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cores = ['roxo','roxa','preto','preta','branco','branca','amarelo','amarela','vermelho','vermelha','dourado','dourada','prata','prateada','prateado']
voltagem = ['220v','120v','127v','110v','12v','9v','5v']




restricao = []
restricao.extend(prep)
restricao.extend(alfabeto)
restricao.extend(cores)
restricao.extend(voltagem)
restricao.extend(numeros)
print (len(restricao))


produto = produto.lower()
produto = produto.split()



produto_limpo = produto_limpo.lower()
produto_limpo = produto_limpo.split()

print(produto)

 


#retira as preposicoes,cores, etc do produto a ser comparado

for i in produto:
    for j in restricao:
        if i == j:
            print("removendo: " + i)
            produto_limpo.remove(i)
            print(produto_limpo)
          
print("string a ser comparada: " + str(produto_limpo))



# produto confrontado
            
produto2 = produto2.lower()
produto2 = produto2.split()

print(produto2)

# conta palavras encontradas
numerador = 0
denominador= len(produto)            


#comparando
for b in produto2:
    for a in produto_limpo:
        if a == b:
            numerador += 1
            listao.append(a)
            
print(numerador)             

indice = round((numerador)/ denominador ,2)
print(indice) 

resultado = (numerador,indice) 
print(listao)
print(resultado)