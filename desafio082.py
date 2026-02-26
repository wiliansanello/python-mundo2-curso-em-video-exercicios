'''
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
'''

lista_geral = []
lista_pares = []
lista_impares = []
continua = 'S'

while True:
    if continua == 'N':
        break
    else:
        numero = int(input('Informe um número: '))
        lista_geral.append(numero)
        while True:
            continua=input('Quer informar outro número (S/N) ?').capitalize()
            if continua in 'SN':
                break
            elif continua != 'S':
                print('Por favor, informe S para Sim ou N para Não')

for n in range(0, len(lista_geral)):
    if lista_geral[n] % 2 == 0:
        lista_pares.append(lista_geral[n])
    else:
        lista_impares.append(lista_geral[n])

lista_geral.sort()
print(f'Foram informados os números {lista_geral}')
lista_pares.sort()
print(f'São pares os números {lista_pares}')
lista_impares.sort()
print(f'São ímpares os números {lista_impares}')