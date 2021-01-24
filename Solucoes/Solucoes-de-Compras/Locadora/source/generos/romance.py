from source.index.lista_romance import ListaRomance
from time import sleep
from pygame import mixer

def Romance():
    
    ListaRomance()

    sleep(1)
    escolha = str(input('Informe que filme deseja assistir (Digite S para sair): ')
                  ).strip().upper()[0]
    sleep(1)
    print()

    while escolha not in 'U':

        sleep(1)
        print('Digite uma opção válida.')
        sleep(1)

    if escolha == 'U':
        mixer.init()
        mixer.music.load('library/sounds/generos/romance/moicanos.mp3')
        mixer.music.play()
        print('No século 18, em meio à guerra entre franceses e ingleses no\ncontinente norte-americano, um homem branco criado pelos índios\ntenta defender a sua tribo dos ataques.')
        sleep(51)

    elif escolha == '':
        mixer.init()
        mixer.music.load('library/sounds/generos/romance/.mp3')
        mixer.music.play()
        print('')
        sleep()

    elif escolha == '':
        mixer.init()
        mixer.music.load('library/sounds/generos/romance/.mp3')
        mixer.music.play()
        print('')
        sleep()
        
    print()
    sleep(1)
    print('Fechando por hoje...')
    sleep(3)
    print()  
    pass