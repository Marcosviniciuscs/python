tabela = ('flamengo','internacional','atlético-MG','são paulo',
         'fluminense','grêmio','palmeiras','santos','athletico-pr',
         'bragantino','ceará sc','corinthians','atlético-go',
         'bahia','sport recife','fortaleza','vasco da gama','goiás',
         'coritiba','botafogo')
print('Lista dos times do brasileirão: ')
print(tabela)
print('=='*35)
print('Os CINCO primeiros times: ')
for cont in range(0, 5):
    print(f'{cont + 1}º', tabela[cont], end=' => ' if cont != 4 else ' ')
print('\n','=='*35)
print('Os ultimos QUATRO colocados: ')
for cont in range(-4, 0):
    print(tabela[cont], end=' -=> ' if cont != -1 else ' ')
print('\n','=='*35)
print('times em ordem alfabéticas: ')
print(sorted(tabela))
print('=='*35)
posição = int(tabela.index('santos')) + 1
print('o {} esta na {}º posição. '.format(tabela[posição - 1], posição))
