nota = float(input('Insira um valor de 0 a 10: '))
while nota < 0 or nota > 10:
    print('Precisa ser um valor entre 0 e 10')
    nota = float(input('Insira um valor de 0 a 10: '))
print('A nota q vc informou é valida') 