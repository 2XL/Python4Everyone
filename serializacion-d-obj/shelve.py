
try:
    import shelve
except ImportError, e:
    print e.code()
    print "no se encontro modulo"





"""
esto... haha

tenemos el modulo shelve que extiende pickle/ cPickle para proporcionar una forma de realizar la serializacion mas clara y sencilla
'acceder mediante una cadena asociada' -> estructura parecida a un diccionario
modulo:
    'shelve'
       funcion:
           open (args: 
               filename (enrealidad puede ser mas de un filenme ocultos al usuario))
               flag
               protocol -> que modelo : 0 , 1 , 2
               writeback    
    objeto tipo shelf
        atributs
            get
            has_key
            items
            keys
            values
            close
        
"""


# shelve.open(filename, flag, protocol, writeback) -> this returns object type Shelf -> podemos trabajar como un diccionario normal para almacenar i recuperar objetos



 
animales = ["piton", "mono", "camello"]
lenguajes = ["python", "mono", "perl"]
shelf = shelve.open("datos.dat")
shelf["primera"] = animales
shelf["segunda"] = lenguajes
print shelf["segunda"]
shelf.close()











