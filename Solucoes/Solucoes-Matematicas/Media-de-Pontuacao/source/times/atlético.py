import emoji
import time
import pygame


def Atlético():
    time.sleep(1)
    pygame.mixer.music.load('library/sounds/times/atlético.mp3')
    pygame.mixer.music.play()
    time.sleep(14)
    print(emoji.emojize('Galo!!!' + ' :chicken: ' * 3, use_aliases=True))
    time.sleep(1)
    print()
    pass
