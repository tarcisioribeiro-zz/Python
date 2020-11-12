import pygame
import time
import emoji

def Japão():
    pygame.mixer.music.load('library/sounds/decolagem.mp3')
    pygame.mixer.music.play()
    time.sleep(8)
    print(emoji.emojize(' :airplane: ' * 10, use_aliases=True))
    time.sleep(1)
    print()
    pegar = 0
    pygame.mixer.music.load('library/sounds/japão.mp3')
    pygame.mixer.music.play()
    print('Bem vindo ao Japão!')
    time.sleep(10)
    print()
    while pegar != 999:
        pegar = int(input(emoji.emojize(
            'O que deseja pegar?\n\n:bike: [ 1 ] Bicicleta\n:car: [ 2 ] Carro\n:bullettrain_side: [ 3 ] Trem Bala\n\nEscreva aqui sua opção: ', use_aliases=True)))
        time.sleep(1)
        print()
        if(pegar == 1):
                print(
                    'A distância até Tokyo é de 10 Km, você gastará 30 minutos de bicicleta.')
                time.sleep(1)
                print()
                pygame.mixer.music.load('library/sounds/bicicleta.mp3')
                pygame.mixer.music.play()
                print(emoji.emojize(' :bike: ' * 30, use_aliases=True))
                time.sleep(6)
                print()
                print('Parabéns, você chegou!')
                time.sleep(1)
                print()
                break
        elif(pegar == 2):
            print(
                'A distância até Tokyo é de 10 Km, você gastará 15 minutos de carro.')
            time.sleep(1)
            print()
            pygame.mixer.music.load('library/sounds/buzina_carro.mp3')
            pygame.mixer.music.play()
            print(emoji.emojize(' :car: ' * 15, use_aliases=True))
            time.sleep(3)
            print()
            print('Parabéns, você chegou!')
            time.sleep(1)
            print()
            break
        elif(pegar == 3):
            print(
                'A distância até Tokyo é de 10 Km, você gastará 5 minutos de trem-bala.')
            time.sleep(1)
            print()
            pygame.mixer.music.load('library/sounds/trem_bala.mp3')
            pygame.mixer.music.play()
            print(emoji.emojize(' :bullettrain_side: ' * 5, use_aliases=True))
            time.sleep(15)
            print()
            print('Parabéns, você chegou!')
            time.sleep(1)
            print()
            break
        elif(pegar == 999):
            print('Ok! Esperamos que volte em breve!')
            time.sleep(1)
            print()
        else:
            print('Não reconheço essa opção. Tente novamente.')
            time.sleep(1)
            print()

    pass

