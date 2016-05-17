#!/usr/bin/python3
################## SERVEUR.py #####################
# autheur: Equipe Smart
# date: 5 avril
#
# Description: cette application sert de serveur avec multi thread
###################################################

# Adresse de connexion
HOST = '127.0.0.1'
# Port de Connexion
PORT = 50000


import socket, sys, threading
import pickle



class ThreadClient(threading.Thread):
    '''objet thread servan a gerer les connexions clients'''
    def __init__(self, conn, nom):
        threading.Thread.__init__(self)
        self.connexion = conn # contient le nom de la connexion
        self.name = nom # le nom du rpi client
        
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
    '''Initialisation des donnes'''
    with open('donnees', 'rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        DIRECTION = mon_depickler.load()
    lecture()


def lecture():
    ''' Lecture du fichier position contenant la position de rpi avec leur angle de detection'''
    fichier = open("position", 'r')
    for line in fichier:
        contenue = line.split()
        POSITION[contenue[0]] = contenue[2],contenue[3],contenue[4],contenue[5]
    fichier.close()

def ecriture():
    ''' Ecriture dans le fichier position de le position des rpi avec leur angles de detection'''
    fichier = open("position", 'w')
    for clef in POSITION:
        message = "%s : %s %s %s %s\n" %(clef,POSITION[clef][0],POSITION[clef][1],POSITION[clef][2], POSITION[clef][3])
        fichier.write(message)
    fichier.close()


DIRECTION = {}
POSITION = {}

# Cette initialisation permet d'initialiser le dictionnaire POSITION qui contiennent toute les variables
initialisation()

DIRECTION = {"led1": 0, "led2": 10,"led3": 20,"led4": 30,"led5": 40,"led6": 50,"led7": 60,"led8": 70,"led9": 80,"led10": 90,"led11": 100,"led12": 110,"led13": 120,"led14": 130,"led15": 140,"led16": 150,"led17": 160,"led18": 170,"led19": 180,"led20": 190,"led21": 200,"led22": 210,"led23": 220,"led24": 230,"led25": 240,"led26": 250,"led27": 260,"led28": 270,"led29": 280,"led30": 290,"led31": 300,"led32": 310,"led33": 320,"led34": 330,"led35": 340,"led36": 350, "ledNULL":360}


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
conn_client = {}                # dictionnaire des clients connectes
while 1:
    try:
        connexion, adresse = mySocket.accept()
        # Identification du client avec d'ouvrir le thread
        nom = bytes.decode(connexion.recv(1024))    
        th = ThreadClient(connexion, nom)
        # ouverture du thread
        th.start()    
        conn_client[nom] = connexion
        print("Client %s connecte, adresse IP %s, port %s." %\
              (nom, adresse[0], adresse[1]))
        connexion.send(b'Vous etes connecte. Envoyez vos messages.')
    except KeyboardInterrupt:
        print("Fin du serveur")
        break
