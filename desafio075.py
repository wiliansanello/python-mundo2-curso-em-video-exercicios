'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final,
mostre:

a) Quantas vezes apareceu o valor 9
b) Em que posição foi digitado o primeiro valor 3
c) Quais foram os números pares
'''
tupla = ()

for contagem in range(0,4):
    valor = int(input('Digite um valor para a coleção: '))
    tupla = tupla + (valor, ) 
    contagem += 1

print(f'O número 9 se repete {tupla.count(9)} vezes.')
print('O número 3 ', end='')

try:    
    print(f'está na posição {tupla.index(3)+1}.')
except:
    print('não foi localizado.')

#solução Guanabara posição número 3
''' if 3 in tupla:
        print(f'está na posição {tupla.index(3)+1})
    else
        print(f'não foi encontrado') 
'''

posicao = 0
num_pares = ()
for numero_par in tupla:
    if tupla[posicao]%2 == 0:
        num_pares = num_pares + (tupla[posicao],)
    posicao += 1

if len(num_pares) > 0:
    print(f'Os números pares dentro da tupla são: {num_pares}')
else:
    print('Não foram encontrados números pares')     

