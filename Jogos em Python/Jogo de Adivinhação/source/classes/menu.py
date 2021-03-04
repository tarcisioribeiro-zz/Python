from time import sleep
from random import randint
from pygame import mixer

def Menu ():
    mixer.init()
    escolha = int(input("Escolha um número de 0 a 20: "))
    sleep(1)
    print()
    computador = randint(0, 20)
    if escolha == computador:
        mixer.music.load('library/sounds/acerto.mp3')
        mixer.music.play()
        sleep(1)
        print('Haha! Eu sabia, você escolheu o número {}.'.format(escolha))
        sleep(15)
        print()
    else:
        sleep(1)
        print('Ok, eu não acertei o seu número. Vou tentar mais cinco vezes.')
        sleep(1)
        for i in (0, 5):

            computador = randint(0, 20)

            if computador  == escolha:
                mixer.music.load('library/sounds/acerto.mp3')
                mixer.music.play()
                print('Acertei! Hehehe')
                sleep(1)
                print()
                mixer.music.load('library/sounds/fim.mp3')
                mixer.music.play()
                sleep(1)
                print('Até a próxima!')
                sleep(3)
                break
            else:
                mixer.music.load('library/sounds/erro.mp3')
                mixer.music.play()
                print('Droga! errei de novo.')
                sleep(6)
