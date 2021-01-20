import pygame
from source.index.lista_acao import ListaAcao
from emoji import emojize
from time import sleep
from pygame import mixer
from source.index.lista_acao import ListaAcao


def Acao():
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
        mixer.init()
        mixer.music.load('library/sounds/generos/acao/predador.mp3')
        mixer.music.play()
        print(' Dutch é contratado pelo governo dos Estados Unidos para resgatar políticos presos na Guatemala.\nMas quando ele e sua equipe chegam na América Central, logo percebem que há algo errado.\nDepois de descobrir vários cadáveres, a equipe descobre que está sendo caçada por uma criatura brutal\ncom força sobre-humana e uma capacidade surpreendente de se camuflar.')
        sleep(35)
    elif escolha == 'R':
        mixer.init()
        mixer.music.load('library/sounds/generos/acao/rambo.mp3')
        mixer.music.play()
        print(' Rambo está preso em uma penitenciária federal quando recebe\numa proposta: será perdoado e reintegrado ao Exército se\nparticipar de uma missão no Vietnã, onde terá que enfrentar todo\ntipo de inimigos, inclusive oficiais americanos corruptos.')
        sleep(58)
    pass
