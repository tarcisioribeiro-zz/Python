from source.index.lista_drama import ListaDrama
from time import sleep
from pygame import mixer

def Drama():

    ListaDrama()

    sleep(1)
    escolha = str(input('Informe que filme deseja assistir (Digite S para sair): ')
                  ).strip().upper()[0]
    sleep(1)
    print()

    while escolha not in '':

        sleep(1)
        print('Digite uma opção válida.')
        sleep(1)

    if escolha == '':
        mixer.init()
        mixer.music.load('library/sounds/generos/drama/.mp3')
        mixer.music.play()
        print('')
        sleep()

    elif escolha == '':
        mixer.init()
        mixer.music.load('library/sounds/generos/drama/.mp3')
        mixer.music.play()
        print('')
        sleep()

    elif escolha == '':
        mixer.init()
        mixer.music.load('library/sounds/generos/drama/.mp3')
        mixer.music.play()
        print('')
        sleep()
        
    print()
    sleep(1)
    print('Fechando por hoje...')
    sleep(3)
    print()
    pass