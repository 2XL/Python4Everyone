"""
existen dos modulos principales para leer doatos de URL's
    urllib
    urllib2    --> en esta leccion utilizaremos urllib2 (es mas completo pero no contiene todas la funcionalidades de urllib)
    
urllib2:
    puede leer datos de una URL:
        protocolos:
            HTTP
            HTTPS
            FTP
            Gopher
"""








# metodos particulares de urllib2
'''
    'urlopen'
        'read' -> por parametro especificamos teamaño
        'readline' -> literal
        'readlines' -> devuelve todo en un array
        'close'
            // funcionan exactamnete igual como si de un fichero de txt se trartar
            // estamos sobre una capa : pegamento : concepto wrapper !
        'geturl' -> devuelve la url que estamos leyendo
        'info' -> devuelve un objeto con las cabeceras de respuesta del servidor 'atributo header html'
'''