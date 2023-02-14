pessoas = list()
dados = list()
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    pessoas.append(dados[:])
    dados.clear()
    opcao = str(input("quer continuar? [S/N] "))
    if opcao in "Nn":
        break
print(f"Foram cadastradas {len(pessoas)} pessoas .")
pesomax = []
pesomin = []
nome1 = []
nome2 = []
for pos , valor in enumerate(pessoas):
    if pos == 0:
        pesomax.append(valor[1])
        pesomin.append(valor[1])

    if valor[1] == pesomax[0]: #sempre que o valor for igual ,vai apenas adcionar um novo nome
        pesomax.clear()
        pesomax.append(valor[1])
        nome1.append(valor[0])
    elif valor[1] > pesomax[0]:#caso, o valor do peso seja maior,ele irá apagar os dados de pesomax e nome1 ,adicionando peso e nomes novos
        pesomax.clear()
        pesomax.append(valor[1])
        nome1.clear()
        nome1.append(valor[0])

    if valor[1] == pesomin[0]:
        pesomin.clear()
        pesomin.append(valor[1])
        nome2.append(valor[0])
    elif valor[1] < pesomin[0]:
        pesomin.clear()
        pesomin.append(valor[1])
        nome2.clear()
        nome2.append(valor[0])
print(f"As pessoas mais pesadas foram : {nome1} com {pesomax} kilos")
print(f"As pessoas  mais leves foram: {nome2} com {pesomin} kilos")

