n = int(input('Insira um numero: '))
f = 1
t = str('')
for i in range(n,0,-1):
    t += f'{i} x '
    f *= i
print(f'{n}! = {t} = {f}')