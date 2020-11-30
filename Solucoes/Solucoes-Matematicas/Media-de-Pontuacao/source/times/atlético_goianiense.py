import emoji
import time
import pygame

def Atlético_Goianiense():
    time.sleep(1)
    pygame.mixer.music.load('library/sounds/times/atlético_goianiense.mp3')
    pygame.mixer.music.play()
    time.sleep(14)
    print(emoji.emojize('Dragão!!!' + ' :dragon: ' * 3,use_aliases=True))
    time.sleep(1)
    print()
    pass