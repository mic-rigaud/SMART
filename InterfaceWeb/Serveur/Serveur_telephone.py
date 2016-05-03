#!/usr/bin/python3

# Definition d'un serveur reseau gerant un systeme de CHAT simplifie.
# Utilise les threads pour gerer les connexions clientes en parallele.

HOST = '192.168.9.30'
PORT = 6666


import socket, sys, threading
import pickle
import time


class ThreadClient(threading.Thread):
    '''derivation d'un objet thread pour gerer la connexion avec un client'''
    def __init__(self, conn, nom):
        threading.Thread.__init__(self)
        self.connexion = conn
        self.name = nom
        
    def run(self):
        while 1:
            c=lecture()
            c=c+'\n\r'
            connexion.send(str.encode(c))
            time.sleep(0.5)
            msgClient = bytes.decode(self.connexion.recv(1024))
            if msgClient.upper() == "FIN" or msgClient =="":
                print("Connection terminer")
                break

                

def lecture():
    fichier = open("detection", 'r')
    contenue = fichier.readline()
    fichier.close()
    return contenue


# Initialisation du serveur - Mise en place du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print("La liaison du socket a l'adresse choisie a echoue.")
    sys.exit()
print("Serveur pret, en attente de requetes ...")
mySocket.listen(5)


# Attente et prise en charge des connexions demandees par les clients :
conn_client = {}                # dictionnaire des connexions clients
while 1:
    try:
        connexion, adresse = mySocket.accept()
        # Creer un nouvel objet thread pour gerer la connexion :
        nom = "telephone"
        th = ThreadClient(connexion, nom)
        th.start()    
        # Memoriser la connexion dans le dictionnaire : 
        #it = th.getName()   
        conn_client[nom] = connexion
        print("Client %s connecte, adresse IP %s, port %s." %\
              (nom, adresse[0], adresse[1]))
        # Dialogue avec le client :
        connexion.send(b'Vous etes connecte.\r\n')
    except KeyboardInterrupt:
        print("Fin du serveur")
        break
