import psycopg2  # Importa el módulo psycopg2 para interactuar con la base de datos PostgreSQL.

#Clase que permite utilizar un cursor de base de datos, 
#garantizando que el cursor se cierre correctamente 
class CursorDelPool:
    def __init__(self):
        self._con = None  # Inicializa la conexión como None al principio.
        self._cursor = None  # Inicializa el cursor como None al principio.

    def __enter__(self):
        from conexion import Conexion  # Importa la clase Conexion solo cuando sea necesaria.
        self._con = Conexion.obtener_conexion()  # Obtiene una conexión del pool.
        self._cursor = self._con.cursor()  # Crea un cursor asociado a la conexión.
        return self._cursor  # Devuelve el cursor.

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cerrar()  # Llama al método cerrar al salir del bloque 'with'.
        from conexion import Conexion  # Importa la clase Conexion solo cuando sea necesaria.
        Conexion.liberar_conexion(self._con)  # Libera la conexión y la devuelve al pool.

    def cerrar(self):
        if self._cursor is not None:  # Verifica si el cursor no es None.
            self._cursor.close()  # Cierra el cursor.
            self._con = None  # Establece la conexión como None.
            self._cursor = None  # Establece el cursor como None.
