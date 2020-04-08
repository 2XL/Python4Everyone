# en python todo son objetos y las funciones no son una excepcion

def saludar(lang):
    def saludar_es():
        print "Hola"
    def saludar_en():
        print "Hello"
    def saludar_fr():
        print "Salut"
    #diccionario
    lang_func = {"es": saludar_es,
                 "en": saludar_en,
                 "fr": saludar_fr}
    return lang_func[lang]

f=saludar("es")
saludar("en")() # primer parentesis indica instancia, 2n indica crida