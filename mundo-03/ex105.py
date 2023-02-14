def notas(*valores, sit=False):
    '''
    ->programa que analisa as notas do alunos
    :param valores: Números que serão desempacotados e lidos(
    o asteristico informa que vai ser lidos varios parâmetros ou vários números)
    :param sit: Mostra a situação da turma
    :return: Retorna as informações do dicionário
    '''
    dc = dict()
    maior = 0
    menor = 0
    soma = 0
    pos = 0
    for v in valores:#varredura do parâmetro 'valores'
        if pos == 0:
            maior = v
            menor = v
        else:
            if v > maior:
                maior = v
            else:
                if v < menor:
                    menor = v
        soma += v #acumulador
        pos += 1 #contador ou incremento
    media = soma / len(valores)
    dc["total"] = len(valores) #total de notas
    dc["maior"] = maior
    dc['menor'] = menor
    dc['média'] = media
    if media < 5: #situação
        a = "Reprovado"
    elif media >= 5 and media < 7:
        a = "recuperação"
    elif media >= 7:
        a = "Aprovado"
    if sit:
        dc['Situação'] = a
    return dc #dicionario


resp = notas(5,8,1,6,sit=True)
print(resp)
print(notas.__doc__)
