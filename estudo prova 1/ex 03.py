n = int(input('Insira um numero: '))
m = 1
t = ''
for i in range(1,n+1):
    m *= i
    t += f'{i} x '
print(f'{n} = {t} = {m}')