# Clase Usuario
class Usuario:
    # Encapsulamiento: los atributos son privados para proteger los datos del usuario.
    def __init__(self, nombre, ID):
        self.__nombre = nombre  # Atributo privado (encapsulamiento)
        self.__ID = ID          # Atributo privado (encapsulamiento)

    def get_nombre(self):  # Método para acceder al atributo privado (encapsulamiento)
        return self.__nombre

    def search_author(self, autor, catalogue):
        # Método para buscar libros por autor en el catálogo
        libros = catalogue.check_available_books(autor)
        print(f"Libros disponibles del autor {autor}:")
        for libro in libros:
            print(f"- {libro.titulo}")

    def checkout(self, libro_id, catalogue, loan):
        try:  # Manejo de errores con try-except
            libro = catalogue.get_libro_by_id(libro_id)
            if libro and libro.disponible:
                # Realizar el préstamo si el libro está disponible
                loan.checkout(libro, self)
                catalogue.update_catalogue(libro)  # Actualizar el catálogo
            else:
                print("El libro no está disponible.")
        except Exception as e:
            # Capturar cualquier error que ocurra durante el proceso de préstamo
            print(f"Error al realizar el préstamo: {e}")


# Clase Catalogue
class Catalogue:
    def __init__(self):
        # Lista de libros disponibles en el catálogo
        self.lista_libros = []  # Lista de libros (puede considerarse encapsulada)

    def check_available_books(self, autor):
        # Retorna una lista de libros disponibles de un autor en particular
        return [
            libro
            for libro in self.lista_libros
            if libro.autor.lower() == autor.lower() and libro.disponible
        ]

    def get_libro_by_id(self, id):
        # Busca un libro por su ID en la lista de libros
        for libro in self.lista_libros:
            if libro.id == id:
                return libro
        return None

    def update_catalogue(self, libro):
        # Actualiza el estado del libro a no disponible
        libro.disponible = False
        print("El catálogo ha sido actualizado.")


# Clase Libro
class Libro:
    # Encapsulamiento: control de atributos como privados
    def __init__(self, id, titulo, autor):
        self.__id = id          # Atributo privado
        self.__titulo = titulo  # Atributo privado
        self.__autor = autor    # Atributo privado
        self.disponible = True  # Por defecto, todos los libros están disponibles

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
        # Método para registrar el préstamo de un libro a un usuario
        print(f"Préstamo realizado: {libro.titulo} al usuario {usuario.get_nombre()}")

    def check_penalties(self, usuario):
        # Validación de posibles sanciones (no implementado en este ejemplo)
        return False


# Clase Estudiante (Herencia)
class Estudiante(Usuario):  # Herencia: Estudiante hereda de Usuario
    def __init__(self, nombre, ID, carrera):
        # Llamada al constructor de la clase padre (Usuario)
        super().__init__(nombre, ID)
        self.carrera = carrera  # Atributo adicional para estudiantes


# Función principal para probar el sistema
def main():
    # Crear usuarios, catálogo y sistema de préstamos
    usuario = Usuario("Juan Pérez", 1)  # Usuario regular
    estudiante = Estudiante("Ana López", 2, "Ingeniería")  # Usuario con herencia
    catalogue = Catalogue()
    loan = Loan()

    # Agregar libros al catálogo
    libro1 = Libro(1, "El Quijote", "Cervantes")
    libro2 = Libro(2, "1984", "Orwell")
    catalogue.lista_libros.extend([libro1, libro2])  # Agregar libros al catálogo

    # Probar funcionalidades
    usuario.search_author("Cervantes", catalogue)  # Buscar libros por autor
    usuario.checkout(1, catalogue, loan)  # Realizar préstamo

    # Probar con el estudiante
    estudiante.search_author("Orwell", catalogue)  # Buscar libros por autor
    estudiante.checkout(2, catalogue, loan)  # Realizar préstamo


# Entry point del programa
if __name__ == "__main__":
    main()