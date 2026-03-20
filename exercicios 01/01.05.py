dataNascimento = input('Insira sua data de nascimento completa: ')
dataAtual = input('Insira a data atual (dia, mes e ano): ')
dataNascimentoSemBarra = dataNascimento.split('/')
diaNascimento = int(dataNascimentoSemBarra[0])
mesNascimento = int(dataNascimentoSemBarra[1])
anoNascimento = int(dataNascimentoSemBarra[2])
dataAtualSemBarra = dataAtual.split('/')
diaAtual = int(dataAtualSemBarra[0])
mesAtual = int(dataAtualSemBarra[1])
anoAtual = int(dataAtualSemBarra[2])
if mesNascimento >= 6:

        if (mesAtual - mesNascimento) <0:
            print(f'vc tem {(anoAtual - anoNascimento) - 1} anos,  {} meses e {} dias')
        else:
            print(f'vc tem {} anos,  {} meses e {} dias')
else: