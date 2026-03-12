import pandas as pd

# Carregar o ficheiro
df = pd.read_csv('lutadores.csv',sep=',')

# Visualizar as primeiras 5 linhas
#print(df.head())
print()
#print(df.to_string())
#print(df)
for linha in df.values:
    print(linha) # Imprime cada linha como um array
print()
# for index, linha in df.iterrows():
#      print(linha)

print()

'''df = pd.read_csv(
    'lutadores.csv', 
    sep=',', 
    encoding='utf-8',
    #parse_dates=['data_venda'],
    #index_col='id_transacao'
)

# Verificar informações sobre as colunas e tipos de dados
print(df.info())
'''
'''
import pandas as pd

# Define o tamanho de cada pedaço (ex: 10.000 linhas por vez)
tamanho_pedaco = 10000

# O parâmetro chunksize transforma a leitura num iterador
leitor = pd.read_csv('arquivo_gigante.csv', chunksize=tamanho_pedaco)

for pedaco in leitor:
    # Processa cada parte do arquivo individualmente
    print(f"A processar bloco de {len(pedaco)} linhas...")
    # Exemplo: somar uma coluna ou filtrar dados
'''
import pandas as pd
import os

# Nome do ficheiro
file_name = 'lutadores.csv'

# 1. Criar um novo dado (um dicionário ou DataFrame)
novo_lutador = {
    'Nome': ['Charles Oliveira'],
    'Categoria': ['Leve'],
    'Vitórias': [34]
}
df_novo = pd.DataFrame(novo_lutador)

# 2. Escrever no ficheiro em modo 'append' (anexar)
# mode='a' -> abre o ficheiro para acrescentar no fim
# index=False -> não guarda o número da linha
# header=False -> não repete o cabeçalho (Nome, Categoria, etc)
# encoding='utf-8' -> garante que caracteres especiais funcionem

# Verificamos se o ficheiro já existe para decidir se escrevemos o cabeçalho
file_exists = os.path.isfile(file_name)

df_novo.to_csv(
    file_name, 
    mode='a', 
    index=False, 
    header=not file_exists, 
    encoding='utf-8'
)

print(f"Dados adicionados com sucesso em {file_name}!")

# --- DICA EXTRA: Usando Python Standard (Sem Pandas) ---
# Se for apenas para adicionar uma linha simples, o módulo 'csv' é mais leve:
import csv

def adicionar_linha_simples(nome, categoria, vitorias):
    with open(file_name, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([nome, categoria, vitorias])

# adicionar_linha_simples('Alex Poatan', 'Meio-Pesado', 10)