import time
import emoji
import pygame

pygame.mixer.music.load('library/sounds/principal/hino_cbf_rj.mp3')
pygame.mixer.music.play()
time.sleep(12)
print()
time.sleep(1)
print(emoji.emojize(' :soccer: ' * 20, use_aliases=True))