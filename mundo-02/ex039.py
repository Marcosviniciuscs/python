from datetime import date
ano = int(input('em qual ano voce nasceu: '))
data = date.today().year
idade = data - ano
if idade < 18:
    print('voce tem {} anos ,ainda falta {} anos para o seu alistamento.'.format(idade,(18 - idade)))
elif idade == 18:
    print('voce tem 18 anos .entao aliste-se imediatamente.')
elif idade > 18:
    print('você tem {} anos ,e ja se passaram {} anos.'.format(idade,idade - 18))
    tempo = data - (idade - 18)
    print('a solicitação do seu alistamento deveria ter ocorrido em {}.'.format(tempo))
