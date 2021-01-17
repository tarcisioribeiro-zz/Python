from time import sleep
from emoji import emojize

print()
sleep(1)
print(emojize('Bem vindo ao nosso programa! :earth_americas:', use_aliases=True))
sleep(1)


opção = ' '


while True:
    print()
    sleep(1)
    print('Menu')
    sleep(1)
    print()
    sleep(1)
    print('A _ Calcular a tabuada de um número de 1 a 10.')
    sleep(1)
    print('B _ Calcular o índice de massa corporal.')
    sleep(1)
    print('C _ Calcular o fatorial de um número inteiro.')
    sleep(1)
    print('D _ Descobrir o menor elemento de um vetor.')
    sleep(1)
    print('E _ Obter a média dos elementos ímpares de um vetor de 20 posições.')
    sleep(1)
    print()
    print('Digite "S" para sair.')
    sleep(1)
    print()
    sleep(1)
    opção = str(input('Informe sua opção: ')).upper()
    sleep(1)

    if opção == 'A':
        def calcular_tabuada(_numero):
            numero = int(_numero)
            if numero <= 0 or numero >= 10:
                sleep(1)
                print('Informe um número inteiro entre 1 e 10.')
            else:
                for i in range(1, 11):
                    print(f'{i} * {numero} = {i * numero}')
                    sleep(1)

        print()
        sleep(1)
        numero_escolhido = int(input('Informe o número: '))
        print()
        sleep(1)
        enviar_tabuada = calcular_tabuada(numero_escolhido)
        pass

    elif opção == 'B':
        def calcular_IMC(_peso, _altura):
            peso = float(_peso)
            altura = float(_altura)
            imc = round(peso//(altura ** altura))
            return imc

        sleep(1)
        print()
        sleep(1)
        str_peso = float(input('Informe o seu peso: '))
        sleep(1)
        print()
        sleep(1)
        str_altura = float(input('Informe a sua altura: '))
        sleep(1)
        print()
        enviardados_IMC = calcular_IMC(str_peso, str_altura)
        print(f'O seu IMC é de {enviardados_IMC}.')
        pass

    elif opção == 'C':
        def calcular_fatorial(_numero, _resultado):
            numero = _numero
            resultado = _resultado
            return resultado

        print()
        sleep(1)
        escolha_numero = int(input('Informe o número: '))
        sleep(1)
        print()
        _fatorial = 1
        for i in range(1, escolha_numero + 1):
            _fatorial *= i
        resultado = calcular_fatorial(escolha_numero, _fatorial)
        sleep(1)
        print(f'O fatorial de {escolha_numero} é igual {resultado}.')
        sleep(1)
        pass

    elif opção == 'D':
        def menor_elemento(_vetor):
            vetor = _vetor
            menorvalor = min(vetor)
            return menorvalor

        sleep(1)
        print()
        sleep(1)
        tamanhovetor = int(input('Informe o tamanho do vetor: '))
        sleep(1)
        print()
        vetor1 = []
        for i in range(1, tamanhovetor + 1):
            sleep(1)
            vetor1.append(
                float(input(f'Informe o valor da {i}ª posição do vetor: ')))
        resultado = menor_elemento(vetor1)

        sleep(1)
        print()
        sleep(1)
        print(f'O menor elemento do vetor é {int(resultado)}.')
        sleep(1)
        pass

    elif opção == 'E':
        def media_impar(vetor_media, _totalimpar, _quantimpar):
            vetormedia = vetor_media
            totalimpar = _totalimpar
            quantimpar = _quantimpar
            mediaimpar = totalimpar/quantimpar
            return mediaimpar

        _vetor = []
        _timpar = 0
        _qimpar = 0
        for i in range(1, 21):
            _vetor.append(
                int(input('Informe o valor da {}ª posição: '.format(i))))
        for i in range(0, 20):
            if(_vetor[i] % 2 == 1):
                _timpar += _vetor[i]
                _qimpar += 1

        print()
        sleep(1)
        _media = media_impar(_vetor, _timpar, _qimpar)
        print('A média dos elementos ímpares do vetor é de {_media}.')
        sleep(1)
        pass

    elif opção == 'S':
        print()
        sleep(1)
        print('Desligando o programa...')
        sleep(3)
        print()
        break
