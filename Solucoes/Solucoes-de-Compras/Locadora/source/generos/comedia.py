from source.index.lista_comedia import ListaComedia
from emoji import emojize
from time import sleep
from pygame import mixer

def Comedia():
    
    ListaComedia()

    sleep(1)
    escolha = str(input('Informe que filme deseja assistir (Digite S para sair): ')
                  ).strip().upper()[0]
    sleep(1)
    print()

    while escolha not in 'PRM':

        sleep(1)
        print('Digite uma opção válida.')
        sleep(1)
        
    pass