
# sincronizar acceso a ciertos recursos

"""
mediante mecanismos:
    threading
    -- estados posibles ?  adquirido : libre
        lock                 -> mutex (mutua exclusion)
        locks reentrantes    -> exclusion mutua
            acquire
            release
        semaforos            -> 
        condiciones
        eventos
        

"""
import threading

lista = []
lock = threading.Lock()
def anyadir(obj):
    lock.acquire()
    lista.append(obj)
    lock.release()
def obtener():
    lock.acquire()
    obj = lista.pop()
    lock.release()
    return obj


import urllib

semaforo = threading.Semaphore(4)
def descargar(url):
    semaforo.acquire()
    urllib.urlretrieve(url)
    semaforo.release()

lista = []
cond = threading.Condition()
def consumir():
    cond.acquire()
    cond.wait()
    obj = lista.pop()
    cond.release()
    return obj
def producir(obj):
    cond.acquire()
    lista.append(obj)
    cond.notify()
    cond.release()



