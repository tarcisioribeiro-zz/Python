import emoji
print()
print(emoji.emojize('Média de pontuação no campeonato :bomb:', use_aliases=True))
print()
pontos = 0
empate = 0
vitoria = 0
derrota = 0
jogos = 0
resultado = ''
jogos = int(input('Quantos jogos a equipe jogou? '))
print()
for i in range(1, jogos + 1):
    resultado = str(input(
        'Qual foi o resultado da {}ª partida? [D, E, V] : '.format(i))).upper()
    if(resultado == 'D'):
        pontos += 0
        derrota += 1
    elif(resultado == 'E'):
        pontos += 1
        empate += 1
    elif(resultado == 'V'):
        pontos += 3
        vitoria += 1
media = (pontos / (jogos * 3)) * 100
print()
print('A pontuação total da equipe foi de {} pontos, com {} derrotas, {} empates e {} vitórias. O aproveitamento da equipe foi de {:.2f}%.'.format(pontos, derrota, empate, vitoria, media))
print()
