from source.decisões.estrutura_veículo import Estrutura_veículo
import pygame
import time
import emoji


def Reino_Unido():
    time.sleep(18)
    print(emoji.emojize(' :airplane: ' * 10, use_aliases=True))
    time.sleep(1)
    print()
    pygame.mixer.music.load('library/sounds/main/decolagem.mp3')
    pygame.mixer.music.play()
    pegar = 0
    pygame.mixer.music.load('library/sounds/fases/reino_unido.mp3')
    pygame.mixer.music.play()
    print('Bem vindo ao Reino Unido!')
    time.sleep(10)
    print()

    Estrutura_veículo()

    pass
