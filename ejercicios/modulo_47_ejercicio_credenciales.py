import hashlib

def obtener_nombre_fichero(email : str) -> str:
    """
    Genera el nombre del fichero.

    :param email: dirección de correo electrónico
    :return: el nombre del fichero
    """
    EXTENSION = '.credentials'
    nombre_fichero = email + EXTENSION
    return nombre_fichero


def obtener_hash_sha256(texto:str) -> bytes:
    """
    Proporciona un hash utilizando el algoritmo SHA256.
    
    :param texto: texto a convertir
    :return: el hash del texto 
    """
    implementacion = hashlib.sha256()
    implementacion.update(texto.encode('utf-8'))
    hash = implementacion.digest()
    return hash


def guardar_credenciales(email:str, password_en_claro:str):
    """
    Guarda el hash de la contraseña en un fichero.
    
    :param email: email de la credencial
    :param password_en_claro: contraseña de la credencial
    """
    nombre_fichero = obtener_nombre_fichero(email)
    hash = obtener_hash_sha256(password_en_claro)
    with open(nombre_fichero, mode='wb') as fichero:
        fichero.write(hash)


"""
def leer_hash_fichero(email) -> hash

def validar_credenciales(email, password) -> bool
	- Leer el hash del fichero -> hash del disco duro ->leer_hash_fichero
	- Generar un hash con el password introducido -> obtener_hash()
	- Comparar los hash

mario@gmail.com.credentials (hash)
"""

# 1. Registro
# Pedir usuario y contraseña
# Obtener el hash de la contraeña
# Guardar el hash en un fichero

# 2. Validación
# Pedir usuario y contraseña
# Obtener el hash de la contraseña
# Leer el hash almacenado
# Comprobar que son iguales