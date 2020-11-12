from emoji import emojize
from carrinho import total
from main import opc

def Pagamento():
    if(opc == 0):
        print('\033[33mSeu pedido ficou em R$ {:.2f}\033[m.'.format(total))
        print()
        pagamento = str(input(emojize(
            '\033[33mComo deseja pagar? \n\nDinheiro :dollar: - Pressione D\nCartão :credit_card: - Pressione C\n\nInforme aqui a opção:\033[m ', use_aliases=True)))
        if(pagamento == 'C'):
            parcelas = int(
                input('\033[33mEm quantas vezes deseja parcelar?\033[m '))
            print()
            print('\033[33mOk, seu pedido foi parcelado em {} vezes no cartão, com cada parcela no valor de R$ {:.2f}. \nVolte sempre!\033[m '.format(
                parcelas, (total / parcelas)))
            print()
        else:
            print(
                '\033[33mOk, muito obrigado pela sua compra! Tenha um bom dia, e volte sempre.\033[m')
            print()
    pass