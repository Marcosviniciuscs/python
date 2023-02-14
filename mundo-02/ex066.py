soma = cont = 0
while True:# enquanto for verdadeiro...
    num = int(input('digite um número [999 para sair] '))
    if num != 999:
        cont = cont + 1
        soma = soma + num
    else:
        break# interrompa
print(f'a soma dos {cont} valores foi de {soma}')



