class Usuario:
    def __init__(self, id_usuario, nombre, apellido, mail, direccion, telefono):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"ID: {self.id_usuario}\nNombre: {self.nombre}\nApellido: {self.apellido}\nMail: {self.mail}\nDirección: {self.direccion}\nTeléfono: {self.telefono}"

if __name__ == "__main__":
    
    usuario1 = Usuario(1, "Matias", "Montealegre", "matias.montealegre@davinci.edu.ar", "Av Cordoba 130", "1122334455")

    
    print(usuario1)
