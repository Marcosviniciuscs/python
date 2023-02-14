num = soma = cont = 0
while num != 999:#começa com zero para entrar dentro do loop
    num = int(input('Digite um numero: [999 para sair]  '))#com esse input ,eu tenho a chance de digitar o valor para ser comparado na condição
    if num != 999:
        soma = soma + num
        cont = cont + 1
print('foram contabilizados {} números'.format(cont))
print('A soma de todos os valores é {}'.format(soma))
