'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
valores = []
maior = menor = 0

for i in range(0,5):
    valores.append(int(input('Digite um valor: ')))
    
    if i == 0:
        maior = menor = valores[i]
    else:
        if valores[i] >= maior:
            maior = valores[i]
        elif valores[i] <= menor:
            menor = valores[i]

print(f'Os valores digitados foram: {valores}')

print(f'O maior valor é {maior}, e está na posição ',end='')
for i, v in enumerate(valores):
    if valores[i] == maior:
        print(f'{i}...',end='')
print('')

print(f'O menor valor é {menor}, e está na posição ',end='')
for i, v in enumerate(valores):
    if valores[i] == menor:
        print(f'{i}...',end='')
print('')    


