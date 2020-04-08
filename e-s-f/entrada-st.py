'''
Created on 17/02/2013

@author: Xiang
'''




nombre = raw_input("Como te llamas? ")
print "Encantado, " + nombre


try:
    edad = raw_input("Cuantos anyos tienes? ")
    dias = int(edad) * 365
    print "Has vivido " + str(dias) + " dias"
except ValueError:
    print "Eso no es un numero"






