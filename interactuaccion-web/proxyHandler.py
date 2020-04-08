import urllib2
 


proxy_h = urllib2.ProxyHandler({"http" : "http://miproxy.net:123"})
opener = urllib2.build_opener(proxy_h)
urllib2.install_opener(opener)
f = urllib2.urlopen("http://www.python.org")