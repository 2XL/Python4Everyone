print "hola mundo"

print "Hola\n\n\tmundo"
print "hola",
print "mundo",
print "hola","mundo",
print "hola"+"mundo"

print "cuesta", 5, "euros"
try:
    print "cuesta"+5+"euros"
except TypeError:
    print "format str and int error"
    
print "hola %s" % "mundo"
print "%s %s" % ("hola","mundo")

"""
%s        Cadena
%d        Entero
%o        Octal
%x        Hexadecimal
%f        Real
"""

print "%10s mundo" % "holaaaaaaaaaaa"

print "%-10s mundo" % "holaaaaaaaaaaaaa"





from math import pi


print "%.100f" % pi

# 3.141592653589793115997963468544185161590576171875


print "%.4s" % "hola mundo"






