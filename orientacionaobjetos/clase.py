class Coche:
    """ Abstraccion de los objetos coche"""
    
# lo primero que llama la atencio en el ejemplo anterior es el nombre tan curioso que tiene el metodo __init__. Este es
# una convencion y mp un caprichjo. El metodo __init__, conuna doble barra baja al principio y final del nombre,se ejecuta justo despuesde de crear unn nuevo objeto a partir de la clase
# proceso quese conoce con el nombre de instanciacion



# la finalidad es para realizar cualquier proceso de incializacion que sea necesario
# este se ejecuta justo despues de crear un nuevo objeto
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print "Tenemos", gasolina, "litros"
        
 
    def arrancar(self):
        if self.gasolina > 0:
            print "Arranca"
        else:
            print "No arranca"


    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -=1
            print "Queden", self.gasolina, "litros"
        else:
            print "No se mueve"
            
 
mi_coche=Coche(3)

mi_coche.arrancar()

mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()


mi_coche.arrancar()





















    