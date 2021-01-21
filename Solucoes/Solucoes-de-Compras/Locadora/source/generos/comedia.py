from source.index.lista_comedia import ListaComedia
from time import sleep
from pygame import mixer


def Comedia():

    ListaComedia()

    sleep(1)
    escolha = str(input('Informe que filme deseja assistir (Digite S para sair): ')
                  ).strip().upper()[0]
    sleep(1)
    print()

    while escolha not in 'CPL':

        sleep(1)
        print('Digite uma opção válida.')
        sleep(1)

    if escolha == 'C':
        mixer.init()
        mixer.music.load('library/sounds/generos/comedia/caca_fantasmas.mp3')
        mixer.music.play()
        print('Uma equipe de cientistas, Dr. Egon, Dr. Ray e Dr. Peter, perde o\nemprego em uma universidade de Nova York. Eles decidem, então,\nse tornar caçadores de fantasmas e travar uma batalha de alta\ntecnologia com o sobrenatural por dinheiro. Com isso, se deparam\ncom uma porta de entrada para outra dimensão que lançará o mal\nsobre a cidade. Os caça-fantasmas precisam agora salvar Nov\nYork da destruição total.')
        sleep(28)

    elif escolha == 'P':
        mixer.init()
        mixer.music.load('library/sounds/generos/comedia/pf.mp3')
        mixer.music.play()
        print('Os caminhos de vários criminosos se cruzam nestas três histórias\nde Quentin Tarantino. Um pistoleiro se apaixona pela mulher de seu\nchefe, um boxeador não se sai bem em uma luta e um casal tenta\nexecutar um plano de roubo que foge do controle.')
        sleep(46)

    elif escolha == 'L':
        mixer.init()
        mixer.music.load('library/sounds/generos/comedia/miss_sunshine.mp3')
        mixer.music.play()
        print('O sonho da pequena Olive é participar do concurso da Pequena\nMiss Sunshine. Ela embarca então em uma divertida e comovente\nviagem com o pai, o tio, o avô, o irmão e a mãe. A família tem que\ncorrer contra o tempo para que Olive chegue no horário e possa\nfazer a apresentação criada pelo seu avô.')
        sleep(15)
        
    print()
    sleep(1)
    print('Fechando por hoje...')
    sleep(3)
    print()
    pass
