import plotly.express as px
import plotly.io as pio
import os
import pandas as pd
import plotly.express as px
import tempfile
import webbrowser
data = pd.read_csv("dataset/train.csv")

print(data.head())
print()
print()
data.head()

# --- CONFIGURAÇÃO DE SEGURANÇA ---
# Em vez de depender do servidor local (127.0.0.1) que causa ERR_CONNECTION_REFUSED,
# vamos salvar o gráfico como um arquivo temporário e abri-lo.

def mostrar_grafico_estavel(fig, nome_arquivo="temp_plot"):
    # 1. Cria um caminho para um arquivo HTML na pasta temporária do Windows
    temp_dir = tempfile.gettempdir()
    caminho_arquivo = os.path.join(temp_dir, f"{nome_arquivo}.html")
    
    # 2. Salva o gráfico como HTML (contém todo o JavaScript necessário dentro dele)
    fig.write_html(caminho_arquivo)
    
    # 3. Abre o arquivo diretamente no navegador padrão
    # Isso usa o protocolo 'file://' em vez de 'http://', eliminando erros de conexão
    webbrowser.open(f"file://{caminho_arquivo}")
    print(f"Gráfico gerado em: {caminho_arquivo}")

# --- EXEMPLO DE USO COM O SEU GRÁFICO ---

# Simulando seus dados
# data = px.data.iris() # Substitua pelo seu 'data'

# fig = px.box(data, 
#              x="species", 
#              y="sepal_width", 
#              color="species",
#              title="Estudo de Caso - Renderização Garantida",
#              points=False) # 'points=False' deixa o arquivo mais leve

# fig.update_traces(quartilemethod="exclusive")

# EM VEZ DE fig.show(), use a nossa nova função:
#mostrar_grafico_estavel(fig)

fig = px.box(data, 
             x="Credit_Score", 
             y="Num_of_Loan", 
             color="Credit_Score", 
             title="Score de Crédito baseado no número de Emprestimos Tomados por Pessoa",
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
mostrar_grafico_estavel(fig) # #fig.show() essa substituiu fig.show()