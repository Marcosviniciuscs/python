lista = []
listpar = []
listimpar = []
num = 0
opc = " "
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    opc = str(input('deseja continuar? [s/n] ')).upper()
    if num % 2 == 0:
        listpar.append(num)
    else:
        if num % 2 == 1:
            listimpar.append(num)
    if opc == "N":
        break
print(f'Os números digitados foram : {lista}')
print(f'Números  pares digitados : {listpar}')
print(f'Números ímpares digitados: {listimpar}')

