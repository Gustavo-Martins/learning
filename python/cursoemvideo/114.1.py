"""Checks Pudim.com.br status."""
import urllib.request


try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("O site Pudeim não está acessível no momento.")
else:
    print("Consegui acessar o site Pudim com sucesso.")
    print(site.read())
