from time import sleep

print('Menu')
print()
print('A _ Calcular a tabuada de um número de 1 a 10.')
print('B _ Calcular o índice de massa corporal.')
print('C _ Calcular o fatorial de um número inteiro.')
print('D _ Descobrir o menor elemento de um vetor.')
print('E _ Obter a média dos elementos ímpares de um vetor de 20 posições.')
print()


opção = ' '


while True:
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
            IMC = peso/(altura**altura)
            return IMC

        sleep(1)
        print()
        sleep(1)
        str_peso = float(input('Informe o seu peso: '))
        print()
        str_altura = float(input('Informe a sua altura: '))
        print()
        enviardados_IMC = calcular_IMC(str_peso, str_altura)
        print('O seu IMC é de %f' % enviardados_IMC)
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
        print('O fatorial de', escolha_numero, 'é igual a', resultado)
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
        for i in range(0, tamanhovetor):
            sleep(1)
            vetor1.append(
                float(input('Informe o valor da posição do vetor: ')))
        resultado = menor_elemento(vetor1)

        sleep(1)
        print()
        sleep(1)
        print('O menor elemento do vetor é', int(resultado))
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
        for i in range(0, 20):
            _vetor.append(int(input('Informe o valor da posição: ')))
        for i in range(0, 20):
            if(_vetor[i] % 2 == 1):
                _timpar += _vetor[i]
                _qimpar += 1

        print()
        sleep(1)
        _media = media_impar(_vetor, _timpar, _qimpar)
        print('A média dos elementos ímpares do vetor é de', _media)
        sleep(1)
        pass
