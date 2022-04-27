# Modulos
import datetime
import hashlib
from sqlite3 import Cursor
from unittest import result
import usuarios.conexion as conexion

# Instancio el modulo de conexion para conectarme a la BD
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


## Clases ##
class Usuario:
    # Atributos
    # Constructor para los atributos
    def __init__(self,nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
    
    # Metodos
    # Meteodo para registrarse como usurio
    def registrar(self):
        date = datetime.datetime.now()
        # Cifrado de contraseña 
        cifrado = hashlib.sha256() # Instancio en la variable cifrado el modulo hashlib con el metodo de cifrado .sha256()
        cifrado.update(self.password.encode('utf8')) # le paso a esta nueva instancia la contraseña en bit con el metodo encode('utf8')

        sql = 'INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)'
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), date) # Guardo el valor hexadecimal de la password con el metodo .hexdigest()
        
        # Capturo erro al registrar un usario con email ya existente
        try:
            cursor.execute(sql,usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result


    def identificar(self):
        # Consulta a BD para comprobar si existe el usuario
        sql = 'SELECT * FROM usuarios WHERE email = %s AND password = %s'
        
        # Cifrado de contraseña 
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        # Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        # Ejecucion de consulta
        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result
        