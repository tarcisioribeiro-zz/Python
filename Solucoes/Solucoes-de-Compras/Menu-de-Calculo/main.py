from emoji import emojize
from time import sleep

from soma import Soma
from subtração import Subtração
from multiplicação import Multiplicação
from divisão import Divisão
from potenciação import Potenciação
from resto import Resto

print()
sleep(1)
print(emojize('Bem vindo à calculadora! :iphone:', use_aliases=True))
sleep(1)
print()

opção = -1

while opção != 0:
    opção = int(input('O que deseja calcular?\n\n[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n[5] Potenciação\n[6] Resto da divisão inteira\n[0] Sair do programa\n\nDigite aqui sua opção: ')) 
    sleep(1)
    print()
    if(opção == 1):
        Soma()
    elif(opção == 2):
        Subtração()
    elif(opção == 3):
        Multiplicação()
    elif(opção == 4):
        Divisão()
    elif(opção == 5):
        Potenciação()
    elif(opção == 6):
        Resto()
    elif(opção == 0):
        print('Volte sempre!')
        sleep(1)
        print('Desligando calculadora...')
        sleep(1)
    else:
        print('Não reconheci essa opção. Tente novamente')
        sleep(1)
        print()