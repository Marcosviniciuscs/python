from random import randint
from time import sleep
palpites = []
temp = []
print("="*40)
print("{:^40}".format("JOGA NA MEGA SENA"))
print("="*40)
num = int(input("Quantos jogos você quer que sorteie? "))
sorteio = 1
while sorteio <= num:
    while True:#nesse caso ,nao sabemos quais números serao gerados.Esse while vai ajudar a gerar  novos numeros para compara-los no if
        numsorteado = randint(1,60)
        if numsorteado not in temp:# se o numero nao estiver na lista "temp",ele será adicionado
            temp.append(numsorteado)
        if len(temp) == 6:#quando um total de 6 numeros forem adicionados na lista temp , o loop vai ser interrompido
            palpites.append(temp[:])
            temp.clear()
            sorteio += 1
            break
print("=-"*5,f" SORTEANDO {num} JOGOS ","-="*5)
for pos,n in enumerate(palpites):
    print(f"Jogo {pos+1}: {n}")
    sleep(1)
print("=-"*6,f"<  BOA SORTE  >","-="*6)
