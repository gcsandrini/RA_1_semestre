import random
V = True
tabuleiro = [1,2,3,4,5,6,7,8,9]
print('considere a casa 0 a primeira de cima p baixo da esquerda p direita, a casa dois a casa ao seu lado e assim por diante')
while V == True:
    escolha = int(input('Escolha uma das 9 casas: '))
    while tabuleiro[escolha] == 'X' or tabuleiro[escolha] == 'O':
        int(input('Essa casa ja foi escolhida! Insira outra: '))
    tabuleiro[escolha] = 'X'
    if tabuleiro[0] == tabuleiro[1] == tabuleiro[2] or tabuleiro[3] == tabuleiro[4] == tabuleiro[5] or tabuleiro[6] == tabuleiro[7] == tabuleiro[8] or tabuleiro[0] == tabuleiro[3] == tabuleiro[6] or tabuleiro[1] == tabuleiro[4] == tabuleiro[7] or tabuleiro[2] == tabuleiro[5] == tabuleiro[8] or tabuleiro[0] == tabuleiro[4] == tabuleiro[8] or tabuleiro[2] == tabuleiro[4] == tabuleiro[6]:
        print('Parabens vc ganhou')
        break
    escolha2 = random.randint(0,8)
    while tabuleiro[escolha2] == 'X' or tabuleiro[escolha2] == 'O' or escolha2 == escolha:
        escolha2 = random.randint(0,8)
    print(f'O robo escolheu a casa {escolha2}')
    tabuleiro[escolha2] = 'O'
    if tabuleiro[0] == tabuleiro[1] == tabuleiro[2] or tabuleiro[3] == tabuleiro[4] == tabuleiro[5] or tabuleiro[6] == tabuleiro[7] == tabuleiro[8] or tabuleiro[0] == tabuleiro[3] == tabuleiro[6] or tabuleiro[1] == tabuleiro[4] == tabuleiro[7] or tabuleiro[2] == tabuleiro[5] == tabuleiro[8] or tabuleiro[0] == tabuleiro[4] == tabuleiro[8] or tabuleiro[2] == tabuleiro[4] == tabuleiro[6]:
        print('O robo venceu')
        break