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
    fase = str(input('Informe em que fase seu time terminou a competição:\n\n1ª Fase - (Digite primeira)\n2ª Fase - (Digite segunda)\n3ª Fase - (Digite 3ª Fase)\n4ª Fase - (Digite quarta)\nOitavas - (Digite oitavas)\nQuartas - (Digite quartas0'))
    pass
