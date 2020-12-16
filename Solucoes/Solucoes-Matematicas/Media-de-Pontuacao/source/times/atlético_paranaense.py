import emoji
import time
import pygame

def Atlético_Paranaense():
    time.sleep(1)
    pygame.mixer.music.load('library/sounds/times/atlético_paranaense.mp3')
    pygame.mixer.music.play()
    time.sleep(17)
    print(emoji.emojize('Furacão!!!' + ' :hurricane: ' * 3,use_aliases=True))
    time.sleep(1)
    print()
    pass