matriz = []
for i in range(5):
    aluno = []
    matricula = int(input('Insira a matricula: '))
    mediaProvas = float(input('Insira a media das provas: '))
    mediaTrabalhos = float(input('Insira a media dos trabalhos: '))
    mediaFinal = mediaProvas+mediaTrabalhos/2
    aluno.append(matricula)
    aluno.append(mediaProvas)
    aluno.append(mediaTrabalhos)
    aluno.append(mediaFinal)
    matriz.append(aluno)
maiorNotaFinal = matriz[0][3]
matriculaMaiorNotaFinal = 0
for i in range(5):
    if matriz[i][3] > maiorNotaFinal:
        maiorNotaFinal = matriz[i][3]
        matriculaMaiorNotaFinal = i
print(f'O aluno com a maior nota foi: {matriz[matriculaMaiorNotaFinal][0]}')