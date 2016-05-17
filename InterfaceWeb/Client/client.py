#!/usr/bin/python3
################## SERVEUR.py #####################
# auteur: Equipe Smart
# date: 5 avril
#
# Description: cette application sert de client
###################################################

import socket, sys
from script.led.SimulLed import SimulLed

# Adresse de connexion
HOST = '127.0.0.1'
# Port de connexion
PORT = 50000
# Nom du RPI se connectant
NOM = "RP1"

    
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Realisaion de la connection
try:
    mySocket.connect((HOST, PORT))
except socket.error:
    print("La connexion a echoue.")
    sys.exit()    
print("Connexion etablie avec le serveur.")
    
# identification du RPI
message = str.encode("%s" % (NOM))
mySocket.send(message)

msgServeur = bytes.decode(mySocket.recv(1024))
print(msgServeur)


led = ""
ledHisto = ""
# Permet de simuler l'acquisition as port GPIO
# Il suffit de changer cette fonction pour que le code soit adapter 
#     au radiogoniometre branche au port GPIO
sim = SimulLed(NOM)

while 1:
    try:
        led = sim.getLed() # recuperation de l'etat des led a cet instant
        if led!=ledHisto:
            print("la led allume:", led)
            mySocket.send(str.encode(led))
        ledHisto = led
    except KeyboardInterrupt:
        # fin de la socket sur une interruption de type Ctrl-C
        mySocket.send(str.encode("FIN"))
        print("Connexion interrompue.")
        mySocket.close()            
        break
 





    
