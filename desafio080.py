'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).

No final, mostre a lista ordenada na tela.
'''

lista_numeros = []
numero = 0
posicao = 0

for n in range(1,6):
    numero = int(input("Digite um número: "))
    if len(lista_numeros) > 0:
        for a in range(0,len(lista_numeros)):
            if numero == lista_numeros[a]:
                numero = int(input(f'O número {numero} já foi acrescentado. Por favor escolha outro: '))
            elif numero > lista_numeros[a]:
                posicao = a + 1
            else:
                posicao = a
                break            
        lista_numeros.insert(posicao, numero)    
    else:
        lista_numeros.append(numero)
    print(f'Valor adicionado na posição {posicao}')

print(f'A lista ordenada ficou assim: {lista_numeros}')