'''Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado(entre 0 e 20)
e mostrá-lo por extenso.'''

contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
            'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
            'Onze', 'Doze', 'Treze','Catorze', 'Quinze',
            'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
continua = 'S'

while continua == 'S':
    numero = int(input('Digite um número entre 0 e 20: '))
    if  0 <= numero <= 20:
        print(f'Você digitou o número {contagem[numero]}')
        while True:
            continua = input('Deseja conferir mais um número? (Digite S OU N)').upper()
            if continua in 'SN':
                if continua == 'N':                
                    print('Obrigado por usar esse programa, até logo!')
                break
            else:
                print('Opção inválida!')
    else:
        print('Tente novamente') 