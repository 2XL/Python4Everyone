import socket

s = socket.socket()
s.bind(("localhost", 9999))
s.listen(2)

sc, addr = s.accept()   # tengo dos buzones o esque me devuelven 2 cosas
# cuando accep desbloquea la ejecucion (llega mensaje entrante)
"""
devuelve:
    1 objeto socket que representa la conexion del cliente 
    2 una tupla que contiene el host y puerto de dicha conexion
"""

while True:
    recibido = sc.recv(1024)
    if recibido =="quit":
        break
    print "Recibido:", recibido
    sc.send(recibido)
print "adios!"
sc.close()
s.close()
