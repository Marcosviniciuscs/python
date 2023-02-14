pilha = []
expr = str(input('Digite uma expressão: '))
expr.split()
for pos in range(0, len(expr)):
    if expr[pos] == "(":
        pilha.append(expr[pos])
    elif expr[pos] == ")":
        if "(" in pilha:
            pilha.pop()
        else:
            pilha.append(expr[pos])
if len(pilha) == 0:
    print("os parenteses estão inseridos corretamente")
elif len(pilha) > 0:
    print("Os parenteses nao estão inseridos corretamente.")
print(pilha)
