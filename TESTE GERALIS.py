while True:
    print('Entre com a nota para o filme:')
    nota = str(input())
    try:
        nota = float(nota)
    except:
        print('Nota Invalida')
    else:
        if nota > 10 or nota < 0:
            print('Digite uma nota de 0 a 10')
        else:
            break
print(nota)
