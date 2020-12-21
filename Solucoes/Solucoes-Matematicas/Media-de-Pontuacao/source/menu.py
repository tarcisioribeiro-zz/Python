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
from source.times.santos import Santos
from source.times.são_paulo import São_Paulo
from source.times.sport import Sport
from source.times.vasco import Vasco
from source.competições.escolha import Escolha

def Menu():
    escolha = 0
    print()
    while escolha != 999:
        escolha = int(input('Informe sua escolha: '))
        time.sleep(1)
        print()
        if(escolha == 1):
            Atlético()
            Escolha()
        elif(escolha == 2):
            Atlético_Goianiense()
            Escolha()
        elif(escolha == 3):
            Atlético_Paranaense()
            Escolha()
        elif(escolha == 4):
            Bahia()
            Escolha()
        elif(escolha == 5):
            Botafogo()
            Escolha()
        elif(escolha == 6):
            Bragantino()
            Escolha()
        elif(escolha == 7):
            Ceará()
            Escolha()
        elif(escolha == 8):
            Corinthians()
            Escolha()
        elif(escolha == 9):
            Coritiba()
            Escolha()
        elif(escolha == 10):
            Flamengo()
            Escolha()
        elif(escolha == 11):
            Fluminense()
            Escolha()
        elif(escolha == 12):
            Fortaleza()
            Escolha()
        elif(escolha == 13):
            Goiás()
            Escolha()
        elif(escolha == 14):
            Grêmio()
            Escolha()
        elif(escolha == 15):
            Internacional()
            Escolha()
        elif(escolha == 16):
            Palmeiras()
            Escolha()
        elif(escolha == 17):
            Santos()
            Escolha()
        elif(escolha == 18):
            São_Paulo()
            Escolha()
        elif(escolha == 19):
            Sport()
            Escolha()
        elif(escolha == 20):
            Vasco()
            Escolha()
    pass
