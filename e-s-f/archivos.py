'''
Created on 17/02/2013

@author: Xiang
'''

f = open("meme.txt", "r")

# la lectura de archivos
while True:
    linea = f.readline()
    if not linea: break
    print linea,
# read - readline - readlines

completo = f.read() # devuelve una cadena con el contenido del archivo
parte = f.read(1) # devuelve una cadena con el contenido en bytes limitado

print parte


















