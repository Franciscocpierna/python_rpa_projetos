"""
3. Pilares da POO

    - Encapsulamento: Protegendo os dados de uma classe.
        Uso de modificadores de acesso (public, private, protected).
        
        
"""

"""
A Programação Orientada a Objetos utiliza vários princípios, sendo um deles
o encapsulamento. O encapsulamento permite que os detalhes de implementação de 
uma classe sejam ocultados, expondo apenas uma interface bem definida. Isso 
é conseguido usando modificadores de acesso: public, private e protected.

    Public: Em Python, todos os membros de uma classe são públicos por 
        padrão. Qualquer membro pode ser acessado de fora da classe.

    Protected: Um membro é considerado protegido se seu nome começa com 
        um sublinhado único (_). Isso é mais uma convenção e um aviso para o 
        programador de que o membro não deve ser acessado diretamente, embora 
        ainda seja possível fazê-lo.

    Private: Um membro é considerado privado se seu nome começa com dois 
        sublinhados (__). Novamente, isso é mais uma convenção do que uma regra 
        rigorosa. O Python realiza um nome mangling dos atributos, alterando o nome 
        do atributo de forma que ele seja mais difícil de ser acessado acidentalmente, 
        mas ainda é possível.
"""

#Exemplo em Python

#Aqui está um exemplo de como usar esses modificadores 
#de acesso em Python:

# Definindo a classe Pessoa
# Define uma classe chamada 'Pessoa'.
class Pessoa:
    
    # Define o método construtor '__init__' para inicializar os atributos da classe.
    def __init__(self, nome, idade):
        
        # Inicializa o atributo 'nome' da instância com o valor fornecido como argumento.
        # Este é um atributo público, significando que pode ser acessado diretamente de fora da classe.
        self.nome = nome  
        
        # Inicializa o atributo '_idade' da instância com o valor fornecido.
        # Este é um atributo protegido, indicado pelo prefixo de sublinhado simples.
        # Ele pode ser acessado dentro da classe e suas subclasses, mas o acesso direto de fora da classe não é recomendado.
        self._idade = idade  
        
        # Inicializa o atributo '__saldo' da instância com o valor 0.
        # Este é um atributo privado, indicado pelo prefixo de dois sublinhados.
        # Ele só deve ser acessado dentro da classe.
        self.__saldo = 0  

    # Define um método público chamado 'mostrar_nome'.
    def mostrar_nome(self):
        
        # Retorna o valor do atributo 'nome'.
        return self.nome  

    # Define um método público chamado 'mostrar_idade'.
    def mostrar_idade(self):
        
        # Retorna o valor do atributo '_idade'.
        return self._idade  
    
    
    # Define um método protegido chamado '_aumentar_idade'.
    def _aumentar_idade(self):
        
        # Incrementa o valor do atributo '_idade' em 1.
        self._idade += 1 
        
        
    # Define um método privado chamado '__aumentar_saldo'.
    def __aumentar_saldo(self, quantidade):
        
        # Incrementa o valor do atributo '__saldo' pela quantidade fornecida.
        self.__saldo += quantidade
        
        
    # Define um método público chamado 'depositar'.
    def depositar(self, quantidade):
        
        # Chama o método privado '__aumentar_saldo' para modificar o atributo '__saldo'.
        self.__aumentar_saldo(quantidade)  
        
        # Retorna o valor atualizado do atributo '__saldo'.
        return self.__saldo
    
    
# Criando uma instância da classe Pessoa e inicializando-a com o nome "Alice" e a idade 30.
# A variável 'p' agora aponta para esta instância.
p = Pessoa("Alice", 30)


# ---- Atributos ----

# Acessando o atributo público 'nome' diretamente.
# Isso é totalmente aceitável porque o atributo é público.
print(p.nome)  # Saída: Alice

# Acessando o atributo protegido '_idade' diretamente.
# Embora isso seja possível, não é recomendado porque o atributo é marcado como protegido.
print(p._idade)  # Saída: 30

# Tentando acessar o atributo privado '__saldo' diretamente.
# Isso não é recomendado e requer uma técnica chamada "name mangling" para ser acessado.
# É melhor usar um método público para acessar atributos privados.
print(p._Pessoa__saldo)  # Saída: 0

# ---- Métodos Públicos -----

print("\nMétodos Públicos\n")

# Utilizando o método público para mostrar o nome novamente.
# Isso é útil se você precisar acessar o nome várias vezes no seu código.
print(p.mostrar_nome())  # Saída: Alice
print(p.mostrar_nome())  # Saída: Alice

# Utilizando o método público para mostrar a idade novamente.
# Isso é útil se você precisar verificar a idade em diferentes partes do código.
print(p.mostrar_idade())  # Saída: 30

# Fazendo um segundo depósito na conta usando um método público.
# Isso é útil para aumentar o saldo em etapas.
print(p.depositar(50)) # Saída: 50
print(p.depositar(50)) # Saída: 100
print(p.depositar(50)) # Saída: 150

# ---- Métodos Protegidos -----

print("\nMétodos Protegidos\n")

# Para usar um método protegido, você normalmente não deveria fazê-lo fora da classe ou subclasses.
# No entanto, para fins de demonstração, mostraremos como isso seria feito.

# Utilizando o método protegido para aumentar a idade.
# Embora isso seja possível, não é a prática recomendada.
p._aumentar_idade()  # Aumenta a idade em 1
p._aumentar_idade()  # Aumenta a idade em 1
print(p.mostrar_idade())  # Saída: 32 (idade aumentada em 2)


# ---- Métodos Privados -----

print("\nMétodos Privados\n")

# Você realmente não deveria acessar métodos privados fora da classe.
# Mas para fins educacionais, mostrarei como isso é tecnicamente possível usando name mangling.

# Utilizando name mangling para acessar um método privado (NÃO RECOMENDADO!)
p._Pessoa__aumentar_saldo(50)  # Aumenta o saldo em 50
print(p.depositar(0))  # Saída: 200 (saldo anterior era 150, aumentou para 200)

"""
O termo "name mangling" (ou "alteração de nome", em tradução livre) é uma 
técnica usada em algumas linguagens de programação, incluindo Python, para alterar 
o nome de um identificador (como uma variável ou método) de modo a torná-lo menos 
acessível ou discernível fora do escopo onde foi definido.

Em Python, os atributos e métodos privados são precedidos por dois sublinhados (__). 
O interpretador Python altera o nome desses membros para incluir o nome da 
classe que os contém. Isso torna mais difícil para o código externo acessar 
esses membros acidentalmente.
"""

# ---- O que não fazer ----

# A seguir estão alguns exemplos de práticas que não são recomendadas:

# Alterar diretamente um atributo protegido de fora da classe.
# Isso quebra o encapsulamento e pode levar a erros.
p._idade = 40  # Não recomendado

# Tentar acessar diretamente um método privado de fora da classe.
# Isso não funcionará a menos que você use name mangling, e ainda assim não é recomendado.
# p.__aumentar_saldo(100)  # Isso dará um erro

"""
Neste exemplo, nome é público, _idade é protegido e __saldo é privado. 
Temos métodos públicos para interagir com esses atributos, bem como métodos 
protegidos e privados (_aumentar_idade e __aumentar_saldo, respectivamente).

Note que mesmo o atributo privado __saldo pode ser acessado fora da classe 
usando "name mangling", como em p._Pessoa__saldo. No entanto, essa não é uma 
prática recomendada.
"""
print()
"""
3. Pilares da POO

    Encapsulamento: Protegendo os dados de uma classe.
        
        Métodos getters e setters.
        
Em programação orientada a objetos, os métodos "getters" e "setters" 
são usados para controlar o acesso a atributos de uma classe. 

Os "getters" são usados para acessar o valor de um atributo, enquanto 
os "setters" são usados para modificar esse valor. 

Essa abordagem é especialmente útil para adicionar uma camada extra de validação 
ou lógica durante o acesso ou modificação de atributos.

Vamos considerar uma classe Produto que tem um preço. Queremos garantir 
que o preço nunca seja negativo e que possamos aplicar um desconto ao 
produto se necessário. Usaremos métodos "getters" e "setters" para controlar esses aspectos.

"""

# Definição da classe Produto
class Produto:
    
    # Método construtor para inicializar atributos da classe
    def __init__(self, nome, preco):
        
        # Atributo público 'nome' para armazenar o nome do produto
        # Público significa que esse atributo pode ser acessado diretamente de fora da classe
        self.nome = nome
        
        # Atributo protegido '_preco' para armazenar o preço do produto
        # Protegido significa que esse atributo deve ser acessado apenas dentro desta classe e suas subclasses
        # Inicializamos com None para indicar que ele ainda não tem um valor definido
        self._preco = None
        
        # Usamos o método setter set_preco() para inicializar o preço do produto
        # Isso garante que todas as regras de validação sejam aplicadas desde o início
        self.set_preco(preco)
        
    # Método getter para obter o preço atual do produto
    # Este método é usado para ler o valor do atributo protegido '_preco'
    def get_preco(self):
        
        return self._preco
    
    
    # Método setter para definir um novo preço para o produto
    # Este método é usado para modificar o valor do atributo protegido '_preco'
    def set_preco(self, valor):
        
        # Verificamos se o valor fornecido é um número não-negativo
        # Essa é uma regra de negócio que queremos impor
        if valor >= 0:
            self._preco = valor  # Se a verificação passar, atualizamos o valor de '_preco'
        else:
            print("Preço deve ser não-negativo")  # Se a verificação falhar, exibimos uma mensagem de erro
            
    # Método para aplicar um desconto percentual ao preço do produto
    # Este método modifica o atributo '_preco', aplicando um desconto a ele
    def aplicar_desconto(self, desconto_percentual):
        
        # Calculamos o novo preço após aplicar o desconto
        # O cálculo é feito tomando o preço original e subtraindo a porcentagem de desconto
        novo_preco = self._preco * (1 - desconto_percentual / 100)
        
        # Usamos o método setter set_preco() para atualizar o preço do produto com o novo valor
        # Isso garante que todas as regras de validação sejam novamente aplicadas
        self.set_preco(novo_preco)

        
# Criando um objeto Produto
p1 = Produto("Camiseta", 50)

# Obtendo o preço usando o método getter
print(f"Preço atual de {p1.nome}: R$ {p1.get_preco()}")  # Saída: Preço atual de Camiseta: R$ 50

# Definindo um novo preço usando o método setter
p1.set_preco(60)

print(f"Novo preço de {p1.nome}: R$ {p1.get_preco()}")  # Saída: Preço atual de Camiseta: R$ 60


# Tentando definir um preço negativo
p1.set_preco(-10)  # Saída: Preço deve ser não-negativo

# Aplicando um desconto de 10% ao produto
p1.aplicar_desconto(10)

print(f"Preço de {p1.nome} após desconto R$ {p1.get_preco()}")  # Saída: Preço de Camiseta após desconto: R$ 54.0

"""
Exercício Pet

Instruções do Exercício

    1. Crie uma classe chamada Pet.
    2. A classe deve ter os seguintes atributos privados: _nome, _idade e _peso.
        - Utilize métodos "getters" para cada um desses atributos.
        - Utilize métodos "setters" para cada um desses atributos. 
        
        Os "setters" devem conter as seguintes validações:
            - O nome deve ser uma string e não pode ser vazio.
            - A idade deve ser um número inteiro e deve ser maior ou igual a 0.
            - O peso deve ser um número flutuante e deve ser maior que 0.
    
    3. Adicione um método exibir_info() que mostre as informações do pet.
    
    
# Teste sua implementação
meu_pet = Pet()
meu_pet.set_nome("Buddy")
meu_pet.set_idade(5)
meu_pet.set_peso(9.5)
meu_pet.exibir_info()

Sua tarefa é completar a classe Pet seguindo as instruções. 
Certifique-se de utilizar "getters" e "setters" para controlar o acesso aos 
atributos da classe.
"""

#Solução

# 1. Crie uma classe chamada Pet.
# Definindo a classe Pet
class Pet:
    
    """
    2. A classe deve ter os seguintes atributos privados: _nome, _idade e _peso.
        - Utilize métodos "getters" para cada um desses atributos.
        - Utilize métodos "setters" para cada um desses atributos. 
    """
    # Método construtor para inicializar os atributos quando um objeto da classe é criado
    def __init__(self):
        
        # Inicializa o atributo '_nome' como uma string vazia. 
        # O prefixo "_" indica que é um atributo protegido.
        self._nome = ""
        
        # Inicializa o atributo '_idade' como 0. 
        # O prefixo "_" indica que é um atributo protegido.
        self._idade = 0
        
        # Inicializa o atributo '_peso' como 0.0. 
        # O prefixo "_" indica que é um atributo protegido.
        self._peso = 0.0
        
    # Método "getter" para o nome, permite obter o valor do atributo '_nome'
    def get_nome(self):
        
        return self._nome
    
    """
    Os "setters" devem conter as seguintes validações:
            - O nome deve ser uma string e não pode ser vazio.
            - A idade deve ser um número inteiro e deve ser maior ou igual a 0.
            - O peso deve ser um número flutuante e deve ser maior que 0.
    """

    # Método "setter" para o nome, permite definir um novo valor para o atributo '_nome'
    def set_nome(self, novo_nome):
        
        """
        Os "setters" devem conter as seguintes validações:
            - O nome deve ser uma string e não pode ser vazio.
        """
        # Verifica se o novo_nome é uma string e se não está vazio
        if isinstance(novo_nome, str) and novo_nome != "":
            
            # Atualiza o valor do atributo '_nome'
            self._nome = novo_nome
            
        else:
            
            # Imprime uma mensagem de erro se o nome fornecido não for válido
            print("Nome inválido.")
            
    # Método "getter" para a idade, permite obter o valor do atributo '_idade'
    def get_idade(self):
        
        return self._idade
    
    
    # Método "setter" para a idade, permite definir um novo valor para o atributo '_idade'
    def set_idade(self, nova_idade):
        
        """
            Os "setters" devem conter as seguintes validações:
            - A idade deve ser um número inteiro e deve ser maior ou igual a 0.
        """
        # Verifica se a nova_idade é um inteiro e se é maior ou igual a 0
        if isinstance(nova_idade, int) and nova_idade >= 0:
            
            # Atualiza o valor do atributo '_idade'
            self._idade = nova_idade
            
        else:
            
            # Imprime uma mensagem de erro se a idade fornecida não for válida
            print("Idade inválida.")
            
    # ---------------------------------------------
    
    # Método "getter" para o peso, permite obter o valor do atributo '_peso'
    def get_peso(self):
        
        return self._peso

    # Método "setter" para o peso, permite definir um novo valor para o atributo '_peso'
    def set_peso(self, novo_peso):
        
        """
        Os "setters" devem conter as seguintes validações:
                - O peso deve ser um número flutuante e deve ser maior que 0.
        """
        
        # Verifica se o novo_peso é um número flutuante e se é maior que 0
        if isinstance(novo_peso, float) and novo_peso > 0:
            
            # Atualiza o valor do atributo '_peso'
            self._peso = novo_peso
            
        else:
            
            # Imprime uma mensagem de erro se o peso fornecido não for válido
            print("Peso inválido.")
            
            
      
    # 3. Adicione um método exibir_info() que mostre as informações do pet.
    def exibir_info(self):
        
        print(f"Nome: {self._nome}")
        print(f"Idade: {self._idade}")
        print(f"Peso: {self._peso} kg")
        
    
# Teste sua implementação
meu_pet = Pet()
meu_pet.set_nome("Bob")
meu_pet.set_idade(5)
meu_pet.set_peso(9.5)
meu_pet.exibir_info()

print("\n-----------------\n")

meu_pet.set_nome("Toto")
meu_pet.set_idade(8)
meu_pet.set_peso(7.5)
meu_pet.exibir_info()

print("\n-----------------\n")

meu_pet.set_nome("Lua")
meu_pet.set_idade(12)
meu_pet.set_peso(9.3)
meu_pet.exibir_info()       
