# Simular um caixa eletrônico, onde o usuário informa o valor sacado e o caixa retorna a quantidade de cada nota

n = 0
cinquenta = vinte = dez = um = resto = 0 
while n == 0:
    n = int(input('Informe o valor que deseja sacar: '))
    if n <= 0:
        break
    cinquenta = n // 50
    resto = ((n) - n // 50)
    vinte = (n - cinquenta*50) - resto // 20
    resto = ((resto) - (resto // 20))
print(f'Cédulas de R$ 50: {cinquenta}.\nCédulas de R$ 20: {vinte}.')