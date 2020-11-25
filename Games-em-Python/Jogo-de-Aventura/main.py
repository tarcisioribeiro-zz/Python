# Bloco de importações das bibliotecas
from source.decisões.corpo_principal import Corpo_Principal
import datetime
import pygame
import time
import emoji

# Começa o player
pygame.mixer.init()

# Bloco de sáida que dá as boas vindas ao usuário
now = datetime.datetime.now()
print()
time.sleep(1)
print(emoji.emojize('Bem vindo! {} :earth_americas:', use_aliases=True).format(now))
print()
pygame.mixer.music.load('library/sounds/main/correndo.mp3')
pygame.mixer.music.play()
time.sleep(8)
print(emoji.emojize(
    'Bem vindo ao jogo de aventura! :runner: :runner: :runner:', use_aliases=True))
time.sleep(1)
print()
Corpo_Principal()

# Bloco de saída final
time.sleep(1)
print(
    'Acesse meu Github! https://github.com/tarcisioribeiro')
