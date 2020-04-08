




def division(a, b):
    return a / b
def calcular():
    division(1, 0)



try:
    calcular()
except ZeroDivisionError:
        print " multi plica por zero "


try:
    f = file("archivo.txt")
except:
    print "El archivo no existe"



try:
    num = int("3a")
    print num
except NameError:
    print "La variable no existe"
except ValueError:
    print "El valor no es un numero"


try:
    num = int("13a")
    print num
except (NameError, ValueError):
    print "Ocurrio un error"



try:
    num = 33
except:
    print "Hubo un error!"
else:
    print "Todo esta bien"



x=0
y=1
try:
    z = x / y
except ZeroDivisionError:
    print "Division por cero"
finally:                # se ejecuta siempre se produzca o no error
    print "Limpiando"


# propios excepciones

class MiError(Exception):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return "Error " + str(self.valor)
    
resultado=21
try: 
    if resultado > 20:
        raise MiError(33)
except MiError, e:
    print e





