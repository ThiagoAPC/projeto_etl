import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('vendas_com_problemas.db')

# Extrair os dados da tabela de vendas para um DataFrame
df_vendas = pd.read_sql_query("SELECT * FROM vendas", conn)

# ---- ETAPA 1: VERIFICAÇÃO E REMOÇÃO DE DUPLICATAS ----
# Verificar e remover duplicatas
df_vendas.drop_duplicates(inplace=True)

# ---- ETAPA 2: TRATAMENTO DE VALORES NULOS ----
# Verificar valores nulos em cada coluna
print("Valores nulos por coluna:")
print(df_vendas.isnull().sum())

# Tratamento de valores nulos
# 1. Preencher valores nulos de 'quantidade' e 'preco_unitario' com a média da coluna
df_vendas['quantidade'].fillna(df_vendas['quantidade'].mean(), inplace=True)
df_vendas['preco_unitario'].fillna(df_vendas['preco_unitario'].mean(), inplace=True)

# 2. Preencher 'desconto' nulo com 0 (assumindo que pode não ter desconto)
df_vendas['desconto'].fillna(0, inplace=True)

# 3. Para colunas de informações textuais (nome_cliente, cidade_cliente, etc.), vamos preencher com 'Desconhecido' ou remover, conforme o contexto.
df_vendas['nome_cliente'].fillna('Desconhecido', inplace=True)
df_vendas['cidade_cliente'].fillna('Desconhecido', inplace=True)
df_vendas['forma_pagamento'].fillna('Indefinido', inplace=True)

# ---- ETAPA 3: CORREÇÃO DE INCONSISTÊNCIAS ----
# Verificar e corrigir inconsistências, como valores totais que não fazem sentido
df_vendas['valor_total'] = df_vendas['preco_unitario'] * df_vendas['quantidade'] - df_vendas['desconto']

# Verificar se algum valor total ficou negativo após os ajustes
df_inconsistentes = df_vendas[df_vendas['valor_total'] < 0]
if not df_inconsistentes.empty:
    print("Registros com valor total negativo:")
    print(df_inconsistentes)

# Corrigir valores totais negativos (definir como 0 ou recalcular)
df_vendas['valor_total'] = df_vendas['valor_total'].apply(lambda x: x if x >= 0 else 0)

# ---- ETAPA 4: CARREGAMENTO DOS DADOS TRANSFORMADOS ----
# Conectar a um novo banco de dados para salvar os dados transformados
conn_transformed = sqlite3.connect('vendas_transformadas.db')

# Carregar os dados transformados em uma nova tabela
df_vendas.to_sql('vendas_transformadas', conn_transformed, if_exists='replace', index=False)

# Fechar as conexões
conn.close()
conn_transformed.close()

print("ETL concluído: dados transformados e carregados no banco de dados 'vendas_transformadas.db'.")
