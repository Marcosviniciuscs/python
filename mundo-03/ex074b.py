from random import randint
tupla = (randint(0, 9), randint(0,9), randint(0,9) , randint(0,9), randint(0,9))
print('os valores sorteados sao : ')
for n in tupla:
    print(n,end=' ')
maior= 0
menor = 0
for pos, numero in enumerate(tupla):
    if pos == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
print('')
print(f'o maior número é o {maior} ')
print(f'o menor número é o {menor} ')
