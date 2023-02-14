from random import randint
from time import sleep
def sorteia(lst):
    for n in range(0,5):
        sort = randint(0,9)
        lst.append(sort)
    print("Os números sorteados foram:",end=" ")
    for valor in lst:
        print(valor, end=" ")
        sleep(0.3)
    print('PRONTO!')

def somapar(lst):
    s = 0
    for v in lst:
        if v % 2 == 0:
            s += v
    print(f"Somando os valores pares de {lst},temos: {s}")


numeros = list()
sorteia(numeros)
somapar(numeros)
