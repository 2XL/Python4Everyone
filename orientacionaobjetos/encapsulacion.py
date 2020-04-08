class Ejemplo:
    def publico(self):
        print "publico"
    
    def __privado(self):
        print "privado"
        
ej = Ejemplo()
ej.publico()
# ej.__privado()

# __arg <- es una variable privada o funcio privada o clase privada
# este mecanismo se concoe como name mangling
# se substituye __ por el nombre de la clase.. esto implica que 
# la clase no es realment privada i podamos acceder a el mediante una pequena trampa

ej._Ejemplo__privado()


class Fecha():
    def __init__(self):
        self.__dia=1
    def getDia(self):
        return self.__dia
    def setDia(self, dia):
        if dia > 0 and dia < 31:
            self.__dia=dia
        else:
            print "error dia range"

mi_fecha = Fecha()
mi_fecha.setDia(33)
            

class Data(object):
    def __init__(self):
        self.__dia=1
    def getDia(self):
        return self.__dia
    def setDia(self, dia):
        if dia > 0 and dia < 31:
            self.__dia = dia
        else:
            print "error"
    
    dia = property(getDia, setDia)
    
mi_fecha = Data()
mi_fecha.dia = 33 # para usar esto require heredar de object estilo JAVA xD
        
        