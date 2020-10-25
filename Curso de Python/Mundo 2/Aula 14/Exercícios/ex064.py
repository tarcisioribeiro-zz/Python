print()
n = 0
cont = 0
soma = 0
while (n != 999):
    n = int(input('Informe um número: '))
    cont += 1
    soma += n
print()
print('Foram digitados {} números e a soma entre eles é de {}.'.format(cont, soma))
print()