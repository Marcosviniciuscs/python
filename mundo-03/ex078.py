lista = list()
for cont in range(0, 5):
    lista.append(int(input(f'digite um valor para posição {cont}: ')))
print(f'o maior valor foi o {max(lista)} e está na posiçõa {lista.index(max(lista))}')
print(f'o menor valor foi o {min(lista)} e está na posição {lista.index(min(lista))}')
