tabela = ('Bragantino','Bahia','Ceará SC','Fortaleza',
         'athletico PR','Flamengo','atlético-GO','Sport recife',
         'Juventude','Cuibá','internacional','São paulo',
         'Fluminense','Grêmio','Atlético-MG','America-MG',
         'Palmeiras','Corinthians','Chapecoense','Santos')
print(f'tabela do brasileirão 2021: {tabela}')
print('==='*20)
print(f'Os cinco primeiros times 72do campeonato: {tabela[:5]}')
print('==='*20)
print(f'Os útimos 4 colocados: {tabela[16:]}')
print('==='*20)
print(f'Times em ordem alfabeticas: {sorted(tabela)}')
print('==='*20)
for pos, time in enumerate(tabela):
    if time == 'Chapecoense':
        print(f'o time {time} esta na posição {pos + 1}º')

