from acesso_cep import BuscaEndereco

cep = 38810000
objeto_cep = BuscaEndereco(cep)

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)

# import requests

# r = requests.get("https://viacep.com.br/ws/01001000/json/")
# print(r.text)