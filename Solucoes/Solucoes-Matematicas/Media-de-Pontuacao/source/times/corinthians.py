import emoji
import time
import pygame


def Corinthians():
    time.sleep(1)
    pygame.mixer.music.load('library/sounds/times/corinthians.mp3')
    pygame.mixer.music.play()
    time.sleep(17)
    print(emoji.emojize('Vai Corinthians!!!' ' :eagle: ' * 3,use_aliases=True))
    time.sleep(1)
    print()
    pass
