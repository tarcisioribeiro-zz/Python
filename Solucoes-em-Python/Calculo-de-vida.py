print()
nome = str(input('Me diga o seu nome: '))
idade = int(input('Me diga quantos anos você tem: '))
print()

dias = idade * 365
horas = dias*24
minutos = horas*60
segundos = minutos*60

print('Vamos lá, {}.'.format(nome))
print()
print('Você tem {} dias de vida.'.format(dias))
print('Você tem {} horas de vida.'.format(horas))
print('Você tem {} minutos de vida.'.format(minutos))
print('Você tem {} segundos de vida.'.format(segundos))
print()
