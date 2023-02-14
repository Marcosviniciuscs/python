from time import sleep
maior = 0
num1 = float(input('primeiro valor: '))
num2 = float(input('segundo valor: '))
mult = 0
opçao = 6
while opçao != 5:
    print('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR 
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA
    ''')
    opçao = int(input('>>>>>>>Qual é a sua opção:  '))
    if opçao == 1:
        soma = num1 + num2
        print('a soma entre {} e {} e igual {}.'.format(num1, num2, soma))
    elif opçao == 2:
        mult = num1 * num2
        print('a multiplicação entre {} e {} e igual a {}.'.format(num1, num2, mult))
    elif opçao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('o maior número é {}'.format(maior))
    elif opçao == 4:
        print('infrome os valores novamente:')
        num1 = float(input('digite o primeiro numero: '))
        num2 = float(input('digite o segundo numero: '))
    elif opçao == 5:
        print('>>>>>>>>>>>>>>')
        sleep(0.5)
        print('Finalizando...')
        sleep(1)
        print('>>>>>>>>>>>>>>')
    else:
        print('tentativa inválida.tente outra opção')
