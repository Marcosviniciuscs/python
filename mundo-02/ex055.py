maior = 0
maior2 = 0
maior3 = 0
for p in range(1,4):
    peso = float(input('peso da {} pessoa: '.format(p)))
    if p == 1:#quando o 'p' for igual a 1 , o peso sera guardado dentro da variavel 'maior3'
        maior3 = peso
        print(maior3)
    if p == 2: #a partir dessa logica, eu consigo guardar o numero do segundo laço com objetivo de analizar ,comparar...
        maior = peso
        print(maior)
    elif p == 3:
        maior2 = peso
        print(maior2)
