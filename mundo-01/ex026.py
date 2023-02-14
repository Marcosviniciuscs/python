frase = str(input('digite algo: ')).strip().upper()
c = frase.count('A')
print('nessa frase aparece ão todo {} vezes a letra A'.format(c))
pr = frase.find('A') + 1
print('a primeira letra A esta localizada na posição {}'.format(pr))
ul = frase.rfind('A') + 1
print('a ultima letra A esta localizada {}'.format(ul))


