


# los sockets son un conncepto abstracto con el que e designa al punto final de una conxion

# un socket queda definido por la direccion ip del a maquina el puerto en el que escucha y el protocolo que utiliza:
"""
socket
    puerto
    ip
    protocolo
"""
# requiere importar el modulo socket ***:::***
"""
clasificacion de sockets por 
    flujo
            socket.SOCK_STREAM    --> tcp    --> cubre el 90% de las necesidades (solo haremos esto xD)
    
    datagramas
            socket.SOCK_DGRAM    --> udp


clasificacion de sockets por
    familia
        socket.AF_UNIX  --> son los primitivos sin concepcion de las redes (son de mucho antes)
        socket.AF_INET  --> son los que nos interesan
        socket.AF_INET6 --> para IPv6

-- para crear:
    socket.socket()
        se puede pasarle varios parametros...
        por defecto toma:
            familia: AF_INET
            tipo:    SOCK_STREAM

"""

import socket

myServer = socket.socket()
myClient = socket.socket()
# indicar puerto que se va a mantener a la escucha nuestro servidor
# usando el metodo bind (unir / atar / obligar )
myServer.bind("localhost", 9999) # host , puerto
# host se puede dejar vacio entonces se pondrar a escuchar por cualquier host disponible



# necesitamos hacer 'listen' para que acepte conexiones entrantes i por parametro el max num de parametros
myServer.listen(10)



# el metodo 'accept' se mantiene a la espera de conexiones entrantes
# bloqueando la ejecucion hasta que llegue un mensaje
# myClient, ("localhost", 9999) = myServer.accept()

recibido = myClient.recv(1024)
print "Recibido: ", recibido
myClient.send(recibido)

# una vez terminado de trabajar ocn sockets lo cerramos con el metodo close





