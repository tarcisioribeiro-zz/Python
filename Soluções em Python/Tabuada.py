# Importa a biblioteca de emojis
import emoji
print()

# Uso dos emojis
print(emoji.emojize(
    '\033[34mTabuada de 1 a 10 :school:\033[m', use_aliases=True))
print()

# Pede ao usuário que informe o número que deseja multiplicar
num = int(
    input('\033[34mInforme um número de 1 a 10 para calcular a tabuada: \033[m'))
print()

# Retorna ao usuário a tabuada
for i in range(0, 11):
    print('\033[34m{} x {} = {} \033[m'.format(i, num, (i*num)))
print()
