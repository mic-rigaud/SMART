#!/usr/bin/python3

# Definition d'un client reseau rudimentaire
# Ce client dialogue avec un serveur ad hoc

import socket, sys
from script.led.Led import Led


HOST = '192.168.9.30'
PORT = 50000
NOM = "RP1"

    
# 1) creation du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2) envoi d'une requete de connexion au serveur :
try:
    mySocket.connect((HOST, PORT))
except socket.error:
    print("La connexion a echoue.")
    sys.exit()    
print("Connexion etablie avec le serveur.")
    
# 3) Dialogue avec le serveur :



message = str.encode("%s" % (NOM))
mySocket.send(message)

msgServeur = bytes.decode(mySocket.recv(1024))
print(msgServeur)


led = ""
ledHisto = ""
sim = Led(NOM)

while 1:
    try:
        led = sim.getLed()
        if led!=ledHisto:
            print("la led allume:", led)
            mySocket.send(str.encode(led))
        ledHisto = led
        
    except KeyboardInterrupt:
        mySocket.send(str.encode("FIN"))
        print("Connexion interrompue.")
        mySocket.close()            
        break
 





    
