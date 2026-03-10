dataNascimento = input('Insira sua data de nascimento completa: ')
if dataNascimento == '11/09/2007':
    print('<3<3<3 a data do meu amorzinho')
dataAtual = input('Insira a data atual (dia, mes e ano): ')
dataNascimentoSemBarra = dataNascimento.split('/')
diaNascimento = int(dataNascimentoSemBarra[0])
mesNascimento = int(dataNascimentoSemBarra[1])
anoNascimento = int(dataNascimentoSemBarra[2])
dataAtualSemBarra = dataAtual.split('/')
diaAtual = int(dataAtualSemBarra[0])
mesAtual = int(dataAtualSemBarra[1])
anoAtual = int(dataAtualSemBarra[2])
if diaNascimento - diaAtual >= 0:
    print('veio por aqui')
    if (mesAtual - mesNascimento) < 0:
        print(f'Sua idade atual é de {(anoAtual - anoNascimento) - 1} anos, {abs((mesAtual - mesNascimento)-1)} meses e {abs((diaAtual + 28) - diaNascimento)} dias')
    else:
        print(f'Sua idade atual é de {anoAtual - anoNascimento} anos, {abs((mesAtual - mesNascimento)-1)} meses e {abs((diaAtual + 28) - diaNascimento)} dias')
else:
    if (mesAtual - mesNascimento) < 0:
        print(f'Sua idade atual é de {(anoAtual - anoNascimento) - 1} anos, {abs(mesAtual - mesNascimento)} meses e {abs(diaAtual - diaNascimento)} dias')
    else:
        print(f'Sua idade atual é de {(anoAtual - anoNascimento)} anos, {abs(mesAtual - mesNascimento)} meses e {abs(diaAtual - diaNascimento)} dias')