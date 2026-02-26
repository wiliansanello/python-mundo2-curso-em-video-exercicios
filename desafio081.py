'''
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, mostre:

a) Quantos números foram digitados.

b)A lista de valores ordenada de forma decrescente.

c)Se o valor 5 foi digitado e está ou não na lista.

EXTRA: A posição ou posições do número 5.'''

continua = ''
lista_numeros = []
tem5 = False
posicao = 0

while True:

    if continua == 'N':
        break
    numero = int(input('Digite um valor:'))

    '''for a in range (0, len(lista_numeros)):
        if a == 0:
            next
        else: 
            if numero < lista_numeros[a]:
                posicao = a
                break
            elif numero > lista_numeros[a]:
                posicao = a + 1'''
    lista_numeros.insert(posicao, numero)
    posicao += 1

    while True:
        continua = input('Deseja digitar outro número? (S/N): ').capitalize()    
        if continua in 'SN':
            break
        else:
            print('Por favor informe S para Sim e N para Não')

print(f'Foram digitados {len(lista_numeros)} números')
print(f'Eles estão listados pela ordem de digitação: {lista_numeros}')

for i in range(0, len(lista_numeros)):
    if lista_numeros[i] == 5:
        print(f'O número 5 está na posição {i}')
        tem5 = True

if not tem5:
    print('O número 5 não foi encontrado')

lista_numeros.sort(reverse=True)
print(f'A lista ordenada de forma decrescente ficou {lista_numeros}')
