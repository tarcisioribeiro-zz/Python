from time import sleep
from pygame import mixer
from emoji import emojize
from random import randint


def Sorteio():
    mixer.init()
    mixer.music.load('library/sounds/tambor-carregando.mp3')
    mixer.music.play()
    sleep(4)
    print(emojize('Revólver carregado, hora do jogo! :ghost: '))
    gatilho = 0
    vitória = 0
    bala = 0
    while vitória < 5 or gatilho != bala:
        bala = randint(1, 6)
        gatilho = randint(1, 6)
        sleep(1)
        print()
        sleep(1)
        print('Hora de apertar o gatilho!!!')
        sleep(1)

        mixer.music.load('library/sounds/tensão.mp3')
        mixer.music.play()
        sleep(5)

        if gatilho == bala:
            mixer.music.load('library/sounds/fogo.mp3')
            mixer.music.play()
            sleep(2)
            print()
            sleep(1)
            print(emojize('Você morreu, otário!!!' +
                          ' :skull: ', use_aliases=True))
            sleep(1)
            print()
            break
        elif gatilho != bala:
            mixer.music.load('library/sounds/vazio.mp3')
            mixer.music.play()
            sleep(2)
            print()
            sleep(1)
            print('Dessa vez você escapou!')
            sleep(1)
            vitória += 1
            if vitória == 5:
                sleep(1)
                print('Você está solto, pode voltar pra casa.')
                sleep(1)
                print()
                break


pass
