'''
ALTERAÇÃO DE ESTRUTURA DE TABELA SQLITE

1. A Estratégia de "Adição com Valor Padrão"
Se você quer adicionar um campo (por exemplo, categoria ou status) sem quebrar os registros antigos, 
você deve definir um valor padrão (DEFAULT).

Comando SQL:
ALTER TABLE produtos ADD COLUMN categoria TEXT NOT NULL DEFAULT 'Geral';

2. A Estratégia Avançada (Para Mudanças Complexas)
Se a nova estrutura for mais complexa do que apenas um valor padrão (por exemplo, se você precisar calcular o novo valor com base em outros campos existentes), o ALTER TABLE simples não serve. Nesse caso, você deve usar o padrão de migração:

Criar uma tabela temporária com a nova estrutura.

Copiar os dados da tabela original para a nova, tratando a lógica dos campos.

Remover a tabela original.

Renomear a tabela temporária para o nome original.

Exemplo prático (SQL):


-- 1. Cria a nova tabela com a estrutura correta
CREATE TABLE produtos_novo (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    preco REAL,
    nova_coluna TEXT NOT NULL -- O novo campo
);

-- 2. Migra os dados com uma lógica de conversão (CASE, por exemplo)


INSERT INTO produtos_novo (id, nome, preco, nova_coluna)
SELECT id, nome, preco, 
       CASE WHEN preco > 100 THEN 'Premium' ELSE 'Comum' END
FROM produtos;

-- 3. Remove a antiga
DROP TABLE produtos;

-- 4. Renomeia a nova
ALTER TABLE produtos_novo RENAME TO produtos;





INSERT INTO produtos_novo (id, nome, preco, nova_coluna)
SELECT id, nome, preco, 'ESTOQUE_INICIAL' -- Este texto é o valor que populará a nova coluna
FROM produtos;



Quando você adiciona um campo de data em uma tabela já populada, o maior risco é o campo ficar com valor NULL 
(vazio) ou com uma data incorreta, o que pode quebrar funções de cálculo ou filtros 
(como o strftime que você usou anteriormente).

Para o seu estoque.db, a melhor estratégia depende de qual informação você deseja colocar nesse novo campo.

Estratégia: Adicionar com Valor Padrão (Recomendado)
Se você quer que todos os registros antigos recebam a data de hoje (data da criação da coluna), 
você pode usar o DEFAULT CURRENT_DATE.

ALTER TABLE produtos ADD COLUMN data_inclusao DATE NOT NULL DEFAULT (DATE('now'));

ou faça assim

-- 1. Cria nova tabela com a coluna 'data_inclusao'
CREATE TABLE produtos_novo (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    preco REAL,
    data_inclusao DATE NOT NULL
);

-- 2. Migra os dados calculando a data (Exemplo: 2026-07-17 menos 1 dia por ID)


INSERT INTO produtos_novo (id, nome, preco, data_inclusao)
SELECT id, nome, preco, DATE('now', '-' || id || ' days')
FROM produtos;

-- 3. Troca as tabelas
DROP TABLE produtos;
ALTER TABLE produtos_novo RENAME TO produtos;
'''



''' 
relatórios com paginação

# --- Lote 1: Pega os primeiros 10 registros (do 0 ao 9) ---
cursor.execute("SELECT * FROM produtos LIMIT 10 OFFSET 0")
lote_1 = cursor.fetchall()
# Exibe ou processa o lote 1...

# --- Lote 2: Pega os próximos 10 registros (do 10 em diante, pulando os 10 primeiros) ---
cursor.execute("SELECT * FROM produtos LIMIT 10 OFFSET 10")
lote_2 = cursor.fetchall()
# Exibe ou processa o lote 2...



ou ainda 

tamanho_lote = 10  # Quantos registros você quer pegar por vez (LIMIT)
offset_atual = 0   # Começa do primeiro registro

while True:
    # Executa a query usando as variáveis
    cursor.execute("SELECT * FROM produtos LIMIT ? OFFSET ?", (tamanho_lote, offset_atual))
    lote = cursor.fetchall()
    
    # Se o lote vier vazio, significa que acabaram os registros no banco
    if not lote:
        break
        
    # Processa os dados do lote atual
    for row in lote:
        print(row)
        
    # Prepara o offset para o próximo ciclo (pula para o próximo bloco)
    offset_atual += tamanho_lote
'''