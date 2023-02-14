soma = 0 #acumulador
cont = 0 #contador
for c in range(1,501,2):
    if c % 3 == 0:
        soma = soma + c #acumulador soma um, multiplica...
        cont = cont + 1 #contador normalmente conta mais 1
print('a soma de todos os {} valores e igual a {}.'.format(cont,soma))

