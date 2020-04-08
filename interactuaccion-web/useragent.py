

import urllib2, urllib

ua = "Mozilla/5.0 (compatible; Konqueror/3.5.8; Linux)"
h = {"User-Agent" : ua}
r = urllib2.Request("http://www.python.org", headers=h)
f = urllib2.urlopen(r)
print f.read()


"""

para personalizar la forma en que trabaja urllib2 podemos instalar un grupod e manejadores( handlers )
agrupados en un objeto de la clase OpenDirector (opener o abridor ), que sera el que se utilice a partid e ese momento al llamar a urlopen)

para construir:
    handler: --<
        build_opener
            cuenta con handlers que se encargan de manerjoar los esquemas disponibles
                HTTP
                HTTPS
                FTP
                    manejar la autenticacion 
                    manejar las redireciones
            para autentificacions requiremos instalar un opener que incluyera como manejador
                HTTPBasicAuthHandler
                ProxyBasicAuthHandler
                HTTPDigestAuthHandler
                ProxyDigestAuthHandler
"""
