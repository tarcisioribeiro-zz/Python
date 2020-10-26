print()
primeiro = int(input('Informe o primeiro termo da PA: '))
print()
razao = int(input('Informe a razão da PA: '))
print()
termo = primeiro
cont = 1
while(cont <= 10):
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('Fim.')
print()
