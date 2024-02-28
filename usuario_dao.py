from conexion import Conexion
from usuario import Usuario


class UsuarioDao:
    # Consultas SQL predefinidas
    SELECCIONAR = "SELECT * FROM usuarios"
    INSERTAR = "INSERT INTO usuarios (username, password) VALUES (%s, %s)"
    ACTUALIZAR = "UPDATE usuarios SET username=%s, password=%s WHERE id_usuario=%s"
    ELIMINAR = "DELETE FROM usuarios WHERE id_usuario=%s"
    
    @classmethod
    def seleccionar(cls):
        # Método para seleccionar todos los usuarios de la base de datos
        with Conexion.obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(cls.SELECCIONAR)
                resultados = cursor.fetchall()  # Obtiene todos los resultados de la consulta
                # Crea una lista de objetos Usuario a partir de los resultados
                usuarios = [Usuario(*fila) for fila in resultados]
        return usuarios
    
    @classmethod
    def insertar(cls, usuario):
        # Método para insertar un nuevo usuario en la base de datos
        with Conexion.obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(cls.INSERTAR, (usuario.username, usuario.password))
                conn.commit()  # Confirma la transacción
                usuario.id_usuario = cursor.lastrowid  # Obtiene el ID del usuario insertado
    
    @classmethod
    def actualizar(cls, usuario):
        # Método para actualizar un usuario existente en la base de datos
        with Conexion.obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(cls.ACTUALIZAR, (usuario.username, usuario.password, usuario.id_usuario))
                conn.commit()  # Confirma la transacción
    
    @classmethod
    def eliminar(cls, usuario):
        # Método para eliminar un usuario de la base de datos
        with Conexion.obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(cls.ELIMINAR, (usuario.id_usuario,))
                conn.commit()
