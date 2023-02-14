import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não esta acessivel no momento!')
else:
    print('Consegui acessar o site pudim com sucesso!')
    #print(site.read()) : lê o conteúdo html
