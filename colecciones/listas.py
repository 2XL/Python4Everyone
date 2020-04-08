# En este capitulo vamos a ver:
# listas, tuplas y diccionarios


#   LISTAS

l = [22,True,"una lista",[1,2]]
mi_var1 = l[3][1]

# el indice empieza desde 0 xD

l = [11, False]
mi_var2 = l[0] # mi var = 11
print mi_var1
print mi_var2

# actualizacion de variable en la lista

l[0] = [1,2,3,4,5]
print l

# lol utilidad en python podemos uzar indices negativos xD
# -1 es el ultimo elemento -2 penultimo i asi succesivamente

inegado = l[0][-1]
print inegado

# permite el concepto slicing xD pillar un rango de elementos
# desde hasta sin incluir este ultimo: [ )a
# admite un tercer valor que implica salto (esquivar elementos intermedios)

l = 3*l
print l

slice = l[1:4]
print slice

slices = l[1:4:2]
print slices

# los argumentos slicing son opcionales es decir si omites uno implica cubrir todo el intervalo

silo = l[2:]
print silo

# tambien nos sirve para modificar la lista i canviar de rango

l = [99, True, "una lista", [1,2]]
l[0:2] = ['a','b']
print l
l[0:3] = ['a','b']
print l

print type(l)
