valores = (int(input('informe o primeiro valor: ')),
           int(input('informe o segundo valor: ')),
           int(input('informe o terceiro valor: ')),
           int(input('informe o ultimo valor: ')))
print(f'o 9 apareceu {valores.count(9)} vezes.')
if 3 in valores: #se o 3 estiver dentro da tupla...
    print(f'o 3 foi digitado na {valores.index(3) + 1 }ª posição ')
else:
    print('o valor 3 não foi encontrado.')
print('os números pares digitados foram: ',end=' ')
for c in range(0, len(valores)):
    if valores[c] % 2 == 0:
        print(valores[c],end=' ')
