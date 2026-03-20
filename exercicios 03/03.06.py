print('EM CASO DE RAIZ DE 2 SUBSTITUA POR 1.41')
lado1 = float(input('Insira a medida do primeiro lado: '))
lado2 = float(input('Insira a medida do segundo lado: '))
lado3 = float(input('Insira a medida do terceiro lado: '))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3 and lado1 == lado3:
            print('é um triangulo esquilatero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        if round(lado1 ** 2) == round(lado2 ** 2 + lado3 ** 2) or round(lado2 ** 2) == round(lado1 ** 2 + lado3 ** 2) or round(lado3 ** 2) == round(lado1 ** 2 + lado2 ** 2):
            print('é um triangulo isoceles e retangulo')
        else:
            print('é um triangulo isoceles')
    else:
        if lado1 ** 2 == lado2 ** 2 + lado3 ** 2 or lado2 ** 2 == lado1 ** 2 + lado3 ** 2 or lado3 ** 2 == lado1 ** 2 + lado2 ** 2:
            print('é um triangulo escaleno e retangulo')
        else:
            print('é um triangulo escaleno')
else:
    print('nao pode formar um triangulo')