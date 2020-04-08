"""
disponemos de dos librerias dedicadas
1r basica:
    thread
2n derivada:
    threading   -> apartir del primero i basado en el modulo threads de java
    """
    
    
    
import threading

class Mithread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num
    
    def run(self):
        print "Soy el hilo", self.num
        

print "soy el hilo principal"

for i in range(0, 10):
    t = Mithread(i)
    t.start()
    t.join()    # serve para que el prograna se quede bloqueado hasta que no se haya terminado todos los hilos
    # puede tomar como parametro un float para indicar el maximo tiempo en espera
    # si se intenta llamar a start par aun hilo en ejecucion obtendremos un error excepcion