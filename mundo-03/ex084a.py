principal = list()
temp = list()
max = 0
min = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(principal) == 0:
        max = temp[1]
        min = temp[1]
    else:
        if temp[1] > max:
            max = temp[1]
        elif temp[1] < min:
            min = temp[1]
    principal.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in "Nn":
        break
print("*"*25)
print(f"Foram cadastrados {len(principal)} pessoas")
print(f"A pessoa mais pesada possui {max} kg . peso de ", end=" ")
for p in principal:
    if p[1] == max:
        print(f"{p[0]},",end=" ")
print(f"\nA pessoa mais leve possui {min} kg. peso de",end=" ")
for p in principal:
    if p[1] == min:
        print(f"{p[0]},")

