lista = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS',
      'ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
for palavra in  lista:
    print(f'\nna palavra {palavra} temos ',end=' ')
    for letra in palavra:
        if letra in "AEIOU":
            print(letra,end=' ')
