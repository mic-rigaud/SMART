#!/usr/bin/python3

# Definition d'un serveur reseau gerant un systeme de CHAT simplifie.
# Utilise les threads pour gerer les connexions clientes en parallele.

HOST = '127.0.0.1'
PORT = 50000


import socket, sys, threading
import pickle


class ThreadClient(threading.Thread):
    '''derivation d'un objet thread pour gerer la connexion avec un client'''
    def __init__(self, conn, nom):
        threading.Thread.__init__(self)
        self.connexion = conn
        self.name = nom
        
    def run(self):
        while 1:
            msgClient = bytes.decode(self.connexion.recv(1024))
            if msgClient.upper() == "FIN" or msgClient =="":
                break
            message = "%s> %s" % (self.name, msgClient)
            print(message)
            direction = "donc la direction %s" % (DIRECTION[msgClient])
            print(direction)
            POSITION[self.name]=POSITION[self.name][0],POSITION[self.name][1],POSITION[self.name][2],DIRECTION[msgClient]
            ecriture()
        # Fermeture de la connexion :
        self.connexion.close()      # couper la connexion cote serveur
        del conn_client[self.name]        # supprimer son entree dans le dictionnaire
        print("Client %s deconnecte." % self.name)
        # Le thread se termine ici    


def initialisation():
    # Initialisation des donnes
    with open('donnees', 'rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        DIRECTION = mon_depickler.load()
    lecture()


def lecture():
    fichier = open("position", 'r')
    for line in fichier:
        contenue = line.split()
        POSITION[contenue[0]] = contenue[2],contenue[3],contenue[4],contenue[5]
    fichier.close()

def ecriture():
    fichier = open("position", 'w')
    for clef in POSITION:
        message = "%s : %s %s %s %s\n" %(clef,POSITION[clef][0],POSITION[clef][1],POSITION[clef][2], POSITION[clef][3])
        fichier.write(message)
    fichier.close()


DIRECTION = {}
POSITION = {}

# Cette initialisation permet d'initialiser les dictionnaire qui contiennent toute les variables
initialisation()

DIRECTION = {"led1": 0, "led2": 10,"led3": 20,"led4": 30,"led5": 40,"led6": 50,"led7": 60,"led8": 70,"led9": 80,"led10": 90,"led11": 100,"led12": 110,"led13": 120,"led14": 130,"led15": 140,"led16": 150,"led17": 160,"led18": 170,"led19": 180,"led20": 190,"led21": 200,"led22": 210,"led23": 220,"led24": 230,"led25": 240,"led26": 250,"led27": 260,"led28": 270,"led29": 280,"led30": 290,"led31": 300,"led32": 310,"led33": 320,"led34": 330,"led35": 340,"led36": 350}


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
        nom = bytes.decode(connexion.recv(1024))    
        th = ThreadClient(connexion, nom)
        th.start()    
        # Memoriser la connexion dans le dictionnaire : 
        #it = th.getName()   
        conn_client[nom] = connexion
        print("Client %s connecte, adresse IP %s, port %s." %\
              (nom, adresse[0], adresse[1]))
        # Dialogue avec le client :
        connexion.send(b'Vous etes connecte. Envoyez vos messages.')
    except KeyboardInterrupt:
        print("Fin du serveur")
        break
