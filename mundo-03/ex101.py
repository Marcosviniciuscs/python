def voto(ano_nasc):
    from datetime import date #escopo de importação econômiza memória ,pois será utilizada durante a execução da def
    data_atual = date.today().year  # escopo local
    idade = data_atual - nasc #escopo local
    if idade <= 15:
        return f"Com {idade} anos: Não vota!"
    if idade >= 16 and idade < 18:
        return  f"Com {idade} anos: Voto opicional!"
    if idade > 18 and idade < 70:
        return f"Com {idade} anos: Voto obrigatório"
    else:
        return f"Com {idade} anos :Voto opicional"


nasc = int(input("Ano de nascimento: "))
print(voto(nasc)) #return : retorna o resultado para o lugar de onde foi passado o parametro
