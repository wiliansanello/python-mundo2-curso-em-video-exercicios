'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.

No final, serão exibidos todos os valores únicos, digitados em ordem crescente.
'''

numeros = []
continua = 'S'

while True:
    
    if continua in 'Nn':
        print('Você interrompeu a digitação.')
        break
    elif continua in 'Ss':
        valor = int(input("Digite um valor para adicionar a lista: "))
        if valor not in numeros:
            numeros.append(valor)
        else:
            print(f'O número {valor} já foi adicionado, digite outro valor.')    
            
        while True:
            continua = input('Deseja digitar outro valor (S = Sim, N = Não)?: ')
            if continua not in 'SsNn':    
                print('Por favor, digite S para Sim ou N para Não')
            else:
                break    
    
numeros.sort()
print(f'Os valores digitados foram: {numeros}')
