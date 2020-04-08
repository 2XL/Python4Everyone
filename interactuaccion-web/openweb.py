
import urllib2

try:
    f = urllib2.urlopen("http://www.python.org") # permite opcion 'data' poder enviar datos o peticiones por post!
    print f.read()
    f.close()
except HTTPError, e:
    print "Ocurrio un error"
    print e.code
except URLError, e:
    print "Ocurrio un error grave!"
    print e.code