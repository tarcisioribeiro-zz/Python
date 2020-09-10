# Pergunta a quantidade de jogos do time
print()
jogos = int(input('Informe a quantidade de jogos do clube: '))
print()

# Faz a pergunta das pontuações
derrotas = int(input('Quantos jogos o time perdeu? '))
empates = int(input('Quantos jogos o time empatou? '))
vitorias = int(input('Quantos jogos o time ganhou? '))
print()

if (derrotas + empates + vitorias) < jogos:
    print('Erro, Rode o programa de novo.')
    print()
else:
# Faz o cálculo da pontuação
    aproveitamento = (empates + (vitorias*3)) / (jogos*3)
# Retorna o aproveitamento
    print('O aproveitamento do clube foi de {:.1f}%.'.format(aproveitamento*100))
    print()



