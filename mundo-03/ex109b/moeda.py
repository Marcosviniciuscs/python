def aumentar(preço=0, taxa=0, mostrar=False):
    cal = preço + (preço * taxa / 100)
    return cal if mostrar is False else moeda(cal)


def diminuir(preço=0, taxa=0, mostrar=False):
    cal = preço - (preço * taxa / 100)
    return cal if mostrar is False else moeda(cal)


def dobro(preço=0, mostrar=False):
    cal = preço * 2
    return cal if mostrar is False else moeda(cal)


def metade(preço=0, mostrar=False):
    cal = preço / 2
    return cal if mostrar is False else moeda(cal)


def moeda(preço, moeda="R$"):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

