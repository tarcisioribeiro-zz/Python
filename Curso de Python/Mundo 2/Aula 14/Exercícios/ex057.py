print()
s = ''
while (s != 'M' and s != 'F'):
    s = str(input('Informe o seu sexo: '))
    if s != 'M' and s != 'F':
        print('Não entendi o que você digitou. Tente novamente.')
print()