def contar_caracteres(x,y):
    return(x.count(y))
def main():
    frase = input('Insira uma frase: ').lower()
    caracter = input('Insira o caracter q vc quer q seja contado: ').lower()
    print(contar_caracteres(frase,caracter))
main()