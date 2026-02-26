'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que
estão na tupla
'''
from random import randint
colecao_numerica = ()

for contagem in range(0,5):
    numero = randint(0,100)
    colecao_numerica = colecao_numerica + (numero,)
    print('(' if contagem == 0 else '', end='')
    print(f'{numero}', end='')
    print(', ' if contagem < 4 else '',end='')
    print(')' if contagem == 4 else '', end='')
    contagem += 1

comparador = sorted(colecao_numerica)
print(f'\nO maior número é {comparador[4]}, e o menor número é {comparador[0]}')

#Solução do Guanabara
#print(f'\nO maior valor sorteado foi {max(colecao_numerica)}, e o menor valor'
#      f' foi {min(colecao_numerica)}')
