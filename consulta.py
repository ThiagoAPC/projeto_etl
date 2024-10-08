import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('vendas_alimentadas.db')
cursor = conn.cursor()

# Fazer uma consulta para verificar os primeiros registros
cursor.execute("SELECT * FROM vendas LIMIT 10")

# Pegar os resultados
rows = cursor.fetchall()

# Exibir os resultados
for row in rows:
    print(row)

# Fechar a conexão
conn.close()
