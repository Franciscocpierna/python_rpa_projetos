def exibir_mensagem():
    
    print("Bem vindo à Urna Eletrônica!")
    
def exibir_opcoes_candidatos():
    
    print("Escolha o número do seu candidato:")
    print("1. Candidato A")
    print("2. Candidato B")
    print("3. Candidato C")
    
def receber_voto():
    
    voto = input("Digite o número do candidato: ")
    return voto

def contabilizar_votos(votos):
    
    #Cria um dicionário vazio para armazenar a contagem dos votos
    contagem = {}
    
    #Para cada voto na lista
    for voto in votos:
        
        #Se o voto já estiver na contagem
        if voto in contagem:
            
            #Incremento o contador para aquele voto
            contagem[voto] += 1
            
        else:
        
            #Inicializo o contador para aquele voto como 1
            contagem[voto] = 1
            
    #Retorna o dicionário com a contagem dos votos
    return contagem

def exibir_resultado(contagem):
    
    print("\nResultado da votação:")
    
    for candidato, votos in contagem.items():
        
        print("Candidato {}: {} voto(s)".format(candidato, votos))
    
#Função principal
def main():
    
    exibir_mensagem()
    exibir_opcoes_candidatos()
    votos = []
    
    while True:
        
        voto = receber_voto()
        
        #isdigit() é um método em Python que retorna True se todos os caracteres 
        #de uma string são dígitos (0 a 9), caso contrário, retorna False.
        
        # está sendo usado para verificar se o valor digitado pelo eleitor é um número 
        #válido. Ele é aplicado em cada voto recebido para garantir que seja uma entrada 
        #numérica válida antes de adicioná-lo à lista de votos. 
        if voto.isdigit():
            
            #append - adiciona o item na lista
            votos.append(voto)
            
        else:
            
            print("Votação encerrada!")
            
            #Encerra o programa
            break
            
        contagem = contabilizar_votos(votos)
        exibir_resultado(contagem)

#Chama a função para executar o programa
main()