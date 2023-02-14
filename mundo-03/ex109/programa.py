from ex109 import moeda
num = float(input('Digite um valor R$ '))
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num,mostrar=True)}.')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num,mostrar=True)}.')
print(f'Aumentando 10%, temos {moeda.aumentar(num, taxa=10, mostrar=True)}.')
print(f'Reduzindo 10%, temos {moeda.diminuir(num,taxa=10, mostrar=True)}')