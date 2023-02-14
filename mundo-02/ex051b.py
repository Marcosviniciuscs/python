print('='*20)
print('\033[1;34m10 termos de uma PA\033[m')
print('='*20)
a1 = int(input('primeiro termo: '))
r = int(input('razão: '))
u1 = int(input('qual é a posição do termo que quer encontrar: '))
for n in range(1,u1 + 1): #o que esta dentro do parenteses indica quantos termos serão calculados
    an = a1 + (n - 1) * r # o laço vai ler cada termo ate o ultimo que foi indicado no input u1 e escreverá cada um pelo print
    print(an,end=' ')
