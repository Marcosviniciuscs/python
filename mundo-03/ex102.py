def fatorial(num, show = False ):
    """
    ->Calcula o fatorial de um número
    :param num: 1º parâmetro: numero que sera usado para saber o fatorial
    :param show: 2º parametro: mostra o calculo quando for verdadeiro.Caso seja falso, nao mostrará o calculo.
    :return: retorna o valor do multiplicador,ou seja , do resultado do calculo do fatorial.
    """
    from time import sleep #escopo de importação
    v = 0
    mult = 1
    print(f"Fatorial de n!{num}:")
    while v < num:
        mult *= num #multiplicador
        if show:
            print(num, end=' x ' if num > 1 else " = ")
            sleep(0.3)
            num -= 1 #decrementa o numero digitado
        else:
            num -= 1
    return mult
    print("=-"*25)

#ex fatorial : 7 * 6 * 5 * 4 * 3 * 2 * 1 = 5040
print(fatorial(5, True))
help(fatorial)