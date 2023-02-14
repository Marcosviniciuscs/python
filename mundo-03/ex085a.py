lista = [[], []]
for c in range(1, 8):
    num = int(input(f"informe o {c}º número: "))
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 == 1:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f"Os números pares digitados foram: {lista[0]}")
print(f"Os números ímpares digitados foram: {lista[1]}")
