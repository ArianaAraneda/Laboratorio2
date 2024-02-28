class Usuario:
    def __init__(self, id_usuario, username, password):
        # Constructor de la clase Usuario que inicializa los atributos del usuario.
        self.id_usuario = id_usuario  # ID único del usuario.
        self.username = username  # Nombre de usuario.
        self.password = password  # Contraseña del usuario.

    def __str__(self):
        # Método especial que devuelve una representación de cadena del objeto Usuario.
        return f"Usuario(id_usuario={self.id_usuario}, username={self.username}, password={self.password})"
