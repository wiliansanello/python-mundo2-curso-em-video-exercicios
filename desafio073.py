'''
Crie uma tupla preenchida com os 20 primeiros colocados da
tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
a)Apenas os 5 primeiros colocados.
b)Os últimos 4 colocados da tabela.
c)Uma lista com os times em ordem alfabética
d)Em que posição da tabela está o time do Vasco
e)Diga em qual posição determinado time está - BÔNUS'''

classificacao = ('Flamengo', 'Cruzeiro', 'Palmeiras', 'Bahia', 'Botafogo', 'Mirassol',
                 'São Paulo', 'Bragantino', 'Fluminense','Atlético-MG', 'Internacional',
                 'Ceará', 'Corinthians', 'Santos', 'Grêmio', 'Vitória', 'Vasco da Gama',
                 'Fortaleza', 'Juventude', 'Sport')


print('Os 5 primeiros colocados são: ', end='')
for time in classificacao[0:5]:
    print(f'{time}' ', ', end='')

print('\n\nOs 4 últimos colocados são: ')
for time_rebaixado in classificacao[-4:]:
    print(f'{time_rebaixado}' ', ', end='')

print(f'\n\nOs times em ordem alfabética são: {sorted(classificacao)}') 

print(f'O Vasco da Gama está na {classificacao.index('Vasco da Gama') + 1}ª posição')

try:
    time_procurado = input('Digite o time que deseja localizar ')
    print(f'O {time_procurado} está na {classificacao.index(time_procurado)+1}ª posição')
except:
    print('O time não foi encontrado. Em qual divisão ele estará?')