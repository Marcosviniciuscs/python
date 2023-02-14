tabela = ('corinthians','cuiabá','são paulo','coritiba','america MG','atlértico MG',
          'ceará sc','avai','fluminense','bragantino','flamengo','atletico go','santos',
          'palmeiras','juventude','goiás','fortaleza','botafogo','internacional','athletico-pr')
print('tabela do campeonato 2022:\n {}'.format(tabela))
print('Os cincos primeiros colocados:\n {}'.format(tabela[0:5]))
print('Os ultimos quatro da tabela:\n  {}'.format(tabela[-4:]))
print('Os times em ordem alfabetica:\n {}'.format(sorted(tabela)))
print('O  avai esta na posição {}'.format(tabela.index('avai')+ 1))
