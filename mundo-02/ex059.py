from time import sleep
soma = 0 #acumulador
mult = 1
opçao = 6
maior = 0
guardasoma = 0
guardamult = 0
guardasoma2 = 0
guardamult2 = 0
for c in range(1,3):
    num = int(input('primeiro número: '))
    soma = soma + num
    mult = mult * num
    if c == 1:
        maior = num
        guardasoma = num
        guardamult = num
    elif c == 2:
        guardasoma2 = num
        guardamult2 = num
    elif num > maior:
        maior = num

while opçao != 5:
    print('''
    [ 1 ] Somar 
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    ''')
    opçao = int(input('qual é a sua opçao? '))
    if opçao == 1:
        print('a soma entre {} e {} e igual {}'.format(guardasoma , guardasoma2, soma))
    elif opçao == 2:
        print('a multiplicação entre {} e {} é igual a {}'.format(guardamult ,guardamult2, mult))
    elif opçao == 3:
        print('o maior numero é o {}.'.format(maior))
    elif opçao == 4:
        for n in range(1, 3):
            num2 = int(input('digite os novos numeros: '))
            soma = soma + num2
            mult = mult * num2
            if n == 1:
                guadasoma = guardasoma + num2
                guardamult = guardamult * num2
            elif n == 2:
                guardasoma2 = guardasoma2 + num2
                guardamult2 = guardamult2 * num2
            elif num2 > maior:
                maior = num2
    elif opçao == 5:
        sleep(0.5)
        print('FINALIZANDO...')
        sleep(1)
    else:
        print('informação inválida!tente novamente.')


