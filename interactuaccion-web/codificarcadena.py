import urllib, urllib2






params = urllib.urlencode({"usuario" : "manuel", "password" : "contrasena"})

f = urllib2.urlopen("http://ejemplo.com/login", params)



# si lo unico que ueremos es descargar el ocntenido de una URL a un archivo local
# lo podemos utilizar la funcion 
# 'urlretrieve' --> de --> urllib


"""
para enviar datos usando GET basta con concatenar la cadena resultante de urlencode con la url 
a la que nos vamos a conectar mediante el simbolo ?.


# diferencia urlopen - entre 1 y 2
    pues que el 2 tambien accepta 
        por parametro un objeto tipo 
        :    REQUEST 
                : USER AGENT
                : CABECERAS PROPIAS
    REQUEST:
        mas simple solo consta de la url
        opcional:
            parametros por post
            diccionario de headers
            origin_req_host
            unverifiable
            
"""
f = urllib2.urlopen("http://ejemplo.com/login" + 
                    "?" + params)





















