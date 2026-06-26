# Classificador de Dados Sensíveis

## Funcionalidade

- Um sistema que verifica um arquivo.txt e retornar um relatório contendo todos os possíveis riscos classificados em Médio e Alto.

## Como fazer funcionar

1. Clona esse repositório
2. Acesse a pasta desse projeto
3. Execute o comando python classificador.py
4. Coloque o caminho do seu arquivo como pedido
5. O relatório do arquivo estará salvo na pasta RELATORIOS

## Estrutura do projeto

```
Classificador_dados_sensiveis/
|
|-- dados/
|    |__ amostra_exemplo.txt
|
|-- relatorios/
|
|__ classificador.py
```

## Exemplo no output

```
Relatório da Análise do Arquivo

O arquivo foi gerado na data de: YYYY-MM-DD HH:MM:SS

Os dados vieram do caminho dados/amostra_exemplo.txt

Dado: E-mail | Encontrado: ['exemplo@gmail.com'] | Risco: Médio

Dado: Saúde | Encontrado: ['Asma, Bronquite e Diabete'] | Risco: Alto

ATENÇÃO: Foram encontrados 2 dados no total, sendo 1 de alto risco.
```

## Contexto 

- Esse projeto foi desenvolvido com base nas categorias de dados pessoais e sensíveis definidos pela LGPD.

## Limitações 

- O classificador não consegue detectar em um documento onde está escrito, por exemplo, "o paciente sofre de diabete" sem o prefixo "Saúde:".
- O classificador pode detectar dados incorretos quando os padrões são estruturalmente parecidos.

## Atualizações Futuras

- Pretendo adicionar leituras de outros tipos de arquivos, por exemplo, JSON e CSV.
- Irei implementar no projeto detecção por palavras-chaves e NLP para identificar com mais clareza dados sensíveis em texto livre, sem depender de prefixos.