# Bloco de importações das bibliotecas
from source.fases.frança import França
from source.fases.eua import Eua
from source.fases.china import China
from source.fases.coréia import Coréia
from source.fases.japão import Japão
from source.decisões.saída import Saida
import time
import emoji
import time
import datetime
import pygame

#Começa o player
pygame.mixer.init()

# Bloco de sáida que dá as boas vindas ao usuário
now = datetime.datetime.now()
print()
time.sleep(1)
print(emoji.emojize('Bem vindo! {} :earth_americas:', use_aliases=True).format(now))
print()
pygame.mixer.music.load('library/sounds/correndo.mp3')
pygame.mixer.music.play()
time.sleep(8)
print(emoji.emojize(
    'Bem vindo ao jogo de aventura! :runner: :runner: :runner:', use_aliases=True))
time.sleep(1)
print()
pygame.mixer.music.load('library/sounds/cintos_avião.mp3')
pygame.mixer.music.play()
print(emoji.emojize('Vamos pegar um avião! :airplane:', use_aliases=True))
time.sleep(8)
print()

# Bloco de entrada que solicita ao usuário a inserção dos seus dados
destino = 0
while destino != 999:
    destino = int(input(
        'Qual o destino deseja seguir: \n\n[ 1 ] Japão\n[ 2 ] Coréia do Sul\n[ 3 ] China\n[ 4 ] Estados Unidos\n[ 5 ] França\n[ 6 ] Espanha\n[ 7 ] Itália\n[ 8 ] Rússia\n[ 9 ] Reino Unido\n[ 10 ] Alemanha\n[ 999 ] Finalizar o programa\n\nDigite aqui sua opção: '))
    time.sleep(1)
    print()
    # Bloco de decisão
    if(destino == 1):
        Japão()
    elif(destino == 2):
        Coréia()
    elif(destino == 3):
        China()
    elif(destino == 4):
        Eua()
    elif(destino == 5):
        França()
    elif(destino == 6):
        print()
    elif(destino == 7):
        print()
    elif(destino == 8):
        print()
    elif(destino == 9):
        print()
    elif(destino == 10):
        print()
    elif(destino == 999):
        Saida()
    else:
        print('Opção não reconhecida. Informe uma opção válida ou digite 999 para sair.')
# Bloco de saída final
time.sleep(1)
print(
    'Acesse meu Github! https://github.com/tarcisioribeiro')
print()
