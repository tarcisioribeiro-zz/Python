from source.decisões.estrutura_veículo import Estrutura_veículo
import pygame
import time
import emoji


def Eua():
    print()
    print(emoji.emojize(' :airplane: ' * 10, use_aliases=True))
    time.sleep(1)
    print()
    pygame.mixer.music.load('library/sounds/main/decolagem.mp3')
    pygame.mixer.music.play()
    time.sleep(8)
    pegar = 0
    pygame.mixer.music.load('library/sounds/fases/eua.mp3')
    pygame.mixer.music.play()
    print('Bem vindo aos Estados Unidos!')
    time.sleep(8)
    print()
    Estrutura_veículo()

    pass
