'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na
sequência.

No final, mostre uma listagem de preços, organizando os dados de forma tabular.
'''

itens = ('Pão na chapa', 5, 
         'Café expressso curto', 3.5, 
         'Capuccino com canela', 9,
         'Omelete', 12.5,
         'Frapuccino', 20,
         'Brownie', 15.5,
         'Vitamina de morango', 13)

print(f'{20*'*'} CAFETERIA WIL E TAI {20*'*'}')
print(f'{25*' '}VALORES{25*' '}')

contador = 0
while contador < len(itens):
    espaçador = 36 - len(itens[contador])
    print(f'{itens[contador]} {espaçador*'-'} R${itens[contador+1]:.2f}')
    contador += 2