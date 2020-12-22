import pygame
import time
import emoji


def Brasileirão():
    empates = 0
    derrotas = 0
    vitórias = 0
    pontuação = 0
    resultado = ''
    time.sleep(1)
    print(emoji.emojize('Bem vindo ao Brasileirão!' + ' :soccer: ' * 3, use_aliases=True))
    pygame.mixer.music.load('library/sounds/competições/brasileirão.mp3')
    pygame.mixer.music.play()
    time.sleep(15)
    for i in range(1, 39):
        resultado = str(input(
            'Você deve informar o prognóstico da partida: \n\nDerrota\nEmpate\nVitória\n\nDigite aqui o resultado da {} partida: '.format(i))).upper()
        time.sleep(1)
        if(resultado == 'DERROTA'):
            derrotas += 1
        elif(resultado == 'EMPATE'):
            empates += 1
            pontuação += 1
        elif(resultado == 'VITÓRIA'):
            vitórias += 1
            pontuação += 3
        else:
            print('Não reconheço esse prognóstico. Tente novamente.')
            time.sleep(1)
    print('A pontuação do seu time foi de {} pontos, com {} derrotas, {} empates e {} vitórias. O aproveitamento foi de {:.2f}%.')
    time.sleep()
    pass
