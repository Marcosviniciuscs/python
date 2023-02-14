import moeda
num = float(input('Digite um valor R$ '))
met = moeda.metade(num)
dob = moeda.dobro(num)
aum = moeda.aumentar(num, 10)
dim = moeda.diminuir(num, 10)
print(f'A metade de {moeda.moeda(num,"U$")} é {moeda.moeda(met,"U$")}.')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(dob)}.')
print(f'Aumentando 10%, temos {moeda.moeda(aum)}.')
