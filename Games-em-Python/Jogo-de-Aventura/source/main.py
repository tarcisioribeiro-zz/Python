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
    destino = str(int(input(
        'Qual o destino deseja seguir: \n\nJapão\n:Coréia do Sul\nChina\nEstados Unidos\nFrança\nEspanha\nItália\nRússia\nReino Unido\nAlemanha\n\nDigite aqui sua opção: ', use_aliases=True))).strip().upper()
    time.sleep(1)
    print()
    if(destino == 'J'):
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
    else:
        print('Opção não reconhecida, tente novamente.')
        time.sleep(1)
print()
