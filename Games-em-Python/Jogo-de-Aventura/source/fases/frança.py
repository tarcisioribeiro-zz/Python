from source.decisões.estrutura_veículo import Estrutura_veículo
import pygame
import time
import emoji

def França():
    pygame.mixer.music.load('library/sounds/decolagem.mp3')
    pygame.mixer.music.play()
    time.sleep(8)
    print(emoji.emojize(' :airplane: ' * 10, use_aliases=True))
    time.sleep(1)
    print()
    pegar = 0
    pygame.mixer.music.load('library/sounds/fases/frança.mp3')
    pygame.mixer.music.play()
    print('Bem vindo a França!')
    time.sleep(7)
    print()
    
    Estrutura_veículo()

    pass

