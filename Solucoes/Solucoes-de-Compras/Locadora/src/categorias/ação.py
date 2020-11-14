from src.catálogo.catálogo_ação import Catálogo_Ação
from time import sleep


def Ação():
    Catálogo_Ação()
    filme = str(
        input('Informe o nome completo do filme que deseja ver: ')).upper()
    sleep(1)
    print()
    if filme == 'RAMBO':
        print('Parabéns! Uma ótima escolha!\nRambo é um veterano de Guerra do Vietnã\n que busca refúgio e respostas\n para os seus traumas de guerra.')
        sleep(1)
        print()
    elif filme == 'DURO DE MATAR':
        print('Parabéns! Ótima escolha! Duro de Matar estrela Bruce Willis no papel de um policial casca grossa.')
        sleep(1)
        print()
    elif filme == 'PREDADOR':
        print('Parabéns" Uma excelente escolha!\n Predador é um filme que mostra uma equipe da CIA\n tentando resolver problemas de tráfico de drogas na América Central,\n quando se deparam com um assassino silencioso.')
        sleep(1)
        print()
    else:
        print('Não temos esse filme na Locadora. Volte sempre que quiser!!!')
        sleep(1)
        print()
    pass
