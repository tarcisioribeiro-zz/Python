from categorias.animação import Animação
from src.categorias.ação import Ação
from time import sleep
import emoji
print()
sleep(1)
print(emoji.emojize('Seja bem vindo! :raising_hand:', use_aliases=True))
print()
sleep(1)
print('-' * 60)
sleep(1)
print('')
print('Bem vindo ao nosso catálogo de filmes!\nAqui estão as categorias:')
print('')
print('Ação')
print('Animação')
print('Comédia')
print('Documentário')
print('Drama')
print('Romance')
sleep(1)
print()
print('-' * 60)
sleep(1)
print()
escolha = ''

while escolha not in 'AÇÃOANIMAÇÃOCOMÉDIADOCUMENTÁRIODRAMAROMANCE':
    escolha = str(input('Informe sua escolha: ')).upper()
    sleep(1)
    print()
    if(escolha == 'AÇÃO'):
        Ação()
    if(escolha == 'ANIMAÇÃO'):
        Animação()
sleep(1)
print('Acesse meu github! \n\nhttps://github.com/tarcisioribeiro')
sleep(1)
print()
