import re
from datetime import datetime

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
    "Saúde": r"Saúde:[ \t]*([^\r\n]*)$",
    "Religião": r"Religião:[ \t]*([^\r\n]*)$",
    "Raça": r"Raça:[ \t]*([^\r\n]*)$",
    "Opinião Política": r"Opinião Política:[ \t]*([^\r\n]*)$",
    "Orientação Sexual": r"Orientação Sexual:[ \t]*([^\r\n]*)$"
}

niveis_de_riscos = {
    "CPF": "Médio",
    "E-mail": "Médio",
    "Telefone": "Médio",
    "Nome Completo": "Médio",
    "RG": "Médio",
    "Data de Nascimento": "Médio",
    "CEP": "Médio",
    "Endereço IP": "Médio",
    "Saúde": "Alto",
    "Religião": "Alto",
    "Raça": "Alto",
    "Opinião Política": "Alto",
    "Orientação Sexual": "Alto"
}

agora = datetime.now()
relatorio_atual = f"relatorio_{agora.strftime('%Y-%m-%d_%H-%M-%S')}.txt"

with open(f"relatorios/{relatorio_atual}", "w", encoding="utf-8") as relatorio:
    for chave, valor in padroes.items():
        encontrados = re.findall(valor, conteudo, re.MULTILINE)
    
        if encontrados and encontrados[0] != "":
            risco = niveis_de_riscos[chave]
            relatorio.write(f"Dado: {chave} | Encontrado: {encontrados} | Risco: {risco}\n")
            