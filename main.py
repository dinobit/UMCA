import Utilis, Conteudo
from time import sleep
while True:
    Utilis.title('UCM AVALIATOR')
    Utilis.menu('Menu principal', 'Ver Filmes', 'Ver Séries', 'Dar Notas', 'Batalha', 'Sair', 'About')
    x = (Utilis.validachoice(7))
    if x == 6:  # about
        Conteudo.menu6()
    if x == 5:  # sair
        Conteudo.menu5()
        break
    if x == 1:  # Ver Filmes
        Conteudo.menu1()
    if x == 2:  # Ver Série
        Conteudo.menu2()
    if x == 3:  # Atribuir notas
        Conteudo.menu3()