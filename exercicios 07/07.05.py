palavras = ['Neblina','Engrenagem','Cacto','Labirinto','Faísca','Horizonte','Âncora','Paralelepípedo','Satélite','Casulo']
menorPalavra = palavras[0]
maiorPalavra = palavras[0]
for i in range(len(palavras)):
    if len(palavras[i]) > len(maiorPalavra):
        maiorPalavra = palavras[i]
    elif len(palavras[i]) < len(menorPalavra):
        menorPalavra = palavras[i]
print(f'A maior palavra é: {maiorPalavra} \nE a menor é: {menorPalavra}') 