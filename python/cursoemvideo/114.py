"""Checks Pudim.com.br status."""
import urllib.request


site = "http://www.pudim.com.br"

try:
    code = urllib.request.urlopen(site).getcode()
    if code == 200:
        print("O site pudim está acessível no momento.")
except:
    print("O site Pudim não está acessível no momento.")
