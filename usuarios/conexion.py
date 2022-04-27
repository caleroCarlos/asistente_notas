# Modulos
import mysql.connector

def conectar():
    # Conexion base de datos
    database = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'mp',
        port = 3306
    )
    # Cursor para interactuar con la BD
    cursor = database.cursor(buffered = True)

    return[database, cursor]