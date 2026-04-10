comando = input("Insira a conta, ou caso queira encerrar o programa digite 'sair': ").lower()
while comando != 'sair':
    if '+' in comando:
        operação = comando.split('+')
        print(f'{int(operação[0])+int(operação[1])}')
        comando = input("Insira a conta, ou caso queira encerrar o programa digite 'sair': ").lower()
    elif '-' in comando:
        operação = comando.split('-')
        print(f'{int(operação[0])-int(operação[1])}')
        comando = input("Insira a conta, ou caso queira encerrar o programa digite 'sair': ").lower()
    elif '*' in comando:
        operação = comando.split('*')
        print(f'{int(operação[0])*int(operação[1])}')
        comando = input("Insira a conta, ou caso queira encerrar o programa digite 'sair': ").lower()
    elif '/' in comando:
        operação = comando.split('/')
        if int(operação[1]) == 0:
            print('Voce nn pode dividir nd por 0')
            comando = input("Insira a conta, ou caso queira encerrar o programa digite 'sair': ").lower()
        else:
            print(f'{int(operação[0])/int(operação[1])}')
            comando = input("Insira a conta, ou caso queira encerrar o programa digite 'sair': ").lower()