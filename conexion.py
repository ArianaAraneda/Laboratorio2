import psycopg2  # Importa el módulo psycopg2 para interactuar con la base de datos PostgreSQL.
from psycopg2.pool import SimpleConnectionPool  # Importa la clase SimpleConnectionPool del módulo psycopg2.pool.
import logger_base  # Importa el módulo logger_base que contiene la configuración de la base de datos.

#Clase Conexion que proporciona métodos para administrar un pool de conexiones a la bd PostgreSQL
class Conexion:
    _pool = None  # Variable de clase para almacenar el pool de conexiones.

    @classmethod
    def obtener_pool(cls):
        # Método de clase para obtener el pool de conexiones.
        if cls._pool is None:
            try:
                # Intenta crear un nuevo SimpleConnectionPool si no existe.
                cls._pool = SimpleConnectionPool(
                    minconn=logger_base.MIN_CON,  # Número mínimo de conexiones en el pool.
                    maxconn=logger_base.MAX_CON,  # Número máximo de conexiones en el pool.
                    dsn=f"dbname={logger_base.DATABASE} user={logger_base.USERNAME} password={logger_base.PASSWORD} host={logger_base.HOST} port={logger_base.DB_PORT}"  # Cadena de conexión a la base de datos.
                )
            except Exception as e:
                print(f"Error al inicializar el pool: {e}")  # Imprime un mensaje de error si ocurre una excepción durante la inicialización del pool.
        return cls._pool  # Devuelve el pool de conexiones.

    @classmethod
    def obtener_conexion(cls):
        # Método de clase para obtener una conexión del pool.
        con = cls.obtener_pool().getconn()  # Obtiene una conexión del pool.
        return con  # Devuelve la conexión.

    @classmethod
    def liberar_conexion(cls, conexion):
        # Método de clase para liberar una conexión y devolverla al pool.
        cls.obtener_pool().putconn(conexion)  # Devuelve la conexión al pool.

    @classmethod
    def cerrar_conexiones(cls):
        # Método de clase para cerrar todas las conexiones en el pool.
        cls.obtener_pool().closeall()  # Cierra todas las conexiones en el pool.
