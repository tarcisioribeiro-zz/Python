import emoji

def Cachorro():
    decisão = ''
    while decisão != 'FUGIR':
        decisão = str(input('Digite fugir para desviar do cachorro: ')).upper()
        if(decisão == 'FUGIR'):
            print('Você fugiu do cachorro!')
        else:
            print(emoji.emojize('O cachorro te mordeu!' + ':dog:' * 10, use_aliases=True))
    pass