#Ler a idade e sexo de várias pessoas, perguntar ao usuário se ele deseja continuar e mostrar o resultado das seguintes condições:
# . Quantas pessoas são maiores de 18 anos.
# . Quantos homens foram cadastrados.
# . Quantas mulheres tem menos de 20 anos.

sexo = progresso = ''
quanthomem = idade = mulher20 = maior18 = 0

while True:
    print()
    sexo = str(input('Informe o sexo da pessoa (M/F): ')).strip().upper()
    idade = int(input('Informe a idade da pessoa: '))
    progresso = str(input('Deseja continuar? (S/N): ')).strip().upper()
    if progresso == 'N':
        break
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        quanthomem += 1
    if (sexo == 'F') and (idade < 20):
        mulher20 +=1
print()
print(f'Foram registradas {maior18} pessoas maiores de 18 anos, {quanthomem} homens e {mulher20} mulheres menores de 20 anos.')
print()