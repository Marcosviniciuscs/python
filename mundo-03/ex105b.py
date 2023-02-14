def nota(*num,sit=False):
    """
    -> FUNÇÃO QUE ANALISA AS NOTAS DA TURMA
    :param num: FORAM PASSADOS VÁRIOS VALORES (PARÂMETROS)
    :param sit: MOSTRA A SITUAÇÃO DA TURMA(OPICIONAL)
    :return: RETORNA AS INFORMAÇÕES DO DICIONÁRIO
    """
    dc = dict()
    dc['Total'] = len(num)
    dc['Maior'] = max(num)
    dc['Menor'] = min(num)
    dc['Media'] = sum(num) / len(num)
    if sit:
        if dc['Media'] < 5:
            dc['Situação'] = "RUIM"
        elif dc['Media'] >= 5 and dc['Media'] < 7:
            dc['Situação'] = "Regular"
        else:
            dc['Situação'] = "Boa"
    return dc


resp = nota(5,10,8,sit=True)
print(resp)
help(nota)