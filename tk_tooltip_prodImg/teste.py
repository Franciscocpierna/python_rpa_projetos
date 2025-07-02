import os
nome = "Tênis+Feminino.jpg" 
print("Arquivos na pasta 'imagem':")

if nome in os.listdir("C:\\python_projetos\\python_rpa_projetos\\tk_tooltip_prodImg\\imagem"):
    print(nome)
else:
    print("imagem não encontrada")  
    
    
     

# import os
 
# def localizar_imagem(produto, pasta="imagem"):
#     produto_base = produto.lower().replace(" ", "").replace("ê", "e").replace("í", "i")
 
#     for nome in os.listdir(pasta):
#         nome_base = nome.lower().replace(" ", "").replace("+", "").replace("-", "").replace("ê", "e").replace("í", "i")
#         if produto_base in nome_base:
#             return os.path.join(pasta, nome)
#     return None
 
# # Exemplo de uso:
# produto = "Tênis+Feminino"
# caminho_imagem = localizar_imagem('C:\python_projetos\\python_rpa_projetos\\tk_tooltip_prodImg\\imagem\\produto')
 
# if caminho_imagem and os.path.exists(caminho_imagem):
#     print("Imagem localizada:", caminho_imagem)
# else:
#     print("Imagem NÃO encontrada para:", produto)