import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=""
)

print("conectado com sucesso!")

import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=""
    )