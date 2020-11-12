# Bloco de importações das bibliotecas
import time
import emoji
import time
import datetime
import pygame
from pygame import mixer

#Começa o player
mixer.init()

# Bloco de sáida que dá as boas vindas ao usuário
now = datetime.datetime.now()
print()
time.sleep(1)
print(emoji.emojize('Bem vindo! {} :earth_americas:', use_aliases=True).format(now))
print()
mixer.music.load('library/sounds/correndo.mp3')
mixer.music.play()
time.sleep(8)
print(emoji.emojize(
    'Bem vindo ao jogo de aventura! :runner: :runner: :runner:', use_aliases=True))
time.sleep(1)
print()
mixer.music.load('library/sounds/cintos_avião.mp3')
mixer.music.play()
print(emoji.emojize('Vamos pegar um avião! :airplane:', use_aliases=True))
time.sleep(8)
print()

# Bloco de entrada que solicita ao usuário a inserção dos seus dados
destino = 0
while destino != 999:
    destino = int(input(
        'Qual o destino deseja seguir: \n\n[ 1 ] Japão\n[ 2 ] Coréia do Sul\n[ 3 ] China\n[ 4 ] Estados Unidos\n[ 5 ] França\n[ 6 ] Espanha\n[ 7 ] Itália\n[ 8 ] Rússia\n[ 9 ] Reino Unido\n[ 10 ] Alemanha\n\nDigite aqui sua opção: '))
    time.sleep(1)
    print()

    # Bloco de decisão
    if(destino == 1):
        mixer.music.load('library/sounds/decolagem.mp3')
        mixer.music.play()
        time.sleep(8)
        print(emoji.emojize(' :airplane: ' * 10, use_aliases=True))
        time.sleep(1)
        print()
        pegar = 0
        mixer.music.load('library/sounds/japão.mp3')
        mixer.music.play()
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
                mixer.music.load('library/sounds/bicicleta.mp3')
                mixer.music.play()
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
                mixer.music.load('library/sounds/buzina_carro.mp3')
                mixer.music.play()
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
                mixer.music.load('library/sounds/trem_bala.mp3')
                mixer.music.play()
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
    elif(destino == 2):
        print(emoji.emojize(' :airplane: ' * 9, use_aliases=True))
        time.sleep(1)
        pegar = 0
        print('Bem vindo a Coréia!')
        time.sleep(1)
        print()
        while pegar != 999:
            pegar = int(input(emoji.emojize(
                'O que deseja pegar?\n\n:bike: [ 1 ] Bicicleta\n:car: [ 2 ] Carro\n:bullettrain_side: [ 3 ] Trem Bala\n\nEscreva aqui sua opção: ', use_aliases=True)))
            time.sleep(1)
            print()
            if(pegar == 1):
                print(
                    'A distância até Seoul é de 15 Km, você gastará 45 minutos de bicicleta.')
                time.sleep(1)
                print()
                print(emoji.emojize(' :bike: ' * 45, use_aliases=True))
                time.sleep(1)
                print()
                print('Parabéns, você chegou!')
                time.sleep(1)
                print()
                break
            elif(pegar == 2):
                print(
                    'A distância até Seoul é de 15 Km, você gastará 22 minutos de carro.')
                time.sleep(1)
                print()
                print(emoji.emojize(' :car: ' * 22, use_aliases=True))
                time.sleep(1)
                print()
                print('Parabéns, você chegou!')
                time.sleep(1)
                print()
                break
            elif(pegar == 3):
                print(
                    'A distância até Seoul é de 15 Km, você gastará 7 minutos de trem-bala.')
                time.sleep(1)
                print()
                print(emoji.emojize(' :bullettrain_side: ' * 7, use_aliases=True))
                time.sleep(1)
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
    elif(destino == 3):
        print(emoji.emojize(' :airplane: ' * 15, use_aliases=True))
        time.sleep(1)
        pegar = 0
        print('Bem vindo a China!')
        time.sleep(1)
        print()
        while pegar != 999:
            pegar = int(input(emoji.emojize(
                'O que deseja pegar?\n\n:bike: [ 1 ] Bicicleta\n:car: [ 2 ] Carro\n:bullettrain_side: [ 3 ] Trem Bala\n\nEscreva aqui sua opção: ', use_aliases=True)))
            time.sleep(1)
            print()
            if(pegar == 1):
                print(
                    'A distância até Beijing é de 20 Km, você gastará 60 minutos de bicicleta.')
                time.sleep(1)
                print()
                print(emoji.emojize(' :bike: ' * 60, use_aliases=True))
                time.sleep(1)
                print()
                print('Parabéns, você chegou!')
                time.sleep(1)
                print()
                break
            elif(pegar == 2):
                print(
                    'A distância até Beijing é de 20 Km, você gastará 30 minutos de carro.')
                time.sleep(1)
                print()
                print(emoji.emojize(' :car: ' * 30, use_aliases=True))
                time.sleep(1)
                print()
                print('Parabéns, você chegou!')
                time.sleep(1)
                print()
                break
            elif(pegar == 3):
                print(
                    'A distância Beijing é de 20 Km, você gastará 10 minutos de trem-bala.')
                time.sleep(1)
                print()
                print(emoji.emojize(' :bullettrain_side: ' * 10, use_aliases=True))
                time.sleep(1)
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
    elif(destino == 4):
        print(emoji.emojize(' :airplane: ' * 15, use_aliases=True))
        time.sleep(1)
        pegar = 0
        print('Bem vindo aos Estados Unidos!')
        time.sleep(1)
        print()
        while pegar != 999:
            pegar = int(input(emoji.emojize(
                'O que deseja pegar?\n\n:bike: [ 1 ] Bicicleta\n:car: [ 2 ] Carro\n:bullettrain_side: [ 3 ] Trem Bala\n\nEscreva aqui sua opção: ', use_aliases=True)))
            time.sleep(1)
            print()
            if(pegar == 1):
                print(
                    'A distância até Washington é de 5 Km, você gastará 20 minutos de bicicleta.')
                time.sleep(1)
                print()
                print(emoji.emojize(' :bike: ' * 20, use_aliases=True))
                time.sleep(1)
                print()
                print('Parabéns, você chegou!')
                time.sleep(1)
                print()
                break
            elif(pegar == 2):
                print(
                    'A distância até Washington é de 5 Km, você gastará 10 minutos de carro.')
                time.sleep(1)
                print()
                print(emoji.emojize(' :car: ' * 10, use_aliases=True))
                time.sleep(1)
                print()
                print('Parabéns, você chegou!')
                time.sleep(1)
                print()
                break
            elif(pegar == 3):
                print(
                    'A distância Washington é de 5 Km, você gastará 5 minutos de trem-bala.')
                time.sleep(1)
                print()
                print(emoji.emojize(' :bullettrain_side: ' * 5, use_aliases=True))
                time.sleep(1)
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
    elif(destino == 5):
        print()
    elif(destino == 6):
        print()
    elif(destino == 7):
        print()
    elif(destino == 8):
        print()
    elif(destino == 9):
        print()
    elif(destino == 10):
        print()
    elif(destino == 999):
        mixer.music.load('library/sounds/fim_aventura.mp3')
        mixer.music.play()
        print('Finalizando aventura...')
        time.sleep(10)
        print()
        break
    else:
        print('Opção não reconhecida. Informe uma opção válida ou digite 999 para sair.')
# Bloco de saída final
time.sleep(1)
print(emoji.emojize(
    'Acesse meu Github :octocat:! https://github.com/tarcisioribeiro', use_aliases=True))
print()
