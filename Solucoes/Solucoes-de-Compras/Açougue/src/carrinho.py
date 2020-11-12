from main import nome
def Carrinho():
    opc = 0
    total = 0
    while opc != 0:
        opc = int(input(
            '\033[33m{}, o que você quer levar?\n\nDigite o número do produto aqui:\033[m \n'.format(nome)))
        if(opc == 1):
            total += 50
        if(opc == 2):
            total += 80
        if(opc == 3):
            total += 30
        if(opc == 4):
            total += 25
        if(opc == 5):
            total += 45
        if(opc == 6):
            total += 15
        if(opc == 7):
            total += 95
    pass