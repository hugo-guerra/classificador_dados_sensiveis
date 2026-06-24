import re

with open("dados/amostra.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

padroes = {
    "CPF": r"\d{3}\.\d{3}\.\d{3}-\d{2}",
    "E-mail": r"\w+@\w+\.\w+",
    "Telefone": r"\(\d{2}\)\s\d{4,5}-\d{4}"
}

for chave, valor in padroes.items():
    encontrados = re.findall(valor, conteudo)
    print(chave, encontrados)