# Contagem regressiva para estouro de fogos

from time import sleep
import emoji
import time

print()

for c in range(10, 0, -1):
    print('{}!'.format(c))
    sleep(1)
print()
print(emoji.emojize('Feliz Ano Novo! :boom: :boom: :boom: :boom: :boom:', use_aliases=True))
print()
