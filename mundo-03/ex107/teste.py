import moeda

num = int(input('Informe um número: '))
print(f'aumentando 10 % , temos R${moeda.aumentar(num, 10)} ')
print(f'O dobro é igual {num} é {moeda.dobro(num)} .')
print(f'A metade do número {num} e igual a {moeda.metade(num)}. ')

