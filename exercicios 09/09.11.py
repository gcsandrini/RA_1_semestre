def soma(x,y):
    return(x+y)
def subtrair(x,y):
    return(x-y)
def multiplicar(x,y):
    return(x*y)
def dividir(x,y):
    return(x/y)
def main():
    continuar = True
    while continuar == True:
        print('Escolha a operação\n1. somar\n2. subtrair\n3. multiplicar\n4. dividir\n5. sair')
        operacao = int(input('Digite o numero correspondete a operação desejada com base na tabela acima: '))
        if operacao == 1:
            numero1 = int(input('Insira o primeiro numero: '))
            numero2 = int(input('Insira o segundo numero: '))
            print(soma(numero1,numero2))
        if operacao == 2:
            numero1 = int(input('Insira o primeiro numero: '))
            numero2 = int(input('Insira o segundo valor: '))
            print(subtrair(numero1,numero2))
        if operacao == 3:
            numero1 = int(input('Insira o primeiro numero: '))
            numero2 = int(input('Insira o segundo valor: '))
            print(multiplicar(numero1,numero2))
        if operacao == 4:
            numero1 = int(input('Insira o primeiro numero: '))
            numero2 = int(input('Insira o segundo valor: '))
            print(dividir(numero1,numero2))
        if operacao == 5:
           continuar = False
main()