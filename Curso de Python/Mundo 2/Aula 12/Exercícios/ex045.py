# Jogo do Jokenpô

from random import randint
import emoji

print()
print('JOKENPÔ')
print()

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print(emoji.emojize(
    'Suas opções são: \n\n[ 0 ] Pedra :bomb: \n[ 1 ] Papel :page_facing_up: \n[ 2 ] Tesoura :scissors:'))
print()
jogador = int(input('Qual a sua jogada? '))
print()
print('JO')
print('KEN')
print('PÔ')
print('==' * 20)
print('O computador escolheu: {}.'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('==' * 20)
print()
if computador == 0:  # Computador jogou pedra
    if jogador == 0:  # Jogador jogou pedra
        print('Empate.')
        print()
    elif jogador == 1:  # Jogador jogou papel
        print('O jogador venceu.')
        print()
    elif jogador == 2:  # Jogador jogou tesoura
        print('O computador venceu.')
        print()
elif computador == 1:  # Computador jogou papel
    if jogador == 0:  # Jogador jogou pedra
        print('O computador venceu.')
        print()
    elif jogador == 1:  # Jogador jogou papel
        print('Empate.')
        print()
    elif jogador == 2:  # Jogador jogou tesoura
        print('O jogador venceu.')
        print()
elif computador == 2:  # Computador jogou tesoura
    if jogador == 0:  # Jogador jogou pedra
        print('O jogador venceu.')
        print()
    elif jogador == 1:  # Jogador jogou papel
        print('O computador venceu.')
        print()
    elif jogador == 2:  # Jogador jogou tesoura
        print('Empate.')
        print()
else:
    print('Jogada inválida.')
    print()
