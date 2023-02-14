from math import sin,cos,tan,radians
angulo = float(input('\033[1;35mDIGITE O ANGULO: \033[m'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('\033[1;32mo angulo {} tem o seno {:.2f}'.format(angulo,seno))
print('o angulo {} tem o cosseno {:.2f}'.format(angulo,cosseno))
print('o angulo {} tem a tangente {:.2f}'.format(angulo,tangente))

