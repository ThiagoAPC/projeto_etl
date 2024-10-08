#O objteivo aqui é criar um BD cheio de problemas pra poder fazer o ETL depois, pra treino
import sqlite3
from faker import Faker
import random
import numpy as np  # Para gerar valores nulos

# Instanciar o gerador de dados fictícios
fake = Faker('pt_BR')

# Conectar ou criar o banco de dados
conn = sqlite3.connect('vendas_com_problemas.db')
cursor = conn.cursor()

# Criar a tabela de vendas com possibilidade de valores nulos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
        id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
        data_venda DATE,
        id_produto INTEGER,
        nome_produto TEXT,
        categoria_produto TEXT,
        preco_unitario FLOAT,
        quantidade INTEGER,
        desconto FLOAT,
        valor_total FLOAT,
        id_cliente INTEGER,
        nome_cliente TEXT,
        cidade_cliente TEXT,
        estado_cliente TEXT,
        forma_pagamento TEXT,
        id_vendedor INTEGER,
        nome_vendedor TEXT,
        canal_venda TEXT
    )
''')

# Função para gerar dados fictícios de vendas com erros
def gerar_vendas_com_erros(n):
    categorias = ['Eletrônicos', 'Acessórios', 'Eletrodomésticos', 'Móveis', 'Roupas', 'Brinquedos']
    produtos = {
        'Eletrônicos': ['Notebook', 'Smartphone', 'Tablet', 'Smartwatch', 'Monitor'],
        'Acessórios': ['Mouse', 'Teclado', 'Fone de Ouvido', 'Carregador', 'Cabo HDMI'],
        'Eletrodomésticos': ['Geladeira', 'Microondas', 'Máquina de Lavar', 'Fogão', 'Aspirador'],
        'Móveis': ['Cadeira', 'Mesa', 'Sofá', 'Cama', 'Armário'],
        'Roupas': ['Camiseta', 'Calça', 'Vestido', 'Casaco', 'Sapato'],
        'Brinquedos': ['Lego', 'Boneca', 'Carrinho', 'Pipa', 'Jogo de Tabuleiro']
    }
    formas_pagamento = ['Cartão de Crédito', 'Boleto', 'Pix', 'Dinheiro', 'Transferência Bancária']
    canais_venda = ['Online', 'Loja Física']

    vendas = []
    for _ in range(n):
        categoria_produto = random.choice(categorias)
        nome_produto = random.choice(produtos[categoria_produto])
        preco_unitario = round(random.uniform(50, 5000), 2) if random.random() > 0.1 else None  # 10% valores nulos
        quantidade = random.randint(1, 5) if random.random() > 0.05 else None  # 5% valores nulos
        desconto = round(random.uniform(0, 20), 2) if random.random() > 0.15 else None  # 15% valores nulos
        valor_total = round((preco_unitario or 0) * (quantidade or 0) - (desconto or 0), 2)
        id_cliente = random.randint(1000, 9999)
        id_vendedor = random.randint(100, 999)
        
        # Simulação de dados inconsistentes
        nome_cliente = fake.name() if random.random() > 0.1 else None  # 10% sem nome de cliente
        cidade_cliente = fake.city() if random.random() > 0.05 else None  # 5% sem cidade
        forma_pagamento = random.choice(formas_pagamento) if random.random() > 0.05 else None  # 5% sem forma de pagamento
        
        venda = (
            fake.date_this_year(),                  # data_venda
            random.randint(1, 1000),                # id_produto
            nome_produto,                           # nome_produto
            categoria_produto,                      # categoria_produto
            preco_unitario,                         # preco_unitario
            quantidade,                             # quantidade
            desconto,                               # desconto
            valor_total,                            # valor_total
            id_cliente,                             # id_cliente
            nome_cliente,                           # nome_cliente
            cidade_cliente,                         # cidade_cliente
            fake.state_abbr(),                      # estado_cliente
            forma_pagamento,                        # forma_pagamento
            id_vendedor,                            # id_vendedor
            fake.name(),                            # nome_vendedor
            random.choice(canais_venda)             # canal_venda
        )
        vendas.append(venda)
    
    return vendas

# Gerar e inserir 1000 vendas fictícias com erros
vendas_com_erros = gerar_vendas_com_erros(1000)

cursor.executemany('''
    INSERT INTO vendas (data_venda, id_produto, nome_produto, categoria_produto, preco_unitario, quantidade, desconto, valor_total, id_cliente, nome_cliente, cidade_cliente, estado_cliente, forma_pagamento, id_vendedor, nome_vendedor, canal_venda)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', vendas_com_erros)

# Commit e fechar a conexão
conn.commit()
conn.close()

print("Banco de dados criado e alimentado com dados inconsistentes!")
