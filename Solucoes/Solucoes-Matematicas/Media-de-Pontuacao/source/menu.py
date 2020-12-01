import emoji
import time
from source.times.atlético import Atlético
from source.times.atlético_goianiense import Atlético_Goianiense
from source.times.atlético_paranaense import Atlético_Paranaense


def Menu():
    escolha = 0
    print()
    while escolha != 999:
        escolha = int(input('Informe sua escolha: '))
        time.sleep(1)
        print()
        if(escolha == 1):
            Atlético()
        elif(escolha == 2):
            Atlético_Goianiense()
        elif(escolha == 3):
            Atlético_Paranaense()
    pass
