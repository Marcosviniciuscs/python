palavras = ('APRENDER','PROGRAMAR','LINGUAGEM',
            'PYTHON','CURSO','GRATIS','ESTUDAR',
            'PRATICAR','TRABALHAR','MERCADO',
            'PROGRAMADOR','FUTURO')
for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p: #dediquei uma variavel para ler a palavra,pois cada palavra é uma lista .assim ,eu consigo ler as vogais.
        if letra in 'AEIOU':#se a letra analisada for :a,e,i,o ou u ,escrever na tela .
            print(letra,end=" ")



