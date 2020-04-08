def cuadrado(num):
    """Calcula el cuadrado de un numero.
    >>> l = [0, 1, 2, 3]
    >>> for n in l:
    ... cuadrado(n)
    [0, 1, 4, 9]
    """
    return num ** 2

def _test():
    import doctest
    doctest.testmod()
 
if __name__ == "__main__":
    _test()