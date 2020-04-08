'''
Created on 17/02/2013

@author: Xiang
'''

import re
if re.match("python", "python"):
    print "cierto"
    
if re.match(".ython", "python"):
    print "cierto"    
    
    
if re.match("py*", "python"):
    print "cierto"    
    
    
        
if re.match("...\.", "abc."):
    print "cierto"    
    
if re.match("python|jython|cython", "python"):
    print "cierto"  
    
    
    
if re.match("(p|j|c)ython", "python"):
    print "cierto"  
    
    
    
if re.match("[pjc]ython", "python"):
    print "cierto"    

    
if re.match("python[0-9]", "python0"):
    print "cierto"     
    
    
if re.match("python[0-9a-zA-Z]", "python0"):
    print "cierto"       
    
    
    
    # python[.,]  <- siii
    # python[\.,] <- nooo
    
    
    # para negar un conjunto!!!
    # [^0-9a-z] <- ^
    
    
# equivalencias
"""
"\d”• : un dígito. Equivale a [0-9]
“\D”• : cualquier carácter que no sea un dígito. Equivale a [^0-9]
“\w”• : cualquier caracter alfanumérico. Equivale a [a-zA-Z0-9_]
“\W”• : cualquier carácter no alfanumérico. Equivale a [^a-zA-Z0-9_]
“\s”• : cualquier carácter en blanco. Equivale a [ \t\n\r\f\v]
“\S”• : cualquier carácter que no sea un espacio en blanco. Equivale a [^ \t\n\r\f\v]
""" 

# subcadenas
"""
“python+” describiría las cadenas “python”, “pythonn” y “pythonnn”, 
pero no “pytho”, ya que debe haber al menos una n.
    
    
El carácter * es similar a +, 
pero en este caso lo que se sitúa a su izquierda 
puede encontrarse cero o mas veces.    

El carácter ? indica opcionalidad, es decir, 
lo que tenemos a la izquierda puede o no aparecer (puede aparecer 0 o 1 veces).


Finalmente las llaves sirven para indicar 
el número de veces exacto que puede aparecer el carácter de la izquierda, 
o bien un rango de veces que puede aparecer. 
Por ejemplo {3} indicaría que tiene que aparecer exactamente 3 veces, 
{3,8} indicaría que tiene que aparecer de 3 a 8 veces,
{,8} de 0 a 8 veces y {3,} tres veces o mas (las que sean).


Otro elemento interesante en las expresiones regulares, para terminar, es la especificación de las posiciones en que se tiene que encontrar la cadena, esa es la utilidad de ^ y $, que indican, respectivamente, que el elemento sobre el que actúan debe ir al principio de la cadena o al final de esta.
^printcicio linea
final linea$
"""    
    
    
    