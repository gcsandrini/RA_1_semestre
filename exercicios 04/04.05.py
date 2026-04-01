escolha = int(input('1: soma \n2: subtração \n3: multiplicação \n4: divisão \n0: sair \nInsira o numero referente a ação desejada: '))
while escolha != 0:
    if escolha == 1:
        numero1 = float(input('Informe o primeiro numero: '))
        numero2 = float(input('Informe o segundo numero: '))
        print(f'{numero1} + {numero2} = {numero1+numero2} ')
        escolha = int(input('1: soma \n2: subtração \n3: multiplicação \n4: divisão \n0: sair \nInsira o numero referente a ação desejada: '))
    elif escolha == 2:
        numero1 = float(input('Informe o primeiro numero: '))
        numero2 = float(input('Informe o segundo numero: '))
        print(f'{numero1} - {numero2} = {numero1-numero2}')
        escolha = int(input('1: soma \n2: subtração \n3: multiplicação \n4: divisão \n0: sair \nInsira o numero referente a ação desejada: '))
    elif escolha == 3:
        numero1 = float(input('Informe o primeiro numero: '))
        numero2 = float(input('Informe o segundo numero: '))
        print(f'{numero1} * {numero2} = {numero1*numero2}')
        escolha = int(input('1: soma \n2: subtração \n3: multiplicação \n4: divisão \n0: sair \nInsira o numero referente a ação desejada: '))
    elif escolha == 4:
        numero1 = float(input('Informe o primeiro numero: '))
        numero2 = float(input('Informe o segundo numero: '))
        print(f'{numero1} / {numero2} = {numero1/numero2}')
        escolha = int(input('1: soma \n2: subtração \n3: multiplicação \n4: divisão \n0: sair \nInsira o numero referente a ação desejada: '))
    else:
        escolha = int(input('1: soma \n2: subtração \n3: multiplicação \n4: divisão \n0: sair \nInsira o numero referente a ação desejada: '))