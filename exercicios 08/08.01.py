matriz = [[0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0]]
for linha in range(5):
    for coluna in range(5):
        if linha == coluna:
            matriz[linha][coluna] = 1
for i in range(5):
    print(matriz[i])