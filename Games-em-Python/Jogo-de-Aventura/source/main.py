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
while destino != 999:
    destino = str(input(
        'Qual o destino deseja seguir: \n\n[ 1 ] Japão\n[ 2 ] Coréia do Sul\n[ 3 ] China\n[ 4 ] Estados Unidos\n[ 5 ] França\n[ 6 ]Espanha\n[ 7 ] Itália\n[ 8 ] Rússia\n[ 9 ] Reino Unido\n[10] Alemanha\n\nDigite aqui sua opção: ')).upper().strip()
    time.sleep(1)
    print()
    if(destino == 1):
        print(emoji.emojize(' :airplane: ' * 10, use_aliases=True))
        time.sleep(1)
        print()
        pegar = 0
        print('Bem vindo ao japão!')
        time.sleep(1)
        print()
        while pegar != 999:
            pegar = str(input(emoji.emojize(
                'O que deseja pegar?\n\n:bike: [ 1 ] Bicicleta\n:car: [ 2 ] Carro\n:bullettrain_side: [ 3 ] Trem Bala\n\nEscreva aqui sua opção: ', use_aliases=True))).strip().upper()
            time.sleep(1)
            print()
    elif(destino == 2):
        print()
    elif(destino == 3):
        print()
    elif(destino == 4):
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
        print('Finalizando aventura...')
        time.sleep(1)
        print()
        break
    else:
        print('Opção não reconhecida. Informe uma opção válida ou digite 999 para sair.')
print()
