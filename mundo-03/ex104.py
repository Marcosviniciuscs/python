def leiaInt(msg):
    num = str(input(msg))
    if num.isnumeric():
        valor = num
    else:
        while True:
            num = str(input("\033[1;31mErro.Informe um número: \033[m"))
            if num.isnumeric():
                valor = num
                break
    return valor

n = leiaInt('Digite um n: ')
print('=-'*20)
print(f"FOI INFORMADO O NÚMERO {n}")
