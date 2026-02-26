'''
Crie um programa que tenha uma tupla com várias tupla_palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

tupla_palavras = ('HABILIDADE', 'QUALIDADE', 'INTENCAO', 'MENTORIA', 'CONDUCAO', 'LEITURA')
vogais = 'AEIOU'
contador_palavras = 0

while contador_palavras < len(tupla_palavras):
    total_vogais = 0
    contador_letras = 0
    lista_letras = []
    palavra = tupla_palavras[contador_palavras]
    while contador_letras < len(palavra):
        letra = tupla_palavras[contador_palavras][contador_letras]
        if letra in vogais:
            total_vogais += 1
            lista_letras.append(letra)        
        contador_letras += 1
    print(f'A palavra {palavra} tem {total_vogais} vogais.', end = ' ')
    print(*lista_letras)
    contador_palavras += 1