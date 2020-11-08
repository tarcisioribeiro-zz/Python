from time import sleep
import emoji
import time
import datetime
now = datetime.datetime.now()
print()
time.sleep(1)
print(emoji.emojize('{} :earth_americas:', use_aliases=True).format(now))
print()
time.sleep(1)
print(emoji.emojize(
    'Bem vindo ao jogo de aventura! :runner: :runner: :runner:', use_aliases=True))
time.sleep(1)
print()
print(emoji.emojize('Vamos pegar um avião! :airplane:', use_aliases=True))
time.sleep(1)
print()
destino = ''
while destino != 'L':
    destino = str(input('Qual o destino deseja seguir: \n\nJapão\nCoréia do Sul\nChina\nEstados Unidos\nFrança\nEspanha\nItália\nRússia\nReino Unido\nAlemanha\n\nDigite aqui sua opção: ')).upper().strip()
    time.sleep(1)
    print()
    if(destino == 'J'):
        print(emoji.emojize(' :airplane: ' * 10, use_aliases=True))
        time.sleep(1)
        print()
        pegar = ''
        destino = ''
        print('Bem vindo ao japão!')
        time.sleep(1)
        print()
        while pegar != 'N':
            pegar = str(input(emoji.emojize(
                'O que deseja pegar?\n\n:bike: Bicicleta\n:car: Carro\n:bullettrain_side: Trem Bala\n\nEscreva aqui sua opção: ', use_aliases=True))).strip().upper()
            time.sleep(1)
            print()
    elif(destino == ''):
        print()
    elif(destino == ''):
        print()
    elif(destino == ''):
        print()
    elif(destino == ''):
        print()
    elif(destino == ''):
        print()
    elif(destino == ''):
        print()
    elif(destino == ''):
        print()
    elif(destino == ''):
        print()
print()
