def aumentar(preço=0, taxa=0):
    cal = preço + (preço * taxa / 100)
    return cal


def diminuir(preço=0, taxa=0):
    cal = preço - (preço * taxa / 100)
    return cal


def dobro(preço=0):
    cal = preço * 2
    return cal


def metade(preço=0):
    cal = preço / 2
    return cal


def moeda(preço, moeda="R$"):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

