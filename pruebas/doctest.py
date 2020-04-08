



"""

    tags
        >>>    python code exec & next line is the expected result (without >>>)
        the testdoc conclude with the next blank line or doc eof
        



"""


def cuadrados(lista):
    """calcula el cuadrado de los numeros de una lista 
    >>> l = [0,1,2,3]
    >>> cuadrados(l)
    [0,1,4,6]
    """
    return [n ** 2 for n in lista]

# para ejecutar la prueba
    # func:
        # testmod
        
def _test():
    import doctest
    doctest.testmod()
    
if __name__ == "__main__":
    _test()
 











