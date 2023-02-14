from time import sleep
boletim = list()
dados = list()
while True:
    for c in range(1,3):
        if c == 1:
            dados.append(str(input("Nome: ")))
        dados.append(float(input(f'Nota {c}: ')))
    dados.append((dados[1] + dados[2]) / 2)
    boletim.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in "Nn":
        break
print("=-"*15)
print("No", "   Nome","               Média")
print("-"*30)
for pos, nome_media in enumerate(boletim):
    print(f"{pos:<5}", f"{nome_media[0]}", f"{nome_media[3]:>20}")
print("-"*50)
num = 0
while num != 999:
    num = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if num != 999:
        print(f"Notas de {boletim[num][0]} são {boletim[num][1:3]}")
        print("-"*50)
print("FINALIZANDO O PROGRAMA...")
sleep(1)
print("VOLTE SEMPRE!!")