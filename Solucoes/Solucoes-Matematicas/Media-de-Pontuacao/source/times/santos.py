import emoji
import time
import pygame


def Santos():
    time.sleep(1)
    pygame.mixer.music.load('library/sounds/times/santos.mp3')
    pygame.mixer.music.play()
    time.sleep(16)
    print(emoji.emojize('Peixe!!!' + ' :fish: ' * 3,use_aliases=True))
    time.sleep(1)
    print()
    pass
