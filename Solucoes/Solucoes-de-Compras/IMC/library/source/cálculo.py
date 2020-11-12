from time import sleep
from source.cadastro import nome, sexo, peso, altura 

def Calculo():
    imc = peso / (altura ** altura)
    if(imc < 18.5):
        print('Peso abaixo do ideal. Vamos ganhar peso!')
        sleep(1)
        print()
    elif(imc >= 18.5 and imc <= 24.9):
        print('Peso normal. Aproveite sua vida!')
        sleep(1)
        print()
    elif(imc >= 25 and imc <= 29.9):
        print('Peso acima do ideal. Vamos perder peso!')
        sleep(1)
        print()
    elif(imc >= 30 and imc <= 39.9):
        print('Peso mais que acima do ideal. Vamos fazer regime!')
        sleep(1)
        print()
    elif(imc >= 40):
        print('Peso muito acima do ideal. Vamos fazer cirurgia e regime!')
        sleep(1)
        print()
    pass