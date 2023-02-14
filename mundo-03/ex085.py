lista = [[], []]
for c in range(1,8):
    num = int(input(f'informe o {c}º número: '))
    if num % 2 == 0:
        if len(lista[0]) == 0:
            lista[0].append(num)
        if num > lista[0][-1]:
            lista[0].append(num)
        else:
            pos = 0
            while num < lista[0][pos]:
                lista[0].insert(pos, num)
                break
            pos += 1
    elif num % 2 == 1:
        if len(lista[1]) == 0:
            lista[1].append(num)
        if num > lista[1][-1]:
            lista[1].append(num)
        else:
            pos = 0
            while num < lista[1][pos]:
                lista[1].insert(pos, num)
                break
            pos += 1
print(f"Os números pares digitados foram: {lista[0]}")
print(f"Os números ímpares digitados foram: {lista[1]}")


