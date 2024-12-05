# Clase Usuario
class Usuario:
    # Encapsulamiento: los atributos son privados para proteger los datos del usuario.
    def __init__(self, nombre, ID):
        self.__nombre = nombre  # Encapsulamiento
        self.__ID = ID          # Encapsulamiento

    def get_nombre(self):  # Método para acceder al atributo privado
        return self.__nombre

    def search_author(self, autor, catalogue):
        libros = catalogue.check_available_books(autor)
        print(f"Libros disponibles del autor {autor}:")
        for libro in libros:
            print(f"- {libro.titulo}")

    def checkout(self, libro_id, catalogue, loan):
        try:  # Manejo de errores con try-except
            libro = catalogue.get_libro_by_id(libro_id)
            if libro and libro.disponible:
                loan.checkout(libro, self)
                catalogue.update_catalogue(libro)
            else:
                print("El libro no está disponible.")
        except Exception as e:
            print(f"Error al realizar el préstamo: {e}")  # Manejo de errores


# Clase Catalogue
class Catalogue:
    def __init__(self):
        self.lista_libros = []  # Encapsulamiento: atributo privado opcionalmente

    def check_available_books(self, autor):
        return [
            libro
            for libro in self.lista_libros
            if libro.autor.lower() == autor.lower() and libro.disponible
        ]

    def get_libro_by_id(self, id):
        for libro in self.lista_libros:
            if libro.id == id:
                return libro
        return None

    def update_catalogue(self, libro):
        libro.disponible = False
        print("El catálogo ha sido actualizado.")


# Clase Libro
class Libro:
    # Encapsulamiento: control de atributos como privados
    def __init__(self, id, titulo, autor):
        self.__id = id          # Encapsulamiento
        self.__titulo = titulo  # Encapsulamiento
        self.__autor = autor    # Encapsulamiento
        self.disponible = True

    # Métodos para acceder a los atributos privados
    @property
    def id(self):
        return self.__id

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor


# Clase Loan
class Loan:
    # Polimorfismo: este método puede adaptarse para distintos tipos de usuarios
    def checkout(self, libro, usuario):
        print(f"Préstamo realizado: {libro.titulo} al usuario {usuario.get_nombre()}")

    def check_penalties(self, usuario):
        # Aquí se podrían validar sanciones, por ahora retorna False (sin sanciones)
        return False


# Clase Estudiante (Herencia)
class Estudiante(Usuario):  # Herencia: Estudiante hereda de Usuario
    def __init__(self, nombre, ID, carrera):
        super().__init__(nombre, ID)  # Llamada al constructor de Usuario
        self.carrera = carrera


# Función principal para probar el sistema
def main():
    # Crear usuarios, catálogo y sistema de préstamos
    usuario = Usuario("Juan Pérez", 1)
    estudiante = Estudiante("Ana López", 2, "Ingeniería")  # Ejemplo de herencia
    catalogue = Catalogue()
    loan = Loan()

    # Agregar libros al catálogo
    libro1 = Libro(1, "El Quijote", "Cervantes")
    libro2 = Libro(2, "1984", "Orwell")
    catalogue.lista_libros.extend([libro1, libro2])

    # Probar funcionalidades
    usuario.search_author("Cervantes", catalogue)
    usuario.checkout(1, catalogue, loan)

    # Probar con el estudiante
    estudiante.search_author("Orwell", catalogue)
    estudiante.checkout(2, catalogue, loan)


if __name__ == "__main__":
    main()