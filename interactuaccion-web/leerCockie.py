
"""

Para leer las cookies mandadas basta crear un objeto iterable a partir del CookieJar 
(tambien podriamos buscar las cabeceras correspondientes, 
pero este sistema es mas claro y sencillo):
"""


import urllib2, cookielib


cookie_j = cookielib.CookieJar()
cookie_h = urllib2.HTTPCookieProcessor(cookie_j)


opener = urllib2.build_opener(cookie_h)
opener.open("http://www.python.org")
for num, cookie in enumerate(cookie_j):
    print num, cookie.name
    print cookie.value
    print

"""
En el improbable caso de que necesitaramos 
anadir una cookie antes de realizar la conexion, 
en lugar de conectarnos para que el sitio la mande, 
podriamos utilizar el metodo set_cookie de CookieJar, 
al que le pasamos un objeto de tipo Cookie. 
El constructor de Cookie, no obstante, 
es bastante complicado.
"""