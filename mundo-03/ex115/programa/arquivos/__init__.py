from ex115.programa.interface import *
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')#tenta abrir um arquivo
        a.close()#rt: leitura e texto
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')#escreve um arquivo de texto
        a.close()# + cria um arquivo
    except:
        print('Houve um ERRO na criação de arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabeçalho('Pessoas CADASTRADAS')
        print(a.read())
