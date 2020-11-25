from source.fases.alemanha import Alemanha
from source.fases.reino_unido import Reino_Unido
from source.fases.rússia import Rússia
from source.fases.itália import Itália
from source.fases.espanha import Espanha
from source.fases.frança import França
from source.fases.eua import Eua
from source.fases.china import China
from source.fases.coréia import Coréia
from source.fases.japão import Japão
from source.fases.brasil import Brasil
from source.fases.méxico import México
from source.fases.argentina import Argentina
from source.decisões.saída import Saida
import time
import emoji
import pygame


def Corpo_Principal():
    destino = 0
    while destino != 999:
        pygame.mixer.music.load('library/sounds/main/cintos_avião.mp3')
        pygame.mixer.music.play()
        print()
        print(emoji.emojize('Vamos pegar um avião! :airplane:', use_aliases=True))
        time.sleep(17)
        print()
        destino = int(input(emoji.emojize(
            'Qual o destino deseja seguir: \n\n[ 0 ] Brasil\n[ 1 ] Japão\n[ 2 ] Coréia do Sul\n[ 3 ] China\n[ 4 ] Estados Unidos\n[ 5 ] França\n[ 6 ] Espanha\n[ 7 ] Itália\n[ 8 ] Rússia\n[ 9 ] Reino Unido\n[ 10 ] Alemanha\n[ 11 ] México\n[ 12 ] Argentina\n[ 999 ] Finalizar o programa\n\nDigite aqui sua opção: ', use_aliases=True)))
        time.sleep(1)

        # Bloco de decisão
        if(destino == 0):
            Brasil()
        elif(destino == 1):
            Japão()
        elif(destino == 2):
            Coréia()
        elif(destino == 3):
            China()
        elif(destino == 4):
            Eua()
        elif(destino == 5):
            França()
        elif(destino == 6):
            Espanha()
        elif(destino == 7):
            Itália()
        elif(destino == 8):
            Rússia()
        elif(destino == 9):
            Reino_Unido()
        elif(destino == 10):
            Alemanha()
        elif (destino == 11):
            México()
        elif (destino == 12):
            Argentina()
        elif(destino == 999):
            Saida()
        else:
            print()
            time.sleep(1)
            print(
                'Opção não reconhecida. Informe uma opção válida ou digite 999 para sair.')

    pass
