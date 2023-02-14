soma = 0 #acumulador
cont = 0 #contador
maior = 0 # homen mais velho / guarda os numeros
nomemaisv = '' # é como se fosse um acumulador ,mas ...de string
total = 0# total de mulheres com menos de 20 anos
for p in range(1, 5):
    print('{} pessoa{}'.format(p,'\=' *10))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).upper()
    soma = soma + idade
    cont = cont + 1
    if sexo == 'M': #colocando o M entre apas ,eu indico que é uma string(letra),e consigo fazer a compração com a variavel 'sexo' que tambem é uma string.
        if idade > maior:
            maior = idade #guarda a informação daquele ponto do laço ex: 1 ou segunda execução do laço
            nomemaisv = nome
    elif sexo == 'F': #a letra entre aspas indica que é uma string
        if idade < 20:
            total = total + 1 #conta quantas vezes ha mulheres com menos de 20 anos no laço .
print('o grupo possui uma idade média de {} anos'.format(soma / cont))
print('o homen com a maior idade tem {} anos e o seu nome é {}'.format(maior,nomemaisv))
print('neste grupo tem {} mulheres com menos de 20 anos.'.format(total))
