import requests

while True:
    r = requests.get('http://192.168.0.33/')
    r = requests.get('http://192.168.0.33/trabalhador')
    r = requests.get('http://192.168.0.33/equipe')
    r = requests.get('http://192.168.0.33/linguagem')
    r = requests.get('http://192.168.0.33/trabalhador/26')