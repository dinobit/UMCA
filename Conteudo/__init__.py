import Utilis
from Utilis import ptcor
from time import sleep
import Dados


def menu1():
    while True:
        Utilis.title('VER FILMES')
        Utilis.menu('Escolha uma opção', 'Fase 1', 'Fase 2', 'Fase 3', 'Fase 4', 'Menu Principal')
        x1 = (Utilis.validachoice(6))
        print(x1)
        if x1 == 5:
            break
        else:
            Dados.mostrafilme(x1)


def menu2():
    Utilis.title('VER SÉRIES')
    Dados.mostrafilme(-1)


def menu3():
    Utilis.title('DAR NOTAS')
    Utilis.menu('Dar Notas Para:', 'Fase 1', 'Fase 2', 'Fase 3', 'Fase 4', 'Séries', 'Menu Principal')
    x3 = (Utilis.validachoice(7))
    while True:
        if x3 == 6:
           break
        else:
            Dados.atribnotas(x3)
            break


def menu4():
    Utilis.title('Batalha')
    Utilis.menu('O que deseja fazer:', 'Mostrar melhor por batalha', 'Batalha Aleatória', 'Confronto Total!', 'Menu Principal')
    x4 = (Utilis.validachoice(5))
    while True:
        if x4 == 4:
           break

def menu5():
    ptcor('Obrigado por utilizar o UCM Avaliator', 1)
    print(f'\033[0;34m', end='')
    Utilis.title('Volte sempre')


def menu6():
    ptcor('  Este é um programa de testes para', 2)
    sleep(.5)
    ptcor('  treinamento de python. Cores, Funções', 2)
    sleep(.5)
    ptcor('  Filas, Dicionarios, Bibliotecas e', 2)
    sleep(.5)
    ptcor('  tratamento de arquivos. ', 2)
    sleep(.5)
    ptcor('  Desenvolvido por Thiago', 4, False)
    ptcor(' chipset ', 3, False)
    ptcor('Andrey Ferreira', 4)
    input('Enter to continue...')
