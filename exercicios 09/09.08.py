def e_palindromo(x):
    if x == x[::-1]:
        return(True)
def main():
    palindromo = input('Insira uma palavra: ')
    if e_palindromo(palindromo) == True:
        print('Essa palavra é um palindromo!')
    else:
        print('Essa palavra não é um palindromo!')
main()