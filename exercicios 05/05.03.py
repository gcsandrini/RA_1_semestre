numeroInicial = int(input('Insira o numero inicial: '))
numeroFinal = int(input('Insira o numero final: '))
for n in range(numeroInicial, numeroFinal+1):
    print(f'TABUADA DO {n}')
    for i in range(11):
        print(f'{i} * {n} = {i*n}')