from time import sleep
from emoji import emojize
import emoji


print()
sleep(1)
print(emojize('Verificador de senha :floppy_disk: ', use_aliases=True))
sleep(1)

confsenha = 'a'
senha = ''

while confsenha != senha:
    print()
    sleep(1)
    senha = str(input('Informe uma senha: '))
    sleep(1)
    print()
    confsenha = str(input('Confirme a senha: '))
    sleep(1)
    print()
    if senha == confsenha:
        print('Senha salva com sucesso.')
        sleep(3)
        break