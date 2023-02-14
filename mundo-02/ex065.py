resp = 'S'
soma = 0
quant = 0
maior = 0
menor = 0
while resp in 'Ss':# o 'in' pergunta se tem o valor dentro da variavel ,utilizado como paramêtro de comparação dentro da string que contem o 's'.
    num = int(input('digite um número: '))
    resp = str(input('quer continuar? [s/n]  ')).lower().strip()[0]
    quant = quant + 1
    soma = soma + num
    if quant == 1:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
média = soma / quant
print('a média dos valores digitados é {:.1f}'.format(média))
print('o maior número foi {} e o menor {}'.format(maior, menor))
