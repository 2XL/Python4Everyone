import urllib2


aut_h = urllib2.HTTPBasicAuthHandler()
aut_h.add_password("realm", "host", "usuario", "password")
opener = urllib2.build_opener(aut_h)
urllib2.install_opener(opener)
f = urllib2.urlopen("http://www.python.org")




