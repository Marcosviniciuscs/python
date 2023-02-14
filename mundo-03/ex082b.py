numeros = list()
par = list()
impar = list()
while True:
    numeros.append(int(input('Digite um número: ')))
    resp = str(input('deseja continuar? [S/N] '))
    if resp in "Nn":
        break
for indice, valores in enumerate(numeros):
    if valores % 2 == 0:
        par.append(valores)
    elif valores % 2 == 1:
        impar.append(valores)
print(f'Números completos: {numeros}')
print(f'Números pares: {par}')
print(f'Números impares: {impar}')
