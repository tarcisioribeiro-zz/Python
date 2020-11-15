from src.catálogo.catálogo_animação import Catálogo_Animação
from time import sleep


def Animação():
    Catálogo_Animação()
    escolha = str(input('Informe o nome completo do filme que deseja ver: ')).upper()
    sleep(1)
    print()
    if(escolha == 'MOANA'):
        print('Filme chato da porra!')
        sleep(1)
        print()
    elif(escolha == 'BIG HERO'):
        print('Filme legalzinho.')
        sleep(1)
        print()
    elif(escolha == 'DETONA RALPH!'):
        print('Filme foda!')
        sleep(1)
        print()
    else:
        print('Não temos esse filme na Locadora. Volte sempre que quiser!!!')
        sleep(1)
        print()
    pass
