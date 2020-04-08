import urllib2

cookie_h = urllib2.HTTPCookieProcessor()
opener = urllib2.build_opener(cookie_h)
urllib2.install_opener(opener) # instalar un nuevo opener que no hace que el destino guarde los cookies

f = urllib2.urlopen("http://www.pyton.org")

"""

si queremos acceder a estas cookies o poder mandar nuestras propias cookies, podemso pasaerle como parametro al 
 ...	inicializar de HTTPokkieProcessor(...args...)
  args == objeto tipo CookieJar  >> modulo -> cookielib
"""