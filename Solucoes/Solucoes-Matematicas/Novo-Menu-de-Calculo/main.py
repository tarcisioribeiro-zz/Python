print('Menu')
print()
print('A _ Calcular a tabuada de um número de 1 a 9.')
print('B _ Calcular o índice de massa corporal.')
print('C _ Calcular o fatorial de um número inteiro.')
print('D _ Descobrir o menor elemento de um vetor.')
print('E _ Obter a média dos elementos ímpares de um vetor de 20 posições.')
print()


opção = ' '


while True:
    opção = str(input('Informe sua opção:')).upper()
    print()
    if opção == 'A':
        def calcular_tabuada(_numero):
            numero = int(_numero)
            if(numero <= 0):
                print('Informe um número inteiro entre 1 e 9.')
            if(numero >= 10):
                print('Informe um número inteiro entre 1 e 9.')
            if(numero >= 1 and numero <= 10):
                for i in range(1, 11):
                    print(i, '*', numero, '=', i*numero)
                    print()
        numero_escolhido = int(input('Informe o número: '))
        print()
        enviar_tabuada = calcular_tabuada(numero_escolhido)
        pass

    if opção == 'B':
        def calcular_IMC(_peso, _altura):
            peso = float(_peso)
            altura = float(_altura)
            IMC = peso/(altura**altura)
            return IMC
        str_peso = float(input('Informe o seu peso: '))
        print()
        str_altura = float(input('Informe a sua altura: '))
        print()
        enviardados_IMC = calcular_IMC(str_peso, str_altura)
        print('O seu IMC é de %f' % enviardados_IMC)
        print()
        pass

    if opção == 'C':
        def calcular_fatorial(_numero, _resultado):
            numero = _numero
            resultado = _resultado
            return resultado

        escolha_numero = int(input('Informe o número: '))
        print()
        _fatorial = 1
        for i in range(1, escolha_numero + 1):
            _fatorial *= i
        resultado = calcular_fatorial(escolha_numero, _fatorial)
        print('O fatorial de', escolha_numero, 'é igual a', resultado)
        print()
        pass

    if opção == 'D':
        def menor_elemento(_vetor):
            vetor = _vetor
            menorvalor = min(vetor)
            return menorvalor
        tamanhovetor = int(input('Informe o tamanho do vetor: '))
        print()
        vetor1 = []
        for i in range(0, tamanhovetor):
            vetor1.append(
                float(input('Informe o valor da posição do vetor: ')))
        resultado = menor_elemento(vetor1)
        print()
        print('O menor elemento do vetor é', int(resultado))
        print()
        pass

    if opção == 'E':
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
        _media = media_impar(_vetor, _timpar, _qimpar)
        print('A média dos elementos ímpares do vetor é de', _media)
        pass