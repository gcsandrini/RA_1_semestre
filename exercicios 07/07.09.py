import random
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random.shuffle(alfabeto)
decisao = input('escolha uma letra do alfabeto: ').lower()
chute = int(input('Escolha um numero de 1 a 26 p vc tentar acertar em qual posição a letra q vc escolheu esta: '))
if chute == alfabeto.index(decisao)+1:
    print('vc acertou')
else:
    print('vc errou')