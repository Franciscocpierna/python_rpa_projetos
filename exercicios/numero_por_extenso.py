"""
Conversor de Valores para Extenso

Escreva um programa que faça a seguinte tarefa:

    1. Solicite ao usuário a entrada de um valor inteiro 
    em reais, sem considerar os centavos e com um limite de até 1 trilhão.
    
    2. O programa deve converter esse valor numérico para sua representação 
    por extenso na língua portuguesa.
    
    3. Exibir o valor por extenso, seguido da palavra "reais".
    
    4. Por exemplo, se o usuário inserir 150, o programa deve 
    exibir Cento e cinquenta reais.
    
    5. O programa deve tratar possíveis erros na entrada, 
    informando ao usuário quando ele não inserir um número válido.
    
    6. Após a conversão, o programa deve perguntar ao usuário se 
    ele deseja converter outro valor. Se a resposta não for "sim", o 
    programa deve ser encerrado.

Restrições:

    - O programa deve aceitar números de 0 a 999.999.999.999 (um trilhão menos um).
    - Não considere valores negativos ou com centavos.
    - As entradas inválidas devem ser tratadas apropriadamente, solicitando ao usuário que insira novamente o valor.
"""

# Solução:

# Definindo a função que converte números de unidades (0-9) para sua representação por extenso
def unidades_para_extenso(n):
    
    # Lista contendo a representação por extenso dos números de 0 a 9, começando com uma string vazia para o índice 0
    unidades = ["", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove"]
    
    # Retorna a representação por extenso do número baseado no índice
    return unidades[n]

# Definindo a função que converte números de dezenas (10-99) para sua representação por extenso
def dezenas_para_extenso(n):
    
    # Lista contendo a representação por extenso das dezenas de 10 a 90
    dezenas = ["", "Dez", "Vinte", "Trinta", "Quarenta", "Cinquenta", "Sessenta", "Setenta", "Oitenta", "Noventa"]
    
    # Dicionário contendo a representação por extenso dos números de 11 a 19, que possuem uma escrita específica
    especiais = {11: "Onze", 12: "Doze", 13: "Treze", 14: "Quatorze", 15: "Quinze", 16: "Dezesseis", 17: "Dezessete", 18: "Dezoito", 19: "Dezenove"}

    # Verifica se o número está entre 11 e 19 (inclusive)
    if 10 < n < 20:
        
        return especiais[n]  # Retorna a representação por extenso do número especial
    
    else:
        
        
        """
        Operador módulo %:
            O operador módulo retorna o resto de uma divisão. Em outras 
            palavras, se você dividir um número a por um número b, ele retorna 
            o que sobra dessa divisão.

        Por exemplo:
            7 % 3 retorna 1 porque 7 dividido por 3 é igual a 2 com um resto de 1.
            9 % 2 retorna 1 porque 9 dividido por 2 é 4 com um resto de 1.

        Como isso ajuda a encontrar a unidade de um número?:
            Se você pegar qualquer número inteiro e calcular o módulo desse 
            número por 10 (n % 10), o resultado será o último dígito (unidade) desse número.

        Exemplos:
            Para n = 1234, n % 10 retorna 4.
            Para n = 567, n % 10 retorna 7.
            Para n = 89, n % 10 retorna 9.
            
        Resumindo, o trecho de código:
        
        unidade = n % 10

        Está simplesmente atribuindo o último dígito (unidade) do número n à variável unidade.
        """
        # Extraí a unidade (último dígito) do número
        unidade = n % 10
        
        # Extraí a dezena (primeiro dígito) do número
        dezena = n // 10

        # Se o número é uma dezena exata (como 20, 30, ... 90)
        if unidade == 0:
            
            return dezenas[dezena]
        
        else:
            
            # Combina a representação da dezena e da unidade com o conectivo "e"
            return dezenas[dezena] + " e " + unidades_para_extenso(unidade)

        
def centenas_para_extenso(n):
    
    # Caso especial para o número 100, que tem uma forma extensa única.
    if n == 100:
        return "cem"
    
    # Lista das representações extensas para as centenas.
    centenas = ["", "Cento", "Duzentos", "Trezentos", "Quatrocentos", "Quinhentos", 
                "Seiscentos", "Setecentos", "Oitocentos", "Novecentos"]

    # Divide o número por 100 para obter a parte das centenas.
    centena = n // 100
    
    # Obtém o restante da divisão por 100 para determinar a parte das dezenas e unidades.
    resto = n % 100

    # Se não houver dezenas ou unidades (resto é 0), retorna somente a parte das centenas.
    if resto == 0:
        
        return centenas[centena]
    
    # Se o resto for menor que 10, significa que há somente unidades.
    elif resto < 10:
        
        # Retorna a parte das centenas concatenada com " e " e a parte das unidades.
        return centenas[centena] + " e " + unidades_para_extenso(resto)
    
    # Se o resto for 10 ou mais, significa que há dezenas (e possivelmente unidades).
    else:
        
        # Retorna a parte das centenas concatenada com " e " e a parte das dezenas (e unidades, se houver).
        return centenas[centena] + " e " + dezenas_para_extenso(resto)
    
    
# Definindo a função que converte números de centavos (0-99) para sua representação por extenso
def centavos_para_extenso(n):
    
    # Se n for igual a 1, o número é tratado de forma especial, já que "centavo" fica no singular
    if n == 1:
        
        return "Um Centavo"
    
    # Se n estiver entre 2 e 9, usamos a função que converte unidades para por extenso
    elif n < 10:
        
        return unidades_para_extenso(n) + " Centavos"
    
    # Para números maiores ou iguais a 10 (ou seja, dezenas de centavos), usamos a função que converte dezenas para por extenso
    else:
        
        return dezenas_para_extenso(n) + " Centavos"
    

def converter_para_extenso(n):
    
    # Se o número for menor que 10, converta diretamente a unidade para a forma extensa.
    if n < 10:
        
        return unidades_para_extenso(n)
    
    # Se o número estiver entre 10 e 99, converta a dezena para a forma extensa.
    elif n < 100:
        
        return dezenas_para_extenso(n)
    
    # Se o número estiver entre 100 e 999, converta a centena para a forma extensa.
    elif n < 1000:
        
        return centenas_para_extenso(n)
    
    # Se o número estiver entre 1.000 e 999.999, converta os milhares para a forma extensa.
    elif n < 10**6:  # Menor que um milhão
        
        milhares = n // 1000  # Quantidade de milhares
        resto = n % 1000  # O restante depois de remover os milhares

        """
        if milhares == 1: - Verifica se a parte dos "milhares" do número é igual a 1. 
        Se sim, estamos tratando do número "mil".
        
        return "mil" + (" e " + converter_para_extenso(resto) if resto > 0 else "") -
        Retorna a string "mil". Se a variável resto for maior que 0, ela adiciona a 
        string " e " seguida da forma por extenso de resto.
        """
        # Caso especial para "mil", que não possui plural.
        if milhares == 1:
            
            return "mil" + (" e " + converter_para_extenso(resto) if resto > 0 else "")
        
        else:
            
            """
                else: - Este é o caso quando milhares não é igual a 1.
                return converter_para_extenso(milhares) + 
                " mil" + (" e " + converter_para_extenso(resto) if resto > 0 else "") - Aqui, a 
                função converter_para_extenso(milhares) é chamada para converter a parte dos 
                milhares para sua forma por extenso. Depois, a palavra " mil" é adicionada. Se a 
                variável resto for maior que 0, " e " seguido pela forma por extenso de resto é 
                também adicionado.
                
                
                Por que a função chama ela mesmo?
                A técnica é conhecida como "recursão", onde uma função chama a si mesma 
                para resolver um problema menor.

                Suponhamos que estamos convertendo o número 12.345 para a sua 
                forma por extenso. A função converter_para_extenso poderia inicialmente 
                dividir esse número em duas partes: os "milhares" (12) e o "resto" (345).

                    - Para a parte dos "milhares" (12), a função chamaria a si mesma com 
                    converter_para_extenso(12), que retornaria "doze".
                    
                    - Para o "resto" (345), a função também chamaria a si mesma com 
                    converter_para_extenso(345), que retornaria "trezentos e quarenta e cinco".

                Agora, combinando essas duas partes, teríamos "doze mil e trezentos e quarenta e cinco".

                A recursão é muito útil quando você tem um problema que pode ser dividido 
                em problemas menores que são essencialmente do mesmo tipo que o problema 
                maior. No caso da conversão de números para a sua forma por extenso, o problema 
                de converter 12.345 é similar ao problema de converter 12 ou 345. Ambos podem 
                ser tratados pela mesma função converter_para_extenso, e é por isso que 
                ela chama a si mesma.

                Naturalmente, para que a recursão não seja infinita, deve haver uma ou mais 
                "condições de base" onde a função não faz uma chamada recursiva e simplesmente 
                retorna um resultado. No código, a "condição de base" está em outra parte do código, onde 
                números menores que 1000 (ou outra constante apropriada) são convertidos diretamente para a sua forma 
                por extenso, sem mais chamadas recursivas.

                Resumindo, o código lida com a forma por extenso de números na casa dos milhares em 
                português, prestando atenção ao caso especial do número "mil".
            """
            
            # Converter a parte dos milhares e adicionar a parte restante (centenas, dezenas e unidades).
            return converter_para_extenso(milhares) + " mil" + (" e " + converter_para_extenso(resto) if resto > 0 else "")    
       
    
    # Se o número estiver entre 1.000.000 e 999.999.999, converta os milhões para a forma extensa.
    elif n < 10**9:  # Menor que um bilhão
        
        milhoes = n // 10**6  # Quantidade de milhões
        resto = n % 10**6  # O restante depois de remover os milhões

        # Caso especial para "um milhão".
        if milhoes == 1:
            
            return "um milhão" + (" e " + converter_para_extenso(resto) if resto > 0 else "")
        
        else:
            
            # Converter a parte dos milhões e adicionar a parte restante.
            return converter_para_extenso(milhoes) + " milhões" + (" e " + converter_para_extenso(resto) if resto > 0 else "") 
        
    # Se o número estiver entre 1.000.000.000 e 999.999.999.999, converta os bilhões para a forma extensa.
    elif n < 10**12:  # Menor que um trilhão
        
        bilhoes = n // 10**9  # Quantidade de bilhões
        resto = n % 10**9  # O restante depois de remover os bilhões

        # Caso especial para "um bilhão".
        if bilhoes == 1:
            
            return "um bilhão" + (" e " + converter_para_extenso(resto) if resto > 0 else "")
        
        else:
            
            # Converter a parte dos bilhões e adicionar a parte restante.
            return converter_para_extenso(bilhoes) + " bilhões" + (" e " + converter_para_extenso(resto) if resto > 0 else "")

    
while True:
    
    try:
        
        """
        1. Solicite ao usuário a entrada de um valor inteiro 
            em reais com um limite de até 1 trilhão.
        """
        
        # Solicita ao usuário um valor em reais, considerando a separação de centavos por ponto
        valor = input("Digite um valor em reais (use ponto para separar os centavos e menor que 1 trilhão): ")
        
        # Separa a parte dos reais e dos centavos
        # reais, _, centavos = valor.partition('.')
        
        # Usando partition para dividir o valor com base no ponto.
        resultado = valor.partition('.')

        #exeplo valor = "123.45"
        # resultado[0] contém a parte da string antes do ponto - "123"
        # resultado[1] contém o ponto - "."
        # resultado[2] contém a parte da string após o ponto - "45"

        reais = resultado[0]
        _ = resultado[1]  # Usamos um underscore quando não queremos usar o valor em cálculos futuros.
        centavos = resultado[2]

        
        # Converte a parte dos reais e dos centavos para inteiros, considerando zero se vazio
        # Verifica se a variável 'reais' contém algum valor
        if reais:
            
            # Se 'reais' contiver algum valor, converte-o para inteiro
            numero_reais = int(reais)
            
        else:
            
            # Caso 'reais' esteja vazio ou None, define 'numero_reais' como 0
            numero_reais = 0

        # Verifica se a variável 'centavos' contém algum valor
        if centavos:
            
            # Se 'centavos' contiver algum valor, converte-o para inteiro
            numero_centavos = int(centavos)
            
        else:
            
            # Caso 'centavos' esteja vazio ou None, define 'numero_centavos' como 0
            numero_centavos = 0
            
        
        """
        1. if 0 <= numero_reais < 1012**:
                - Esta é uma forma concisa de verificar se numero_reais está no intervalo 
                de 0 (inclusive) a 10**12 (exclusivo). Em outras palavras, está verificando 
                se numero_reais tem no máximo 12 dígitos e é um número não negativo.

        2. and 0 <= numero_centavos < 100:
                - Esta condição verifica se numero_centavos está no intervalo de 
                0 (inclusive) a 100 (exclusivo). Ou seja, está garantindo que numero_centavos 
                é um número de dois dígitos (0-99) e também não negativo.

        - Ambas as condições precisam ser verdadeiras devido ao uso do operador and.

        Então, para que a condição geral seja verdadeira (True), numero_reais deve ser um 
        número entre 0 e 10**12 (ou seja, até 11 dígitos), e numero_centavos deve 
        ser um número entre 0 e 99. Se alguma dessas condições não for atendida, a expressão 
        retornará False.
        """
        if 0 <= numero_reais < 10**12 and 0 <= numero_centavos < 100:
            
            # Verifica se o número de reais é maior que zero.
            if numero_reais > 0:
                
                """
                2. O programa deve converter esse valor numérico para sua representação 
                    por extenso na língua portuguesa.
                """
                # Converte o número de reais para sua representação extensa.
                extenso_reais = converter_para_extenso(numero_reais)

                # Se o número de reais for maior que um, adiciona "reais" ao final.
                if numero_reais > 1:
                    
                    extenso_reais += " Reais"
                    
                # Caso contrário, ou seja, se for exatamente um real, adiciona "real" ao final.
                else:
                    
                    extenso_reais += " Real"
                    
            # Se o número de reais for zero, a representação extensa é uma string vazia.
            else:
                extenso_reais = ""  
                
                
            # Inicia a variável extenso_centavos como uma string vazia.
            extenso_centavos = ""

            # Se o número de centavos for maior que zero,
            if numero_centavos > 0:
                
                # Converte o número de centavos para sua representação extensa.
                extenso_centavos = centavos_para_extenso(numero_centavos)
                
            
            # Combina as partes dos reais e dos centavos, considerando o "e" entre eles, se necessário
            if extenso_reais and extenso_centavos:
                
                extenso = extenso_reais + " e " + extenso_centavos
                
            else:
                
                extenso = extenso_reais + extenso_centavos
                
                
            print(extenso)
            
        else:
            
            # Exibe uma mensagem de erro se o valor estiver fora dos limites estabelecidos
            print("Por favor, insira um número válido e menor que 1 trilhão.")
        
        
    except ValueError:
        
        print("Por favor, digite um número válido.")

    # Pergunta ao usuário se ele deseja continuar convertendo outros valores
    continuar = input("Deseja converter outro valor? (sim/não) ").strip().lower()
    
    if continuar != 'sim':
        
        # Encerra o programa se o usuário decidir não continuar
        print("Obrigado por usar o programa!")
        break
        