def voto(ano_nasc):
    from datetime import date
    data_atual = date.today().year
    idade = data_atual - ano_nasc
    if idade < 15:
        return f"Com {idade} anos, Não vota!"
    if idade >= 16 and idade <= 18:
        return f"Com {idade} anos, Voto facultativo!"
    if idade > 18 and idade <= 70:
        return f"Com {idade} anos, Voto obrigatório!"
    if idade > 70:
        return f"Com {idade} anos, Voto facultativo!"


nasc = int(input("Ano de nascimento: "))
resp = voto(nasc)
print(resp)

