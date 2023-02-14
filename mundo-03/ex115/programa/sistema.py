from interface import menu
from interface import validaçãoInt
from interface import cabeçalho
from ex115.programa.arquivos import arquivoExiste
from ex115.programa.arquivos import criarArquivo
from ex115.programa.arquivos import lerArquivo
from time import sleep

#programa principal
arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
   criarArquivo(arq)
cadastro = list()
while True:
    cabeçalho("Menu Principal")
    menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema', 'Atutalizar sistema'])
    n = validaçãoInt()
    if n == 1:
        lerArquivo(arq)
        print(f'{"Nome":<10} {"Idade":>24}')
        for pessoa in cadastro:
            print(f'{pessoa[0]:<10} {pessoa[1]:>24}')

    elif n == 2:
        nome = str(input('Nome: '))
        idade = validaçãoInt()

        print("Dados cadastrados com sucesso!")

    elif n == 3:
        print(f'Finalizando o programa...')
        sleep(1)
        print('Até mais!')
        break
