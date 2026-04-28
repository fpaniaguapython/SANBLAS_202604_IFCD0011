"""
def obtener_nombre_fichero(email : str) -> str:
	# Concatena credentials
	# Input -> nayra2680@yahoo.com
	# Output -> nayra2680@yahoo.com.credentials

def guardar_credenciales(email, password_en_claro)
	# Guarda el hash

def obtener_hash(password_en_claro) -> bytes

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