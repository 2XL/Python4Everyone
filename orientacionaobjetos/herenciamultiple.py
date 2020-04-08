class Terrestre:
    def desplazar(self):
        print "El animal anda"

class Acuatico:
    def desplazar(self):
        print "el animal nada"
# HERENCIA MULTIPLE
""" EN PYTHON A DIFERENCIA DE LOS OTROS LENGUAJES COMO JAVA O C... """
# de las uqe hereda separados por comas:

class Cocodrilo(Terrestre, Acuatico):
    pass

c=Cocodrilo()
c.desplazar()   # terrestre se encuentra mas a la izquierda por lo tanto se imprimira andar

