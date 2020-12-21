from source.competições.brasileirão import Brasileirão
from source.competições.brasileirão import Brasileirão
from source.competições.copa_do_brasil import Copa_do_Brasil
import time

def Escolha():
    escolha = int(input('Informe qual competição deseja:\n\n1 - Brasileirão\n2 - Copa do Brasil\n\nDigite aqui sua escolha: '))
    time.sleep(1)
    if(escolha == 1):
        Brasileirão()
    elif(escolha == 2):
        Copa_do_Brasil()
    pass