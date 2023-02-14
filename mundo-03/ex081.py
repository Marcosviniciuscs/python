num = 0
opcao = " "
lista = []
while True:
    lista.append(int(input('digite um número: ')))
    opcao = str(input('deseja continuar? [S/N]  ')).upper()
    while opcao not in "SN":
        opcao = str(input('informacao inválida.informe [S/N]')).upper()
    if opcao == "N":
        break
print(f"foram digitados {len(lista)} números ")
lista.sort(reverse = True)
print(f"Os números em ordem descrescente: {lista}")
if 5 in lista:
    print('o 5 se encontra na lista!')
else:
    print('o 5 não se encontra na lista')



