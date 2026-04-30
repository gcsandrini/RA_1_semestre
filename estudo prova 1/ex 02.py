n = int(input('Insira um numero: '))
s = 0
t = str('')
for i in range(1,n+1):
    s += i
    t += f'{i} + '
print(f'{n} = {t} = {s}')