matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_coluna3 = 0
maisegunda_linha = 0
#insere os valores na lista matriz
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um número para [{l}, {c}]: "))
print("*"*35)
#usa o for novamente para formatar a tabela
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end=" ")
    print()
print("*"*35)
#for usado para somar os valores pares , somar os valores da coluna 3 e mostrar o maior valor da linha 2
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if c == 2:
            soma_coluna3 += matriz[l][c]
        if l == 1:#segunda linha vista na matrix printada
            if c == 2:
                maisegunda_linha = matriz[l][c]
            elif matriz[l][c] > maisegunda_linha:
                maisegunda_linha = matriz[l][c]
print(f"A soma dos valores pares e igual a: {soma_pares}")
print(f"A soma da terceira coluna é igual a: {soma_coluna3}")
print(f"O maior número da linha 2 é o {maisegunda_linha}")

