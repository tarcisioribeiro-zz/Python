from source.index.lista_drama import ListaDrama
from time import sleep
from pygame import mixer

def Drama():

    ListaDrama()

    sleep(1)
    escolha = str(input('Informe que filme deseja assistir (Digite S para sair): ')
                  ).strip().upper()[0]
    sleep(1)
    print()

    while escolha not in 'DFR':

        sleep(1)
        print('Digite uma opção válida.')
        sleep(1)

    if escolha == 'D':
        mixer.init()
        mixer.music.load('library/sounds/generos/drama/django.mp3')
        mixer.music.play()
        print('No sul dos Estados Unidos, o ex-escravo Django faz uma aliança\ninesperada com o caçador de recompensas Schultz para caçar os\ncriminosos mais procurados do país e resgatar sua esposa de um\nfazendeiro que força seus escravos a participar de competições\nmortais.')
        sleep(65)

    elif escolha == 'F':
        mixer.init()
        mixer.music.load('library/sounds/generos/drama/forrest_gump.mp3')
        mixer.music.play()
        print('Mesmo com o raciocínio lento, Forrest Gump nunca se sentiu\ndesfavorecido. Graças ao apoio da mãe, ele teve uma vida normal.\nSeja no campo de futebol como um astro do esporte, lutando no\nVietnã ou como capitão de um barco de pesca de camarão, Forrest\ninspira a todos com seu otimismo.\nMas a pessoa que Forrest mais\nama pode ser a mais difícil de salvar: seu amor de infância, a doce\ne perturbada Jenny.')
        sleep(63)

    elif escolha == 'R':
        mixer.init()
        mixer.music.load('library/sounds/generos/drama/rocky.mp3')
        mixer.music.play()
        print('Rocky Balboa, um pequeno boxeador da classe trabalhadora da\nFiladélfia, é arbitrariamente escolhido para lutar contra o campeão\ndos pesos pesados, Apollo Creed, quando o adversário do invicto\nlutador agendado para a luta é ferido. Durante o treinamento com o\nmal-humorado Mickey Goldmill, Rocky timidamente começa um\nrelacionamento com Adrian, a invisível irmã de Paulie, seu amigo\nempacotador de carne.')
        sleep(48)
        
    print()
    sleep(1)
    print('Fechando por hoje...')
    sleep(3)
    print()
    pass