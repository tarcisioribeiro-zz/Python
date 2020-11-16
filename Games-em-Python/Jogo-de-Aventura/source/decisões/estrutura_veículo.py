import pygame
import time
import emoji

def Estrutura_veículo():
    veiculo = int(input(emoji.emojize(
            'Qual veículo deseja utilizar?\n\n:bike: [ 1 ] Bicicleta\n:car: [ 2 ] Carro\n:bullettrain_side: [ 3 ] Trem Bala\n\nEscreva aqui sua opção: ', use_aliases=True)))
    time.sleep(1)
    print()
    if(veiculo == 1):
        print(
                    'A distância até o Centro é de 10 Km, você gastará 30 minutos de bicicleta.')
        time.sleep(1)
        print()
        pygame.mixer.music.load('library/sounds/decisões/bicicleta.mp3')
        pygame.mixer.music.play()
        print(emoji.emojize(' :bike: ' * 30, use_aliases=True))
        time.sleep(6)
        print()
        print('Parabéns, você chegou!')
        time.sleep(1)
        print()
    elif(veiculo == 2):
        print(
                'A distância até o Centro é de 10 Km, você gastará 15 minutos de carro.')
        time.sleep(1)
        print()
        pygame.mixer.music.load('library/sounds/decisões/buzina_carro.mp3')
        pygame.mixer.music.play()
        print(emoji.emojize(' :car: ' * 15, use_aliases=True))
        time.sleep(3)
        print()
        print('Parabéns, você chegou!')
        time.sleep(1)
        print()
    elif(veiculo == 3):
        print(
                'A distância até o Centro é de 10 Km, você gastará 5 minutos de trem-bala.')
        time.sleep(1)
        print()
        pygame.mixer.music.load('library/sounds/decisões/trem_bala.mp3')
        pygame.mixer.music.play()
        print(emoji.emojize(' :bullettrain_side: ' * 5, use_aliases=True))
        time.sleep(15)
        print()
        print('Parabéns, você chegou!')
        time.sleep(1)
        print()
    elif(veiculo == 999):
        print('Ok! Esperamos que volte em breve!')
        time.sleep(1)
        print()
    else:
        print('Não reconheço essa opção. Tente novamente.')
        time.sleep(1)
        print()
    pass
