from src.catálogo.catálogo_comédia import Catálogo_Comédia
from time import sleep


def Comédia():
    Catálogo_Comédia()
    escolha = str(
        input('Informe o nome completo do filme que deseja ver: ')).upper()
    sleep(1)
    print()
    if(escolha == 'OS SEIS RIDÍCULOS'):
        print('Filme chato da porra!')
        sleep(1)
        print()
    elif(escolha == 'MONTY PYTHON'):
        print('Filme legal demais!')
        sleep(1)
        print()
    elif(escolha == 'RICK AND MORTY'):
        print('Filme foda!')
        sleep(1)
        print()
    else:
        print('Não temos esse filme na Locadora. Volte sempre que quiser!!!')
        sleep(1)
        print()
    pass
