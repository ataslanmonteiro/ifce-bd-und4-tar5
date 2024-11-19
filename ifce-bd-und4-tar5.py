import mysql.connector

# Conexão com o servidor MySQL
cnx = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="1234",
    database="banco_monteiro"
)

# Criação de um cursor
cur = cnx.cursor()

# Executa uma consulta SQL
cur.execute("SELECT CURDATE()")

# Recupera e imprime o resultado
row = cur.fetchone()
print("Data atual é:", row[0])

# Fecha a conexão
cur.close()
cnx.close()