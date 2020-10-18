# Juros de valor pago sobre um produto
produto = float(input('Informe o valor do produto: '))
print()
pagamento = str(input('Selecione o método de pagamento:\n\nA - À vista (dinheiro/cheque)\nB - À vista - cartão\nC - 2 vezes no cartão\nD - 3 ou mais vezes no cartão\n\nInforme sua opção: '))
print()

if(pagamento == 'A'):
    print('O valor do pagamento é de R$ {:.2f}.'.format(produto*0.9))
    print()
elif(pagamento == 'B'):
    print('O valor do pagamento é de R$ {:.2f}.'.format(produto*0.95))
    print()
elif(pagamento == 'C'):
    print('O valor do pagamento é de R$ {:.2f}.'.format(produto))
    print()
elif(pagamento == 'D'):
    print('O valor do pagamento é de R$ {:.2f}.'.format(produto*1.2))
    print()
else:
    print('Erro no pagamento, tente de novo.')
    print()
