import random
from random import randint
from source.eventos.cachorro import Cachorro
from source.eventos.caminhão import Caminhão
from source.eventos.ladrão import Ladrão

def Chama_Evento():
    evento = randint(1, 3)
    if(evento == 1):
        Cachorro()
    if(evento == 2):
        Caminhão()
    if(evento == 3):
        Ladrão()
    pass