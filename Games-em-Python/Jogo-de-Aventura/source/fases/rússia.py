from source.decisões.estrutura_veículo import Estrutura_veículo
import pygame
import time
import emoji


def Rússia():
    print(emoji.emojize(' :airplane: ' * 10, use_aliases=True))
    time.sleep(1)
    print()
    pygame.mixer.music.load('library/sounds/main/decolagem.mp3')
    pygame.mixer.music.play()
    time.sleep(8)
    pegar = 0
    pygame.mixer.music.load('library/sounds/fases/rússia.mp3')
    pygame.mixer.music.play()
    print('Bem vindo a Rússia!')
    time.sleep(16)
    print()

    Estrutura_veículo()

    pass
