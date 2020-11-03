import emoji


# Pergunta ao usuário a velocidade do objeto
print()
vel = float(input('Informe a velocidade do obejto: '))
print()

# Retorna a informação ao usário
if(vel <= 300):
    print('É um carro.')
elif(vel > 300 and vel <= 450):
    print('É um helicóptero.')
elif(vel > 450 and vel <= 2750):
    print('É um avião.')
else:
    print('Objeto muito veloz, não foi possível reconhecer.')
print()
