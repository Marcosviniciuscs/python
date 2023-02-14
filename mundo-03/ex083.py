pilha = list()
expr = str(input('Digite uma expressao: '))
for simb in expr:
    if simb == "(":
        pilha.append(simb)
    elif simb == ")":
        if "(" in pilha:
            pilha.pop()
        else:
            pilha.append(simb)
if len(pilha) == 0:
    print("os parentes estao inseridos corretamente.")
else:
    print("Os parentes nao estão corretos.")
print(pilha)
