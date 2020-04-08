



"""
pydoc is too simple
    no complex sematic options and styles
"""


 


""" Modulo para ejemplificar el uso de epydoc. """
class Persona:
    """Mi clase de ejemplo."""
    def __init__(self, nombre):
        """Inicializador de la clase Persona."""
        self.nombre = nombre
        self.mostrar_nombre()
    def mostrar_nombre(self):
        """Imprime el nombre de la persona"""
        print "Esta es la persona %s" % self.nombre
    
class Empleado(Persona):
    """Subclase de Persona."""
    pass
if __name__ == "__main__":
    raul = Persona("Raul")


 

''' hay que instalar etc... pydoc  me lo salto xD'''








