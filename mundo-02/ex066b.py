cont = soma = 0
while True:    #loop infinto
    num = int(input('digite um valor(999 para sair): '))
    if num == 999:
        break# desvia a execução para fora do laço
    cont = cont + 1
    soma = soma + num
print(f'a soma dos {cont} valores e de {soma}')# método novo
