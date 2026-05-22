def imprime_diagonal(x):
    return(x[0][0],x[1][1],x[2][2])
def main():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            valor = int(input(f'Insira seu valor para a posição {i+1},{j+1}: '))
            linha.append(valor)
        matriz.append(linha)
    print(imprime_diagonal(matriz))
main()