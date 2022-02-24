import csv, shutil
from time import sleep
from Utilis import ptcor, validanota


def mostrafilme(fs):
    '''
    Mostra pausadamente os filmes da fase selecionada
    :param fs: fase passada para execução
    :return: Null 0 ziero niente ''
    '''
    from time import sleep
    if fs < 0:
        texto = '~~~~ Série'
        fase = 's1.csv'
    else:
        texto = '~~~~ Filme'
        fase = ('f' + f'{fs}.csv')
    print(f'\033[0;34m{texto:<40}', end='')
    print(f'{"Ano   Nota"}\033[m')
    try:
        with open(fase, 'r') as arquivo:
            arquivo_csv = csv.reader(arquivo)
            for linha in arquivo_csv:
                dado = linha
                #print(dado)
                print(f'{dado[0]:<40}{dado[1]}    {dado[2]}')
                sleep(.5)
            arquivo.close()
    except (FileExistsError, FileNotFoundError, PermissionError):
        ptcor('Erro ao ler o arquivo', 3)
        sleep(2)


def atribnotas(fs):
    dados = []
    if fs == 5:
        texto = 'Série'
        fase = 's1.csv'
    else:
        texto = 'Filme'
        fase = ('f' + f'{fs}.csv')
    #print(f'\033[0;34m{texto:<40}', end='')
    #print(f'{"Ano       Nota"}\033[m')
    try:
        with open(fase, 'r') as arquivotc:
            arquivotc_csv = csv.reader(arquivotc, delimiter=',')
            for linha in arquivotc_csv:
                dados.append(linha)
            arquivotc.close()
    except (FileExistsError, FileNotFoundError, PermissionError):
        ptcor('Erro ao abrir o arquivo!', 3)
    else:
        #print('*' * 50)
        #print(dados)
        #print(dados[0])
        print(len(dados))
        for r in range(len(dados)):
            #print(dados[r][2])
            #print('*' * 50)
            #print('Entre com a nota para o filme:')
            filme = dados[r][0]
            dados[r][2] = validanota(filme)
        print('*' * 50)
        print(dados)
        print('*' * 50)
    try:
        with open('novo_'+fase, 'w', newline='', encoding='utf-8') as arquivotcf:
            for linha in dados:
                for r in range(3):
                    if r < 2:
                        arquivotcf.write(linha[r] + ',')
                    else:
                        arquivotcf.write(linha[r] + '\n')
    except(FileExistsError, FileNotFoundError, PermissionError):
        ptcor('Erro ao abrir o arquivo!', 3)
    else:
        arquivotcf.close()
        shutil.move(fase, 'old_' + fase)
        shutil.move('novo_' + fase, fase)
        print('salvando notas...')
        sleep(2)