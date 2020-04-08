


"""
Docstrings

todos los objetos cuentan ocn una variable especial:

__doc__ 

mediante la que indicar el proposit y uso del objeto
estos son los llamados:
    -    docstrings     :: cadesnas de documentacion
        
"""


def haz_algo(arg):
    """Este es el docstring de la funcion."""
    print arg

print haz_algo.__doc__

haz_algo.__doc__ = """Este es un nuevo doctring"""

print haz_algo.__doc__

help(haz_algo)





























