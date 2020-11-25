import time
import emoji
import pygame

def Bombeiro():
    time.sleep(1)
    print()
    print(emoji.emojize(' :firetruck: ' * 20, use_aliases=True))
    time.sleep(1)
    pygame.mixer.music.load('library/sounds/eventos/bombeiro.mp3')
    pygame.mixer.music.play()
    time.sleep(14)
    pass