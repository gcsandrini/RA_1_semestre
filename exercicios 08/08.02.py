matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f'Insira o valor da posição[{i}][{j}]: '))
        linha.append(valor)
    matriz.append(linha)
maiorValor = matriz[0][0]
linhaMaior = 0
colunaMaior = 0
for l in range(4):
    for c in range(4):
        if matriz[l][c] > maiorValor:
            maiorValor = matriz[l][c]
            linhaMaior = l
            colunaMaior = c
print(f'Esse é o maior valor: {maiorValor} e ele se encotra na coluna: {colunaMaior} e na Linha: {linhaMaior}')