'''
Created on 17/02/2013

@author: Xiang
'''

# python editor.py hola.txt

import sys.argv

if(len(sys.argv)>1):
    print "Abriendo "+sys.argv[1]
else:
    print "Debes indicar el nombre del archivo"
