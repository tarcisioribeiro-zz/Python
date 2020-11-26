# Bloco de importações
import time
import emoji
import pygame

# Iniciação do Player
pygame.mixer.init()
pygame.mixer.music.load('library/sounds/principal/hino_cbf_rj.mp3')
pygame.mixer.music.play()
time.sleep(12)
print()

# Boas vindas
time.sleep(1)
print(emoji.emojize(' :soccer: ' * 20, use_aliases=True))
time.sleep(1)
print()
time.sleep(1)
print('Bem vindo à calculadora de pontos do futebol brasileiro!')
time.sleep(1)
print()