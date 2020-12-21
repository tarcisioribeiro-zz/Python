import pygame
import time
import emoji


def Copa_do_Brasil():
    time.sleep(1)
    print(emoji.emojize('Bem vindo a Copa do Brasil!' +
                        ' :soccer: ' * 3, use_aliases=True))
    time.sleep(1)
    print()
    fase = ''
    prêmio = 0
    fase = str(input('Informe em que fase seu time terminou a competição:\n\n1ª Fase - (Digite primeira)\n2ª Fase - (Digite segunda)\n3ª Fase - (Digite terceira)\n4ª Fase - (Digite quarta)\nOitavas - (Digite oitavas)\nQuartas - (Digite quartas)\nSemi - (Digite semi)\nFinal - (Digite final)\n\nDigite aqui a fase: ')).upper()
    while fase == '':
        if(fase == 'PRIMEIRA'):
            prêmio = 1000000
            time.sleep(1)
            print('A premiação do seu time é de R$ {}.'.format(prêmio))
        elif(fase == 'SEGUNDA'):
            prêmio = 2000000
            time.sleep(1)
            print('A premiação do seu time é de R$ {}.'.format(prêmio))
        elif(fase == 'TERCEIRA'):
            prêmio = 3000000
            time.sleep(1)
            print('A premiação do seu time é de R$ {}.'.format(prêmio))
        elif(fase == 'QUARTA'):
            prêmio = 5000000
            time.sleep(1)
            print('A premiação do seu time é de R$ {}.'.format(prêmio))
        elif(fase == 'OITAVAS'):
            prêmio = 8500000
            time.sleep(1)
            print('A premiação do seu time é de R$ {}.'.format(prêmio))
        elif(fase == 'QUARTAS'):
            prêmio = 15000000
            time.sleep(1)
            print('A premiação do seu time é de R$ {}.'.format(prêmio))
        elif(fase == 'SEMI'):
            prêmio = 22000000
            time.sleep(1)
            print('A premiação do seu time é de R$ {}.'.format(prêmio))
        elif(fase == 'FINAL'):
            prêmio = 30000000
            time.sleep(1)
            print('A premiação do seu time é de R$ {}.'.format(prêmio))
    pass
    time.sleep(1)
    print()
    