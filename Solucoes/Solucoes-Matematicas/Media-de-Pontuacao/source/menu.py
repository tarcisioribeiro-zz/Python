import emoji
import time
from source.times.atlético import Atlético
from source.times.atlético_goianiense import Atlético_Goianiense

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
    pass