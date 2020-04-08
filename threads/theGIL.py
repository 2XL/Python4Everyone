""" 


la ejecucion de los therads en python esta controlada por el gil (GLOBAL INTERPRETER LOCK)
de manera que solo un thread puede ejecutarse a la vez (limitacion de rendimiento)
pero esto no sucede con los procesos (en ocasiones nos puede interesar mas))


" 
cada intervalo de intercanvio de ejecucion esta 
    asignado por defecto como:
        10 instrucciones de bytecode
        o cuando el hilo se pone a dormir
        o cuando hay una op de E/S
    augque lo podemos modificar mediante la funcion:
        sys.set-checkinterval
        
    para minimizar el efecto GIL [global interpreter lock)
    es conveniente llamar al interpredte con el flag -0
    lo que hara es genere un byte code optimizado con menos instrucciones y por lo tanto
    menos cambios de ocntexto.
    tambien podemos plantear el utilizar procesos en lugar de threads como 
    ya comentamos utilizando el modulo:
        'processing'
        otras alternativas es 
            .c
            IronPython
            Jython
                que carecen de GIL
    
"""

