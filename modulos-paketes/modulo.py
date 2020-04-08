def mi_func():
    print "una funcion"
    
class MiClass:
    def __init__(self):
        print "una clase"
        
print "un modulo"

import os, sys, time
print time.asctime()

from time import asctime

print asctime()

from abc import *   # esto es una mal practica

import sys
sys.path


# atributos especiales de modulos
# __name__
# __doc__   
# los modulos tambien son clases