"""
class Queue
    cola fifo estructura de datos
    es familiar a las primitivas de threading para ahorarnos tener que sincronizar el acceso a los datos

"""
import threading, Queue

q = Queue.Queue()
class MiThread(threading.Thread):
    def __init__(self, q):
        self.q = q
        threading.Thread.__init__(self)
    def run(self):
        while True:
            try:
                obj = q.get(False)
            except Queue.Empty:
                print "Fin"
                break
            print obj

for i in range(10):
    q.put(i)
    
t = MiThread(q)
t.start()
t.join()