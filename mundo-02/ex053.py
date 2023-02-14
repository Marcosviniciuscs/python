frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = '' #acumulador para str
for letra in range(len(junto) -1, -1,-1):
    inverso += junto[letra]
print('o inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('temos um palíndromo!')
else:
    print('a frase não é um palíndromo!')