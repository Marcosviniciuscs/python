def aumentar(preço=0, taxa=0, mostrar=False):
    '''
    -> calcula o aumento do preço de acordo com a taxa.
    :param preço: Parãmetro que o usuário informa
    :param taxa:  Valor que será acrescentado
    :param mostrar: formata a moeda para brl ou nao (se estiver em 'true')
    :return: retorna a moeda formatada ou nao ,de acordo com o parametro acima.
    '''
    cal = preço + (preço * taxa / 100)
    return cal if mostrar is False else moeda(cal)


def diminuir(preço=0, taxa=0, mostrar=False):
    '''
    -> reduz o valor do preço de acordo com a taxa
    :param preço: Valor informado pelo usuário
    :param taxa: Quanto que será reduzido
    :param mostrar: Se for verdadeiro mostrará a moeda formatada
    :return: retorna o resultado do calculo .
    '''
    cal = preço - (preço * taxa / 100)
    return cal if mostrar is False else moeda(cal)


def dobro(preço=0, mostrar=False):
    '''
    ->Dobra o preço
    :param preço: valor informado pelo usuário
    :param mostrar: se for verdadeiro mostrará a moeda formatada
    :return: retorna o resultado formatado
    '''
    cal = preço * 2
    return cal if mostrar is False else moeda(cal)


def metade(preço=0, mostrar=False):
    '''
    ->Informa a metade do valor
    :param preço: valor informado pelo usuário
    :param mostrar: se for verdadeiro mostrará a moeda formatada
    :return: Retorna o resultado formatado
    '''
    cal = preço / 2
    return cal if mostrar is False else moeda(cal)


def moeda(preço, moeda="R$"):
    '''
    ->formata a moeda
    :param preço: valor informado pelo usuário
    :param moeda: Mostra o tipo da moeda(Reais,dolar)
    :return:
    '''
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxa1=10, taxa2=5):
    print('-'*30)
    print(f'{"Resumo do Valor"}'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço:  \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxa1}% de Aumento:  \t{aumentar(preço, taxa1, True)}')
    print(f'{taxa2}% de Redução:  \t{diminuir(preço, taxa2, True)}')
    print('-'*30)

