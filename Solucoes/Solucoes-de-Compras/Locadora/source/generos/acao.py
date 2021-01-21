from source.index.lista_acao import ListaAcao
from time import sleep
from pygame import mixer


def Acao():

    ListaAcao()

    sleep(1)
    escolha = str(input('Informe que filme deseja assistir (Digite S para sair): ')
                  ).strip().upper()[0]
    sleep(1)
    print()

    while escolha not in 'PRM':

        sleep(1)
        print('Digite uma opção válida.')
        sleep(1)

    if escolha == 'P':
        mixer.init()
        mixer.music.load('library/sounds/generos/acao/predador.mp3')
        mixer.music.play()
        print('Dutch é contratado pelo governo dos Estados Unidos para resgatar políticos presos na Guatemala.\nMas quando ele e sua equipe chegam na América Central, logo percebem que há algo errado.\nDepois de descobrir vários cadáveres, a equipe descobre que está sendo caçada por uma criatura brutal\ncom força sobre-humana e uma capacidade surpreendente de se camuflar.')
        sleep(35)

    elif escolha == 'R':
        mixer.init()
        mixer.music.load('library/sounds/generos/acao/rambo.mp3')
        mixer.music.play()
        print('Rambo está preso em uma penitenciária federal quando recebe\numa proposta: será perdoado e reintegrado ao Exército se\nparticipar de uma missão no Vietnã, onde terá que enfrentar todo\ntipo de inimigos, inclusive oficiais americanos corruptos.')
        sleep(58)

    elif escolha == 'M':
        mixer.init()
        mixer.music.load('library/sounds/generos/acao/mi.mp3')
        mixer.music.play()
        print('O agente do governo Ethan Hunt e seu mentor, Jim Phelps,\nembarcam em uma missão secreta que toma um rumo desastroso,\nna qual Jim é morto e Ethan torna-se o principal suspeito do\nassassinato. Agora um fugitivo, Hunt recruta o brilhante Luther\nStickell e o piloto Franz Krieger para ajudá-lo a entrar no prédio da\nCIA, fortemente vigiado, a fim de pegar um arquivo de computador\nconfidencial que vai provar sua inocência.')
        sleep(53)
        
    print()
    sleep(1)
    print('Fechando por hoje...')
    sleep(3)
    print()
    pass
