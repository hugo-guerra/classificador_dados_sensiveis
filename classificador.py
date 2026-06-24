import re

with open("dados/amostra.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

padroes = {
    "CPF": r"CPF:\s*(\d{3}\.\d{3}\.\d{3}-\d{2})",
    "E-mail": r"E-mail:\s*([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)",
    "Telefone": r"Telefone:\s*(\(\d{2}\)\s?\d{4,5}-\d{4})",
    "Nome Completo": r"Nome:\s*([A-Za-zÀ-ÿ]+(?: [A-Za-zÀ-ÿ]+)+)",
    "RG": r"RG:\s*(\d{2}\.\d{3}\.\d{3}-\d{1})",
    "Data de Nascimento": r"Data de Nascimento:\s*(\d{2}/\d{2}/\d{4})",
    "CEP": r"CEP:\s*(\d{5}-\d{3})",
    "Endereço IP": r"IP:\s*((?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})",
    "Saúde": r"Saúde:\s*(.*)",
    "Religião": r"Religião:\s*(.*)",
    "Raça": r"Raça:\s*(.*)",
    "Opinião Política": r"Opinião Política:\s*(.*)",
    "Orientação Sexual": r"Orientação Sexual:\s*(.*)"
}

niveis_de_riscos = {
    "CPF": "Risco: Médio",
    "E-mail": "Risco: Médio",
    "Telefone": "Risco: Médio",
    "Nome Completo": "Risco: Médio",
    "RG": "Risco: Médio",
    "Data de Nascimento": "Risco: Médio",
    "CEP": "Risco: Médio",
    "Endereço IP": "Risco: Médio",
    "Saúde": "Risco: Alto",
    "Religião": "Risco: Alto",
    "Raça": "Risco: Alto",
    "Opinião Política": "Risco: Alto",
    "Orientação Sexual": "Risco: Alto"
}

for chave, valor in padroes.items():
    encontrados = re.findall(valor, conteudo)
    print(f"O {niveis_de_riscos[chave]} para {padroes[chave]}{encontrados}")