frase = str(input('digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print('o inverso da palavra {} é {}'.format(junto,inverso))
if junto == inverso:
    print('temos um políndromo!')
else:
    print('não temos um políndromo!')
