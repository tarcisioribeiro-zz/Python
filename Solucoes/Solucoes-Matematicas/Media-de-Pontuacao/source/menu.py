import emoji
import time
from source.times.atlético import Atlético
from source.times.atlético_goianiense import Atlético_Goianiense
from source.times.atlético_paranaense import Atlético_Paranaense
from source.times.bahia import Bahia
from source.times.botafogo import Botafogo
from source.times.bragantino import Bragantino
from source.times.ceará import Ceará
from source.times.corinthians import Corinthians
from source.times.coritiba import Coritiba
from source.times.flamengo import Flamengo
from source.times.fluminense import Fluminense
from source.times.fortaleza import Fortaleza
from source.times.goiás import Goiás
from source.times.grêmio import Grêmio
from source.times.internacional import Internacional
from source.times.palmeiras import Palmeiras

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
        elif(escolha == 4):
            Bahia()
        elif(escolha == 5):
            Botafogo()
        elif(escolha == 6):
            Bragantino()
        elif(escolha == 7):
            Ceará()
        elif(escolha == 8):
            Corinthians()
        elif(escolha == 9):
            Coritiba()
        elif(escolha == 10):
            Flamengo()
        elif(escolha == 11):
            Fluminense()
        elif(escolha == 12):
            Fortaleza()
        elif(escolha == 13):
            Goiás()
        elif(escolha == 14):
            Grêmio()
        elif(escolha == 15):
            Internacional
        elif(escolha == 16):
            Palmeiras()
    pass
