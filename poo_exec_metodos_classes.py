
print("Exercício: Formatador de Frases em Python")

"""
Exercício: Formatador de Frases em Python

Objetivo:

Neste exercício, você será desafiado a criar uma aplicação Python 
que ajuda os usuários a formatar frases de diversas maneiras. A aplicação 
deve oferecer opções para converter toda a frase para maiúsculas ou minúsculas, 
capitalizar a primeira letra, transformá-la em um título, contar 
vogais e consoantes, e mais.

Requisitos:

    Crie uma classe chamada FormatadorDeFrase que será responsável por 
    todas as operações de formatação.

    1. A classe deve possuir os seguintes métodos:
    
        para_maiusculas(): converte toda a frase para maiúsculas.
        para_minusculas(): converte toda a frase para minúsculas.
        capitalizar(): capitaliza a primeira letra da frase.
        formato_titulo(): converte a primeira letra de cada palavra da frase para maiúscula.
        contar_vogais(): conta e retorna o número de vogais na frase.
        contar_consoantes(): conta e retorna o número de consoantes na frase.
        contar_letra_a(): conta e retorna o número de ocorrências da letra 'a' na frase.
        procurar_palavra(palavra): conta e retorna o número de ocorrências de uma palavra específica na frase.
        obter_frase(): retorna a frase atual.

    2. Implemente uma função menu que serve como interface do usuário. Essa 
    função deve mostrar um menu com as opções de formatação e realizar a 
    operação escolhida pelo usuário.

    3. O programa deve continuar rodando e mostrando o menu até que o usuário escolha sair.

Detalhes:

    O programa deve ser case-insensitive para contagem e pesquisa de palavras.
    Você pode assumir que o usuário entrará apenas com caracteres alfabéticos e espaços.

"""

#Solução

# Definindo a classe FormatadorDeFrase
class FormatadorDeFrase:
    
    # Método construtor, que é chamado quando um novo objeto da classe é instanciado
    def __init__(self, frase):
        
        # Inicializa a variável de instância 'frase' com o valor passado como argumento
        self.frase = frase
        
    # Método para converter todos os caracteres da frase para maiúsculas
    def para_maiusculas(self):
        
        # Usa o método upper() para converter a frase para maiúsculas e 
        # armazena na variável de instância 'frase'
        self.frase = self.frase.upper()
        
    # Método para converter todos os caracteres da frase para minúsculas
    def para_minusculas(self):
        
        # Usa o método lower() para converter a frase para minúsculas e 
        # armazena na variável de instância 'frase'
        self.frase = self.frase.lower()
        
    # Método para capitalizar a primeira letra da frase
    def capitalizar(self):
        
        # Usa o método capitalize() para capitalizar a primeira letra da 
        # frase e armazena na variável de instância 'frase'
        self.frase = self.frase.capitalize()
        
    # Método para converter a frase para o formato de título
    def formato_titulo(self):
        
        # Usa o método title() para capitalizar a primeira letra de cada
        # palavra na frase
        self.frase = self.frase.title()
        
    # Método para contar o número de vogais na frase
    def contar_vogais(self):
        
        # Define uma string contendo todas as vogais
        # vogais = 'aeiou'
        vogais = 'aeiouáéíóúàèìòùãõâêîôû'
        
        # Conta as vogais na frase (convertida para minúsculas) e retorna a soma
        # return sum(1 for letra in self.frase.lower() if letra in vogais)
        
        # Inicializa uma variável de contagem para armazenar o número de vogais
        contagem = 0

        # Converte a frase para minúsculas para simplificar a comparação
        frase_minuscula = self.frase.lower()

        # Percorre cada letra da frase
        for letra in frase_minuscula:
            
            # Verifica se a letra atual é uma vogal
            if letra in vogais:
                
                # Incrementa a variável de contagem
                contagem += 1

        # Retorna o total de vogais encontradas
        return contagem
    
    # Método para contar o número de consoantes na frase
    def contar_consoantes(self):
        
        # Define uma string contendo todas as consoantes
        consoantes = 'bcdfghjklmnpqrstvwxyzç'
        
        # Conta as consoantes na frase (convertida para minúsculas) e retorna a soma
        # return sum(1 for letra in self.frase.lower() if letra in consoantes)
        
        # Inicializa uma variável de contagem para armazenar o número de consoantes
        contagem = 0

        # Converte a frase para minúsculas para facilitar a comparação
        frase_minuscula = self.frase.lower()

        # Loop para percorrer cada letra da frase
        for letra in frase_minuscula:
            
            # Checa se a letra atual é uma consoante
            if letra in consoantes:
                
                # Incrementa a variável de contagem
                contagem += 1

        # Retorna o total de consoantes encontradas
        return contagem
                
    # Método para contar o número de ocorrências da letra 'a' na frase
    def contar_letra_a(self):
        
        # Usa o método count() para contar o número de ocorrências da 
        # letra 'a' na frase (convertida para minúsculas)
        return self.frase.lower().count('a')
    
    # Método para procurar e contar o número de ocorrências de uma palavra específica na frase
    def procurar_palavra(self, palavra):
        
        # Usa o método count() para contar o número de ocorrências da 
        # palavra na frase (ambas convertidas para minúsculas)
        return self.frase.lower().count(palavra.lower())
    
    # Método para obter a frase atual
    def obter_frase(self):
        
        # Retorna a variável de instância 'frase'
        return self.frase


# Definindo a função menu, que será a interface do usuário para o programa
def menu():
    
    # Imprime uma mensagem de boas-vindas
    print("\nBem-vindo ao Formatador de Frase!")
    
    # Solicita ao usuário que digite uma frase
    frase = input("Por favor, digite uma frase: ")
    
    # Cria um objeto 'formatador' da classe FormatadorDeFrase, 
    # passando a frase digitada como argumento
    formatador = FormatadorDeFrase(frase)
    
    # Enquanto verdadeiro, o menu ficará em execução
    while True:
        
        """
        para_maiusculas(): converte toda a frase para maiúsculas.
        para_minusculas(): converte toda a frase para minúsculas.
        capitalizar(): capitaliza a primeira letra da frase.
        formato_titulo(): converte a primeira letra de cada palavra da frase para maiúscula.
        contar_vogais(): conta e retorna o número de vogais na frase.
        contar_consoantes(): conta e retorna o número de consoantes na frase.
        contar_letra_a(): conta e retorna o número de ocorrências da letra 'a' na frase.
        procurar_palavra(palavra): conta e retorna o número de ocorrências de uma palavra específica na frase.
        obter_frase(): retorna a frase atual.
        """
        
        # Imprime as opções do menu
        print("\nEscolha uma opção para formatar a sua frase:")
        print("1. Converter para maiúsculas")
        print("2. Converter para minúsculas")
        print("3. Capitalizar a primeira letra da frase")
        print("4. Converter para o formato título.")
        print("5. Contar Vogais")
        print("6. Contar Consoantes")
        print("7. Contar letra 'a'")
        print("8. Pesquisar palavra")
        print("9. Mostrar frase atual")
        print("10. Sair")
        
        # Solicita ao usuário que escolha uma opção
        escolha = input("\nDigite o número da sua escolha: ")
        
        # Verifica qual opção foi escolhida e chama o método correspondente
        # do objeto 'formatador'
        if escolha == "1":
            
            # Chama o método para converter a frase para maiúsculas
            formatador.para_maiusculas()
            
        elif escolha == "2":
            
            # Chama o método para converter a frase para minúsculas
            formatador.para_minusculas()
            
        elif escolha == "3":
            
            # Chama o método para capitalizar a primeira letra da frase
            formatador.capitalizar()
            
        elif escolha == "4":
            
            # Chama o método para converter a frase para o formato de título
            formatador.formato_titulo()
            
        elif escolha == "5":
            
            # Chama o método para contar as vogais na frase e imprime o resultado
            print(f"Total de vogais: {formatador.contar_vogais()}")
            
        elif escolha == "6":
            
            # Chama o método para contar as consoantes na frase e imprime o resultado
            print(f"Total de consoantes: {formatador.contar_consoantes()}")
            
        elif escolha == "7":
            
            # Chama o método para contar ocorrências da letra 'a' na frase e imprime o resultado
            print(f"Total de ocorrências da letra 'a': {formatador.contar_letra_a()}")

        elif escolha == "8":
            
            # Solicita ao usuário a palavra que deseja pesquisar
            palavra = input("Digite a palavra que você quer pesquisar: ")
            
            # Chama o método para pesquisar a palavra e armazena o resultado
            contagem = formatador.procurar_palavra(palavra)
            
            # Exibe o resultado da pesquisa
            if contagem > 0:
                print(f"A palavra '{palavra}' aparece {contagem} vez(es) na frase.")
            else:
                print(f"A palavra '{palavra}' não foi encontrada na frase.")
                
        elif escolha == "9":
            
            # Mostra a frase atualizada
            print("\nFrase atual:", formatador.obter_frase())
            continue
            
        elif escolha == "10":
            
            # Encerra o programa
            print("Saindo do programa. Até mais!")
            
            break
            
        else:
            
            print("Escolha inválida. Tente novamente.")

        # Mostra a frase atualizada após aplicar qualquer formatação
        print("Frase atual: ", formatador.obter_frase())

# Verifica se o script está sendo executado como programa 
# principal e, nesse caso, chama a função menu
if __name__ == "__main__":
    menu()
