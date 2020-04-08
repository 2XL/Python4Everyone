# tipos: entero/coma flotante/ complejos/ strings/ booleans

# esto es una cadena
c = "Hola Mundo"

# y esto es un entero
e = 21

# podemos comprobar con la funcion type
print type(c)
print type(e)

# type (enteros) devolveria int
entero = 23
enteroL = 21L
print type(enteroL)
# asignacion ocatal

# 027 octal = 23 en decimal
entero = 027

# en hexadecimal 0x17 = 23 en decimal

print 027
print 0x17

# numeros reales

real=0.2703
print real
print type(real)

# numeros complejos

complejo = 2.1 + 7.8j
print complejo
print type(complejo)


# operadores aritmeticos
r = 3 + 2
print r
r = 4 - 7
print r
r = -7
print r
r = 2*6
print r
r= 2**6
print r
r=3.5/2
print r
r=3.5//2    # division entera xD
print r
r=7%2
print r


# operandos logicos

r=3&2

r= 3 |2

r = 3 ^ 2   # ^ esto es un xor xD

r = ~5      # esto es un not xD
print r

# desplazamiento de bits

r = 1 << 10
print r
r = r >> 5
print r


# cadenas
# pueden tener una codificacion unicode(u) / raw(r)

unicode = u"a"
raw = r"\n"
print unicode
print raw 
ucalele = u"\n" # printa una linea blanca xD
print ucalele

triple = ''' primera linea
esto se vera en otra linea '''


tripledoble = """ primar p2    
                    otra linea """ # los tabuladores tambien surgen efecto xD
                    
                    
print triple
print tripledoble

# manipulacion de cadenas

a = "uno"
b= "dos"
c = a + " " + b
print c 
d = c + c 
print d

doble = a*2
print doble




# Booleanos

r = True and False
print r 

r = True or False
print r 

r = not True
print r 

# expresiones alternativas para booleanos

r = 5==3
r = 5!=3
r = 5<3
r = 5>3
r = 5 <= 4
r = 5 >= 3



































