maior = 0 #acumulador que so guarda numeros neste caso
menor = 0
for p in range(1, 6):
    peso = float(input('peso da {} pessoa: '.format(p)))
    if p == 1: #esta lendo o pessoa da primeira pessoa
        maior = peso
        menor = peso
        print(maior)
        print(menor)
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('o maior peso lido foi de {}kg'.format(maior))
print('o menor peso lido foi de {}kg'.format(menor))
