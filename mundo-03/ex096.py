def area(larg, compr):
    a = larg * compr
    print(f"A Área de um terreno {larg}x{compr} e igual: {a} m²")


print('controle de terrenos')
print('-' * 30)
l = float(input('Largura: M '))
c = float(input('Comprimento: M '))
area(l, c)

