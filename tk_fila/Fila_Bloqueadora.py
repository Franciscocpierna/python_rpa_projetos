"""
Filas
        
            Variações e Tipos Especiais

                Fila Bloqueadora: Usada em programação concorrente, onde as 
                operações de enfileiramento e desenfileiramento podem ser bloqueadas.
                

Uma fila bloqueadora, ou "Blocking Queue", é uma fila utilizada em 
programação concorrente. Ela tem a habilidade de bloquear a thread de execução 
quando a fila está vazia (durante uma tentativa de retirada) ou quando a fila está 
cheia (durante uma tentativa de inserção).

A ideia básica é que, em ambientes multithreaded, uma thread possa esperar 
pacientemente até que haja espaço disponível ou até que haja algo na 
fila para ser processado.

Vamos criar um exemplo prático usando o módulo queue do Python, que fornece a 
classe Queue para criar filas bloqueadoras.

Exemplo: Produtor-Consumidor

Neste exemplo, teremos um produtor que coloca itens na fila e um consumidor que 
retira e processa esses itens.
"""

# Importando os módulos necessários:
# 'queue' para manipulação de filas, 
# 'threading' para execução de código em paralelo (threads)
# e 'time' para controlar pausas (delays) na execução.
import queue
import threading
import time

# Cria uma instância de fila chamada 'fila' com uma capacidade máxima de 5 itens.
# Isso significa que a fila pode armazenar no máximo 5 itens simultaneamente.
fila = queue.Queue(maxsize=5)



# Define a função 'produtor', que representa as ações do produtor neste problema 
# clássico do produtor-consumidor.
def produtor():
    
    # O produtor irá produzir 10 itens no total. O loop 'for' itera 10 vezes.
    for i in range(10):
        
        # Exibe uma mensagem indicando qual item está sendo produzido.
        # O valor de 'i' será o item, que vai de 0 a 9.
        print(f"Produzindo item {i}")
        
        # Adiciona o item (neste caso, o número de 0 a 9) à fila.
        # Se a fila estiver cheia, esta linha fará a thread esperar até que haja 
        # espaço disponível.
        fila.put(i)
        
        # Pausa a execução da thread por 0,5 segundos.
        # Isso simula um cenário onde leva um certo tempo para o produtor gerar um novo item.
        # Neste caso, estamos assumindo que leva meio segundo para produzir um item.
        time.sleep(0.5)
        
        
# Define a função 'consumidor', que representa as ações do consumidor neste problema 
# clássico do produtor-consumidor.
def consumidor():
    
    # O consumidor irá consumir 10 itens no total. O loop 'for' itera 10 vezes.
    for i in range(10):
        
        # Remove e obtém o próximo item da fila.
        # Se a fila estiver vazia, esta linha fará a thread esperar até que um item 
        # esteja disponível.
        item = fila.get()
        
        # Exibe uma mensagem indicando qual item está sendo consumido.
        print(f"Consumindo item {item}")
        
        # Pausa a execução da thread por 1 segundo.
        # Isso simula um cenário onde leva um certo tempo para o consumidor processar um item.
        # Neste caso, estamos assumindo que leva um segundo inteiro para consumir um item.
        time.sleep(1)
        
        
# Cria threads para o produtor e consumidor:
# 'threading.Thread' é usado para criar uma nova thread. 
# O parâmetro 'target' especifica a função que a thread executará.

# Cria uma thread para a função 'produtor'
thread_produtor = threading.Thread(target=produtor)

# Cria uma thread para a função 'consumidor'
thread_consumidor = threading.Thread(target=consumidor)


# Inicia as threads criadas anteriormente.
# Uma vez iniciadas, as threads começarão a executar as 
# funções 'produtor' e 'consumidor' em paralelo.
thread_produtor.start()
thread_consumidor.start()


# Os métodos 'join' são usados para esperar que as threads terminem.
# Isso garante que o programa principal não termine enquanto as 
# threads ainda estão executando.
thread_produtor.join()
thread_consumidor.join()


# Imprime "Fim!" uma vez que ambas as threads (produtor e consumidor) 
# tenham concluído sua execução.
print("Fim!")


"""
A função produtor() é definida para representar as ações do produtor no problema Produtor-Consumidor.

A função consumidor() é definida para representar as ações do consumidor no problema Produtor-Consumidor.

thread_produtor = threading.Thread(target=produtor): Cria uma thread para a função produtor.

thread_consumidor = threading.Thread(target=consumidor): Cria uma thread para a função consumidor.

thread_produtor.start(): Inicia a thread do produtor.

thread_consumidor.start(): Inicia a thread do consumidor.

thread_produtor.join(): Espera até que a thread do produtor termine sua execução.

thread_consumidor.join(): Espera até que a thread do consumidor termine sua execução.

print("Fim!"): Imprime "Fim!" uma vez que ambas as threads (produtor e consumidor) tenham concluído sua execução.

Em resumo, este código simula um cenário onde um produtor está colocando itens em 
uma fila e um consumidor está retirando e processando esses itens. As threads do produtor 
e do consumidor são iniciadas e executam suas respectivas funções de forma paralela. As 
filas bloqueadoras garantem que o produtor espere se a fila estiver cheia e que o consumidor 
espere se a fila estiver vazia.
"""
print()