import sys  # Importa el módulo sys para utilizar funcionalidades relacionadas con el sistema.
from usuario import Usuario  # Importa la clase Usuario desde el módulo usuario.
from usuario_dao import UsuarioDao  # Importa la clase UsuarioDao desde el módulo usuario_dao.

class MenuAppUsuario:
    def __init__(self):
        self.usuario_dao = UsuarioDao()  # Inicializa un objeto de UsuarioDao.

    def mostrar_menu(self):
        print("1. Listar usuarios")  # Opción para listar usuarios.
        print("2. Agregar usuario")  # Opción para agregar un nuevo usuario.
        print("3. Actualizar usuario")  # Opción para actualizar un usuario existente.
        print("4. Eliminar usuario")  # Opción para eliminar un usuario existente.
        print("5. Salir")  # Opción para salir de la aplicación.

    def procesar_opcion(self, opcion):
        if opcion == 1:  # Si la opción es 1, llama al método para listar usuarios.
            self.listar_usuarios()
        elif opcion == 2:  # Si la opción es 2, llama al método para agregar un usuario.
            self.agregar_usuario()
        elif opcion == 3:  # Si la opción es 3, llama al método para actualizar un usuario.
            self.actualizar_usuario()
        elif opcion == 4:  # Si la opción es 4, llama al método para eliminar un usuario.
            self.eliminar_usuario()
        elif opcion == 5:  # Si la opción es 5, muestra un mensaje y termina el programa.
            print("Saliendo...")
            sys.exit(0)  # Sale del programa con código de salida 0.
        else:  # Si la opción no es ninguna de las anteriores, muestra un mensaje de error.
            print("Opción inválida. Intente nuevamente.")

    def listar_usuarios(self):
        usuarios = self.usuario_dao.seleccionar()  # Obtiene la lista de usuarios desde el DAO.
        for usuario in usuarios:  # Itera sobre la lista de usuarios y los imprime uno por uno.
            print(usuario)

    def agregar_usuario(self):
        username = input("Ingrese el nombre de usuario: ")  # Solicita al usuario que ingrese el nombre.
        password = input("Ingrese la contraseña: ")  # Solicita al usuario que ingrese la contraseña.
        usuario_id = self.usuario_dao.insertar(Usuario(None, username, password))  # Inserta el usuario en la base de datos.
        print(f"Usuario agregado con ID: {usuario_id}")  # Imprime el ID del usuario agregado.

    def actualizar_usuario(self):
        usuario_id = int(input("Ingrese el ID del usuario a actualizar: "))  # Solicita al usuario que ingrese el ID del usuario a actualizar.
        username = input("Ingrese el nuevo nombre de usuario: ")  # Solicita al usuario que ingrese el nuevo nombre de usuario.
        password = input("Ingrese la nueva contraseña: ")  # Solicita al usuario que ingrese la nueva contraseña.
        self.usuario_dao.actualizar(Usuario(usuario_id, username, password))  # Actualiza el usuario en la base de datos.
        print(f"Usuario con ID {usuario_id} actualizado.")  # Imprime un mensaje de confirmación.

    def eliminar_usuario(self):
        usuario_id = int(input("Ingrese el ID del usuario a eliminar: "))  # Solicita al usuario que ingrese el ID del usuario a eliminar.
        self.usuario_dao.eliminar(Usuario(usuario_id, None, None))  # Elimina el usuario de la base de datos.
        print(f"Usuario con ID {usuario_id} eliminado.")

if __name__ == "__main__":
    app = MenuAppUsuario()  # Crea una instancia de la clase MenuAppUsuario.
    while True:  # Bucle infinito para mostrar el menú continuamente.
        app.mostrar_menu()  # Muestra el menú de la aplicación.
        opcion = int(input("Seleccione una opción: "))  # Solicita al usuario que seleccione una opción del menú.
        app.procesar_opcion(opcion)  # Procesa la opción seleccionada por el usuario.
