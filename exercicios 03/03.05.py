cord_X = float(input('Insira a coordenada do seu X: '))
cord_Y = float(input('Insira a coordenada do seu Y: '))
if cord_X == 10 and cord_Y <= 10:
    print('Na fronteira')
elif cord_Y == 10 and cord_X <= 10:
    print('Na fronteira')
elif cord_X < 10 or cord_Y < 10:
    print('Dentro do quadrado')
elif cord_X > 10 or cord_Y > 10:
    print('Fora do quadrado')