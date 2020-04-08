import threading

def imprime(num):
    print "soy el hilo", num
    

print "soy el hilo principal"

for i in range(0, 10):
    t = threading.Thread(target=imprime, args=(i,))
    t.start()
   # a = threading.Thread(group, target, name, args, kwargs, verbose)
"""
ademas de los parametros:
    target -> el nom de la funcio
    args    -> args en una tupla
    kwargs    -> un diccionari
    name -> nombre que tendra el thread
    verbose -> ...
    group -> en un futuro para un grupo de threads
    
comprobar:
    isAlive
    setName
    getName

funciones - threading.enumerate
                main_thread
            threading.activeCount
                consulta el numero de threads ejecutandose

objetos - Thread
    setDeamon - boolean indicando si se trata de un deamon
                - la aplicacion terminara de ejecutarse automaticamente, 
                 - terminando estos threads de forma segura.
                 
threading    
    Timer (hereda de thread)     
        - ejecutar run despues de un periodo de tiempo 
    cancel
        - cancelar la ejecucion antes de que termine el periodo de espera

"""