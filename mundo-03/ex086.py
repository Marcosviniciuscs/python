lista = [[], [], []]
for c in range(0,3):
    lista[0].append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0,3):
    lista[1].append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0,3):
    lista[2].append(int(input(f"Digite um valor para [2, {c}]: ")))
print(f"""
[ {lista[0][0]} ] [ {lista[0][1]} ] [ {lista[0][2]} ]
[ {lista[1][0]} ] [ {lista[1][1]} ] [ {lista[1][2]} ]
[ {lista[2][0]} ] [ {lista[2][1]} ] [ {lista[2][2]} ]
""")
