def aumentar(preço=0, taxa=0, mostrar=True):
    cal = preço + (preço * taxa / 100)
    if mostrar == True:
        return moeda(cal)
    else:
        return cal


def diminuir(preço=0, taxa=0, mostrar=True):
    cal = preço - (preço * taxa / 100)
    if mostrar == True:
        return moeda(cal)
    else:
        return cal


def dobro(preço=0, mostrar=True):
    cal = preço * 2
    if mostrar == True:
        return moeda(cal)
    else:
        return cal


def metade(preço=0, mostrar=True):
    cal = preço / 2
    if mostrar == True:
        return moeda(cal)
    else:
        return cal


def moeda(preço, moeda="R$"):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

