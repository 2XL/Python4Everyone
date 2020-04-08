# bucle while


edad = 0
while edad < 18:
    edad = edad + 1
    print "Felicidades, tienes " + str(edad)
    
# si se nos olvida el incrementado de offset este bucle seguira indefinidamente el qual se conoce como bucle infinito hay situaciones en los que el bucle infinito es util
#     por ejemplo veamos un pequeno programa que repite todo 
#     lo que el usario diga hasta que escriba adios xD  
entrada2=0
while True:
    entrada = "hola mundo" # raw_input("> ")
    if entrada2 == "adios":
        break
    else:
        print entrada
    entrada2 = "adios"
# tenemos otra que es el continue que consiste en pasar a ejecutar directamente la siguiente iteracion

edad = 0
while edad < 18:
    edad = edad+1
    if(edad % 2 == 0):
        continue
    print "Felicidades, tienes "+str(edad)

# bucle for estio moderno deslizante


# for ... in
# a los que hayais tenido expriencia previa con segun que lenguajes este bucle os va a sorprender gratament-
# en python  for se realiza como una forma generica de iterar sobre una secuencia. Y como tal
# intenta facilitar su uso para este finally:
# en este aspecto de un bucle for en python:

secuencia = ["uno", "dos", "tres"]
for elem in secuencia:
        print elem



# como hemos dicho los for se utilizan en python para recorrer secuencias, por lo que vamos a utilizar un tipo secuencia como es la lista para nuestro ejemplo
# leamos la cabecera del bucle como si de lenguaje natural se tratara " para cada elemento en secuencia"


for elem in secuencia:
        print elem









