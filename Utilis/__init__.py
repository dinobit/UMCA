def menu(msg, *args):
    print('\033[0;34m', end='')
    print(msg.center(42))
    print(f'\033[m', end='')
    cont = 1
    for i in args:
        print(f'    {cont} - ', end='')
        ptcor(i, 1)
        cont += 1


def title(msg, mod=0):
   print('='*42)
   print(msg.center(42))
   print('='*42)


def ptcor(txt, cor = 0, quebra = True):
    '''
    Recebe um texto e o imprime colorido
    :param txt: mensagem a imprimir
    :param cor: 0, sem cor - 1, amarelo - 2, azul - 3, vermelho - 4, verde
    :param quebra: False = Quebra a linha no final, True = Não quebra
    :return: Nada
    '''
    if cor == 0: # Sem cor
        print(f'\033[m', end='')
    elif cor == 1: # Amarelo
        print(f'\033[0;33m', end='')
    elif cor == 2: # Azul
        print(f'\033[0;34m', end='')
    elif cor == 3: # Vermelho
        print(f'\033[0;31m', end='')
    elif cor == 4: # Verde
        print(f'\033[0;32m', end='')
    print(f'{txt}', end ='')
    if quebra:
        print(f'\033[m')
    else:
        print(f'\033[m', end='')


def validachoice(l):
    '''
    Pede um INT para a opção de menu e o valida retornando a escolha polida
    :param l: l = limite (1 numero a mais que a quantidade de opções do menu)
    :return: c (escolha INT dentro das opções definidas)
    '''
    while True:
        c = input('Escolha uma opção: ')
        try:
            c = int(c)
            if 0 < c < l:
                break
            else:
                ptcor('Opção incorreta!', 3)
        except (ValueError, TypeError):
            ptcor('Opção incorreta!', 3)
    return c


def validanota(f):
    while True:
        print(f'Entre com a nota para o filme: {f}')
        nota = str(input('')).replace(',', '.')
        try:
            nota = float(nota)
        except:
            ptcor('Nota Invalida', 3)
        else:
            if nota > 10 or nota < 0:
                ptcor('Digite uma nota de 0 a 10', 3)
            else:
                break
    nota = str(nota)
    return nota


