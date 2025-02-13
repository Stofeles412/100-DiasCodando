import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://receitas.globo.com/receitas-da-tv/mais-voce/pudim-de-leite-condensado-4d514bb052e0b252bc00e85a.ghtml')
except:
    print("Erro, o site pudim não estar acessivel")
else:
    print("site pudim estar acessivel")
    print(site.read())