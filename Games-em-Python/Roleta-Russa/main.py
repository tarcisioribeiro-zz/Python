from time import sleep
from pygame import mixer
from emoji import emojize
from source.sorteio import Sorteio


sleep(1)
print()
sleep(1)
print(emojize('Vamos jogar Roleta Russa!!!' + ' :gun: ' * 3, use_aliases=True))
sleep(1)
print()

Sorteio()
