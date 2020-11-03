import emoji


# Pergunta ao usuário a velocidade do objeto
print()
vel = float(input('Informe a velocidade do objeto: '))
print()

# Retorna a informação ao usário
if(vel <= 300):
    print(emoji.emojize('É um carro :car:.', use_aliases=True))
elif(vel > 300 and vel <= 450):
    print(emoji.emojize('É um helicóptero :helicopter:.', use_aliases=True))
elif(vel > 450 and vel <= 2750):
    print(emoji.emojize('É um avião :airplane:.', use_aliases=True))
else:
    print('Objeto muito veloz, não foi possível reconhecer.')
print()
