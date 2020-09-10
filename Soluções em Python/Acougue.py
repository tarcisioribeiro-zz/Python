import emoji
print()
print('Bem vindo ao Açougue Santa Maria!')
print()
print('Consulte a tabela de preços, fique a vontade! Quando quiser finalizar a compra, digite 0.')
print()
print('----------------------------------------------')
print(emoji.emojize(
    '\033[33m1 :sheep: 1 Kg de Carne de carneiro - R$ 50,00\033[m', use_aliases=True))
print(emoji.emojize(
    '\033[33m2 :boar: 1 Kg de Carne de javali - R$ 80,00\033[m', use_aliases=True))
print(emoji.emojize(
    '\033[33m3 :pig: 1 Kg de Carne de porco - R$ 30,00\033[m', use_aliases=True))
print(emoji.emojize(
    '\033[33m4 :chicken: 1 Frango Inteiro - R$ 25,00\033[m', use_aliases=True))
print(emoji.emojize(
    '\033[33m5 :cow: 1 Kg de Carne bovina - R$ 45,00\033[m', use_aliases=True))
print(emoji.emojize(
    '\033[33m6 :fish: 1 Peixe inteiro - R$ 15,00\033[m', use_aliases=True))
print(emoji.emojize(
    '\033[33m7 :water_buffalo: 1 Kg de Carne de Búfalo - R$ 95,00\033[m', use_aliases=True))
print('----------------------------------------------')
print()

pagamento = ''
parcelas = 0
opc = ''
total = 0
nome = str(input('\033[33mOi, qual seu nome?\033[m '))
print()

while opc != 0:
    opc = int(input(
        '\033[33m{}, o que você quer levar?\n\nDigite o número do produto aqui:\033[m \n'.format(nome)))
    if(opc == 1):
        total += 50
    if(opc == 2):
        total += 80
    if(opc == 3):
        total += 30
    if(opc == 4):
        total += 25
    if(opc == 5):
        total += 45
    if(opc == 6):
        total += 15
    if(opc == 7):
        total += 95
    if(opc == 0):
        print('\033[33mSeu pedido ficou em R$ {:.2f}\033[m.'.format(total))
        print()
        pagamento = str(input(emoji.emojize(
            '\033[33mComo deseja pagar? \n\nDinheiro :dollar: - Pressione D\nCartão :credit_card: - Pressione C\n\nInforme aqui a opção:\033[m ', use_aliases=True)))
        if(pagamento == 'C'):
            parcelas = int(
                input('\033[33mEm quantas vezes deseja parcelar?\033[m '))
            print()
            print('\033[33mOk, seu pedido foi parcelado em {} vezes no cartão, com cada parcela no valor de R$ {:.2f}. \nVolte sempre!\033[m '.format(
                parcelas, (total / parcelas)))
            print()
            break
        else:
            print(
                '\033[33mOk, muito obrigado pela sua compra! Tenha um bom dia, e volte sempre.\033[m')
            print()
            break
