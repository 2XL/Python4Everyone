"""
decorator 110 page python para todos
import threading, time
 
    def synchronized(lock):
        def dec(f):
            def func_dec(*args, **kwargs):
                lock.acquire()
                try:
                    return f(*args, **kwargs)
                finally:
                    lock.release()
            return func_dec
        return dec

class MyThread(threading.Thread):
    @synchronized(mi_lock)
    def run(self):
        print "metodo sincronizado"
        """
        
        
        
        
        
        
        
        