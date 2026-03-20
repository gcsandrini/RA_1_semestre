usuario = input('Insira seu usuario: ').lower()
senha = input('Insira sua senha: ')
if usuario == 'admin' and senha == '1234':
    print('Acesso liberado')
elif usuario == 'convidado' and senha == '':
    print('Acesso restrito')
else:
    print('Acesso bloqueado')