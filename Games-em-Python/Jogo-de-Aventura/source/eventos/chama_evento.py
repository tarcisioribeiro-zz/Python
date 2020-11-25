import random
from random import randint
from source.eventos.cachorro import Cachorro
from source.eventos.caminhão import Caminhão
from source.eventos.ladrão import Ladrão
from source.eventos.bombeiro import Bombeiro
from source.eventos.alien import Alien

def Chama_Evento():
    evento = randint(0, 4)
    if(evento == 0):
        Cachorro()
    if(evento == 1):
        Caminhão()
    if(evento == 2):
        Ladrão()
    if(evento == 3):
        Bombeiro()
    if(evento == 4):
        Alien()
    pass
