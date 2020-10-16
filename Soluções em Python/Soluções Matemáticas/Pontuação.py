print()
print('Bem vindo a calculadora de pontuação!')
print()
partida = int(
    input('Informe a quantidade de partidas que a equipe disputou: '))
print()
print('Para computar os resultados, precisamos que digite o resultado.\n\nD - DERROTA\nE - EMPATE\nV - VITÓRIA\n')

pontuacao = 0
resultado = ''

for i in range(1, partida + 1):
    resultado = str(input('Informe o resultado da {}ª partida: '.format(i)))
    if(resultado == 'D'):
        pontuacao += 0
    if(resultado == 'E'):
        pontuacao += 1
    if(resultado == 'V'):
        pontuacao += 3

print()
print('A pontuação do clube foi de {} pontos.'.format(pontuacao))
print()
