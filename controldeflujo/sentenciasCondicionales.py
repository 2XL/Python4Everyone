from random import randint


fav="pcrigger.com"
# si (if) fav es igual a "pcrigger.com"
if fav == "pcrigger.com":
    print "LoL, Welcome Troll!"
    print "endLine"
    
# if ... else

if fav  != "ola":
        print "this was not ola!"

if fav != "pcrigger.com":
    print "this is not pcrigger.com"
else:
    print "this is it!"  
    
    
# if...elseif...elseif
numero = 10
if numero < 0:
    print "negativo"
elif numero > 0:
    print "positivo"
else:
    print "Cero"
    
# A if C else B
num=10
var = "par" if (num % 2 == 0) else "impar"
print num 
print 'es'
print var

# en python no existe switch xD
# se tendira que emular con el diccionario
