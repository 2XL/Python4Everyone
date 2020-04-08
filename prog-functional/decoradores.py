# un decorator es una funcion que recibe una funcio como parametro
# y devuelve otra funcio como resultado


def imp(var):
    print var

def mi_decorador(funcion):
    def nueva(*args):
        print "Llamada a la funcion", funcion.__name__
        retorno = funcion(*args)
        return retorno
    return nueva

imp("hola")

mi_decorador(imp)("hola")


@mi_decorador   # llama al decorador antes que la misma funcion xD, los deocradores se ejecutan de abajo a arriba
def imp(s):
    print s
    
    
imp("TROOL")
