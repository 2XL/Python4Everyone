# FUNCIONES
# una funcion es un fragmento de codigo con un nombre asociado que realiza una serie de tareas y devuelve un valor


# A los fragmentos de codigo que tienen un nombre asociado y no devuelve : procedimientos

# en python no existe acciones / procedimientos ( si no se especifica se devuelve un none == null)

def mi_funcion(arg1, arg2):
    print arg1
    print arg2
    
    
# docstring (cadena de documentacion) al inicio de la funcion

def mi_docfunc(arg1, arg2): 
    """ Esta funcion imprimer los dos valores pasados como parametro"""
    print arg1
    print arg2
    
mi_funcion('ndroi', 'ppl')

# se permite alterar el orden de los argumentos
mi_funcion(arg2= 'soy 2', arg1='soy 1')

# tambien es possible crear una funcion con numero variable de argumentos
# o asignarles valores por defecto durante el proceso de definicion

def imprimir(texto, veces = 1):
    print veces*texto
    
imprimir('lol')
imprimir('olo', 5)


def vararg(a, *args):
    for arg in args:
        print arg
vararg(1,2)
vararg(1,2,3)
vararg(1,2,3,4)

# tambien se puede utilizar otro modo en vez de una tupla se usa como diccionario

def varios(arg1, arg2, **args):
    for i in args.items():
        print i
        
varios(1,2, tercero=3, segundo=2)

# en python se utiliza el paso por valor de referencias a objetos
# pero en python a diferencia de java, todo es objeto



# en el caso de las tupas cuando se pasa por parametro a una funcion se genera una lista nueva que sera mutable en la funcio i transparente
# a fuera de la funcion

def f(x,y):
    x=x+3
    y.append(23)
    print x, y

# notar variables mutables e inmutables
x=22
y=[22]
f(x,y)
print x,y



def sumar(x,y):
    return x+y

print sumar(3,2)


# tambien podems retornar varios variables a la vez para print o inicializar vars

def exp2(x,y):
    return x*x,y*y

a=5
b=9
aa, bb = exp2(a, b)
print exp2(a,b)
print aa,bb






















