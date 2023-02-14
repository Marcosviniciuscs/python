soma = 0 #acumulador
cont = 0 #contador
for c in range(1,7):
    n = int(input('digite o {}º numero: '.format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('voce informou {} numeros pares e a soma deles é igual a {}'.format(cont,soma))
