import random
from random import randint
from source.eventos.cachorro import Cachorro
from source.eventos.caminhão import Caminhão
from source.eventos.ladrão import Ladrão

def Chama_Evento():
    evento = randint(0, 2)
    if(evento == 0):
        Cachorro()
    if(evento == 1):
        Caminhão()
    if(evento == 2):
        Ladrão()
    pass