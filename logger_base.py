#Define variables de configuración para la conexión a la base de datos, 
#como el nombre de la base de datos, el nombre de usuario, la contraseña,
# el puerto y el host.

# Definición de parámetros de conexión a la base de datos
DATABASE = "laboratorio_usuarios"  # Nombre de la base de datos
USERNAME = "usuario"  # Nombre de usuario para la conexión
PASSWORD = "ariana"  # Contraseña del usuario para la conexión
DB_PORT = "5432"  # Puerto de la base de datos
HOST = "localhost"  # Dirección del servidor de la base de datos

# Configuración del pool de conexiones
MIN_CON = 1  # Número mínimo de conexiones en el pool
MAX_CON = 5  # Número máximo de conexiones en el pool
