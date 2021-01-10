import emoji
from time import sleep
from source.fases.deserto import Deserto
from source.fases.floresta import Floresta
from source.fases.praia import Praia

def Seletor():
    fase = int(input(emoji.emojize(
        'Qual fase deseja jogar? \n\n[ 1 ] Fase da floresta :evergreen_tree:\n[ 2 ] Fase da praia :palm_tree:\n[ 3 ] Fase do deserto :cactus:\n\nDigite aqui sua opção: ', use_aliases=True)))
    print()
    sleep(1)
    if(fase == 1):
        Floresta()
    if(fase == 2):
        Praia()
    if(fase == 3):
        Deserto()
    pass
