soma = int(0)
while True:
    numero = input('Insira um numero inteiro positivo: ')
    if numero.isdigit() == True:
        for n in range(1,int(numero)+1):
            print(n, end=' + ')
            soma += n
        print(end='= 'f'{soma}')
        break
    else:
        print('Esse numero nn é aceito')      