#Definindo uma lista de perguntas e respostas
perguntas = [
    {
        "pergunta": "Qual é a capital da França?",  # Pergunta sobre a capital da França
        "opcoes": ["a) Paris", "b) Londres", "c) Roma", "d) Berlim"],  # Opções de resposta
        "resposta": "a"  # Resposta correta
    },
    {
        "pergunta": "Qual é o maior planeta do sistema solar?",  # Pergunta sobre o maior planeta do sistema solar
        "opcoes": ["a) Marte", "b) Saturno", "c) Júpiter", "d) Vênus"],  # Opções de resposta
        "resposta": "c"  # Resposta correta
    },
    {
        "pergunta": "Quem pintou a Mona Lisa?",  # Pergunta sobre o pintor da Mona Lisa
        "opcoes": ["a) Vincent van Gogh", "b) Pablo Picasso", "c) Leonardo da Vinci", "d) Salvador Dalí"],  # Opções de resposta
        "resposta": "c"  # Resposta correta
    },
    {
        "pergunta": "Qual é o rio mais longo do mundo?",  # Pergunta sobre o rio mais longo do mundo
        "opcoes": ["a) Amazonas", "b) Nilo", "c) Yangtzé", "d) Mississipi"],  # Opções de resposta
        "resposta": "b"  # Resposta correta
    },
    {
        "pergunta": "Quem escreveu o livro 'Dom Quixote'?",  # Pergunta sobre o autor do livro "Dom Quixote"
        "opcoes": ["a) Miguel de Cervantes", "b) William Shakespeare", "c) Johann Wolfgang von Goethe", "d) Dante Alighieri"],  # Opções de resposta
        "resposta": "a"  # Resposta correta
    }
]

# Variável para armazenar a pontuação do jogador
pontuacao = 0

# Loop através de cada pergunta
for i in range(len(perguntas)):
    
    # Obtendo a pergunta atual
    pergunta_atual = perguntas[i]
    
    # Imprimindo o número e a pergunta atual
    print("Pergunta", i + 1, ":")
    print(pergunta_atual["pergunta"])
    
    # Imprimindo as opções de resposta
    for opcao in pergunta_atual["opcoes"]:
        
        print(opcao)
        
    # Obtendo a resposta do jogador
    resposta = input("Digite a letra correspondente à sua resposta:")
        
    # Verificando se a resposta está correta
    if resposta == pergunta_atual["resposta"]:
            
        print("Resposta correta!")
            
        #pontuacao = pontuacao + 1
        pontuacao += 1
            
    else:
            
        print("Resposta incorreta!")
            
    print() # Linha em branco para separar as perguntas

# Fim do jogo
print("Fim de Jogo!")
print("Sua pontuação final é:", pontuacao, "pontos.")