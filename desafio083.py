'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá 
analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
parenteses_expressao = []
qtd_parent_abre = 0
qtd_parent_fecha = 0

expressao = input('Digite uma expressão matemática: ')
print(f'A expressão digitada foi {expressao}')

for a in expressao:
    if a in '()':
        parenteses_expressao.append(a)
        #guardar posição do caracter do parêntese

if len(parenteses_expressao) > 0:
    for b in range (0,len(parenteses_expressao)):
        if parenteses_expressao[a] == '(':
            qtd_parent_abre += 1            
        else:
            qtd_parent_fecha += 1
            
    #colocar essa checagem dentro de um for que analise a expressão
    if parenteses_expressao[0] == ')':
        print('Não foi encontrada abertura para a expressão encerrada na posição')
    if parenteses_expressao[len(parenteses_expressao)] =='(':
        print('O fechamento de parênteses na posição')


    if qtd_parent_abre == qtd_parent_fecha:
        print('Os parênteses da expressão estão abertos e fechados corretamente')
    elif qtd_parent_abre > qtd_parent_fecha:
        print('Falta fechar parênteses em alguma expressão')
    else:
        print('Está faltando um parêntese de abertura.')    

    