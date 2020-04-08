"""



serializacion or marshalling
    existe varios modulos:
        marshal    -> basico i mas primitivo -> su objetivo principal es trabajar con bytecodes (file.pyc)
                no comprueba
                no seguridad
                solo objetos simples
                no compatible entre versiones (inadecuado par mucho tiempo)
                escrito en .c (es mas rapido)
        pickle
                casi cualquier objeto
                seguridad basica
                mas complejo
                escrito en .py (es mucho mas lento)
                
        cPickle
                verion .c de pickle si el factor tiempo es relevante 1000 veces mas rapido que pickle == marshal
        shelve
        



"""

try:
    import cPickle as pickle
except ImportError:
    import pickle
    
    # llamar a una funcion dump (con arg: objeto a serializar, objeto archivo en el que guardarlo (con permisos read realine write)) para serializar



fichero = file("datos.dat", "w")
animales = ["piton", "mono", "camello"]
pickle.dump(animales, fichero)
fichero.close()


# pickle.dump(obj, file, protocol)

# protocol -> indica el protocol a utilitzar al guardar : defecto 0 (txt, menos eficiente)
    # alternativo: 1 mas eficiente que 0 menos que 2 (usan bin)
    # alternativa: 2 el mas eficiente (usan bin)

"""


"""











