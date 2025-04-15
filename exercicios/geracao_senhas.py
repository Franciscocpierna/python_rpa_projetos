"""
13. Crie um programa que:

- Solicite ao usuário que insira o tamanho desejado para a senha.
- Gere uma senha aleatória de acordo com o tamanho informado.
- A senha pode conter letras maiúsculas, minúsculas, números e 
            caracteres especiais.
"""

# Importando módulos necessários:
import random  # Módulo para gerar dados aleatórios.
import string  # Módulo que contém sequências de caracteres 
        # comuns como letras e dígitos.

# Definição da função 'gerar_senha' que aceita um parâmetro: 'tamanho'.
def gerar_senha(tamanho):
    
    # Concatena strings de caracteres alfabéticos (maiúsculas e 
            # minúsculas), numéricos e símbolos.
    # 'string.ascii_letters' inclui todas as letras 
            # de A a Z (maiúsculas e minúsculas).
    # 'string.digits' inclui todos os dígitos de 0 a 9.
    # 'string.punctuation' inclui todos os caracteres de 
            # pontuação como !, @, #, etc.
    caracteres = string.ascii_letters + string.digits + string.punctuation
    print(caracteres)  # Exibe os caracteres disponíveis para a senha.
    # Gera a senha usando uma compreensão de lista:
    # 'random.choice(caracteres)' seleciona um caractere 
            # aleatório da string 'caracteres'.
    # 'for i in range(tamanho)' repete a seleção 'tamanho' 
            # vezes para formar uma senha do comprimento desejado.
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    
    # Retorna a senha gerada.
    return senha

# Bloco principal do programa, executado ao iniciar o script.
try:
    
    # Solicita ao usuário para digitar o tamanho da 
            # senha que deseja.
    # 'int(input(...))' converte a entrada do usuário para um 
            # inteiro, necessário para o loop.
    tamanho_senha = int(input("Digite o tamanho desejado para a senha: "))
    
    # Verifica se o tamanho da senha é ao menos 1, já que não é 
            # possível ter uma senha de tamanho zero ou negativo.
    if tamanho_senha < 1:

        # Aviso caso o tamanho seja inapropriado.
        print("O tamanho da senha deve ser maior que zero!")  
        
    else:
        
        # Chama a função 'gerar_senha' com o tamanho fornecido e 
                # armazena o resultado em 'senha_gerada'.
        senha_gerada = gerar_senha(tamanho_senha)
        
        # Exibe a senha gerada.
        print(f"Senha gerada: {senha_gerada}")

except ValueError:
    
    # Captura erro caso a conversão para inteiro falhe, o que 
            # acontece se o usuário não digitar um número.
    print("Entrada inválida! Por favor, insira um número inteiro.")