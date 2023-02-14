km = float(input('{}quantos KM foram percorridos? KM '.format('\033[1;34m')))
dias = int(input('numeros de dias que ficou alugado? '))
preço = km * 0.15 + 60 * dias
print('\033[1;31mo carro ficou alugado por {} dias e percorreu {}km.entao custará ao cliente R${} reais'.format(dias,km,preço))