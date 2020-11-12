from emoji import emojize


def Tabela():
    print()
    print('Bem vindo ao Açougue Santa Maria!')
    print()
    print('Consulte a tabela de preços, fique a vontade! Quando quiser finalizar a compra, digite 0.')
    print()
    print('----------------------------------------------')
    print(emojize(
        '\033[33m1 :sheep: 1 Kg de Carne de carneiro - R$ 50,00\033[m', use_aliases=True))
    print(emojize(
        '\033[33m2 :boar: 1 Kg de Carne de javali - R$ 80,00\033[m', use_aliases=True))
    print(emojize(
        '\033[33m3 :pig: 1 Kg de Carne de porco - R$ 30,00\033[m', use_aliases=True))
    print(emojize(
        '\033[33m4 :chicken: 1 Frango Inteiro - R$ 25,00\033[m', use_aliases=True))
    print(emojize(
        '\033[33m5 :cow: 1 Kg de Carne bovina - R$ 45,00\033[m', use_aliases=True))
    print(emojize(
        '\033[33m6 :fish: 1 Peixe inteiro - R$ 15,00\033[m', use_aliases=True))
    print(emojize(
        '\033[33m7 :water_buffalo: 1 Kg de Carne de Búfalo - R$ 95,00\033[m', use_aliases=True))
    print('----------------------------------------------')
    print()
    pass
