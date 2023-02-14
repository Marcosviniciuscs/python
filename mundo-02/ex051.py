print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
a1 = int(input('primeiro termo: '))
r = int(input('Razão: '))
for n in range(1,11):# o laço repetira 10x ,mas fazendo 1 calculo por vez ao mesmo tempo escrevendo o valor na tela .
    an = a1 +(n - 1)* r
    print(an,end=' -> ')
print('acabou')
