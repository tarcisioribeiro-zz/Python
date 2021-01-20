import pygame
from source.index.lista_acao import ListaAcao
from emoji import emojize
from time import sleep
from pygame import mixer
from source.index.lista_acao import ListaAcao


def Acao():
    mixer.init()
    ListaAcao()
    sleep(1)
    escolha = str(input('Informe que filme deseja assistir: ')
                  ).strip().upper()[0]
    sleep(1)
    print()
    while escolha not in 'PRM':
        sleep(1)
        print('Digite uma opção válida.')
        sleep(1)
    if escolha == 'P':
        mixer.music.load('library/sounds/generos/acao/predador.mp3')
        mixer.music.play()
        print(' Dutch é contratado pelo governo dos Estados Unidos para resgatar políticos presos na Guatemala.\nMas quando ele e sua equipe chegam na América Central, logo percebem que há algo errado.\nDepois de descobrir vários cadáveres, a equipe descobre que está sendo caçada por uma criatura brutal com força sobre-humana e uma capacidade surpreendente de se camuflar.')
        sleep(35)
    pass
