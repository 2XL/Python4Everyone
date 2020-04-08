

import threading

# crear zona de memoria privada para threads


datos_locales = threading.local()
datos_locales.mi_var = "hola"
print datos_locales.mi_var


local = threading.local()
def f():
    print local.var
    
local.var = "hola"
t = threading.Thread(target=f)
print local.var
t.start()
t.join()

"""

hola
hola
Exception in thread Thread-1:
Traceback (most recent call last):
  File "C:\Python27\lib\threading.py", line 551, in __bootstrap_inner
    self.run()
  File "C:\Python27\lib\threading.py", line 504, in run
    self.__target(*self.__args, **self.__kwargs)
  File "C:\Users\Xiang\Coding\PythonParaTodos\threads\datos-globales-indep.py", line 15, in f
    print local.var
AttributeError: 'thread._local' object has no attribute 'var'

"""