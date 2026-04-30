b = int(input('Insira a sua base: '))
e = int(input('Insira o seu expoente: '))
r = 1
t = ''
c = 1
for i in range(1,e+1):
    r *= b
    t += f'{b} x '
    c += 1 
print(r)
print(c)