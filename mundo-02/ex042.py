r1 = float(input('primeira reta: '))
r2 = float(input('segunda reta: '))
r3 = float(input('terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos formam um triangulo ',end ='')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r3 == r2 != r1:
        print('ISOSCELES')
    elif r1 != r2 != r3:
        print('ESCALENO')
else:
    print('essas medidas não formam triangulos.')




