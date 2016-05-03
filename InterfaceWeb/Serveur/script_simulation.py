#!/usr/bin/python3

import math
import pickle
import time


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


def move(drone):
    drone[0]=drone[0]+20
    drone[1]=drone[1]+10


def verif_distance(drone):
    for clef in POSITION:
        if (math.sqrt((drone[0]-int(POSITION[clef][0]))**2+(drone[1]-int(POSITION[clef][1]))**2)>300):
            POSITION[clef] = POSITION[clef][0],POSITION[clef][1],POSITION[clef][2],360

def calcul_angle(drone):
    for clef in POSITION:
        angle = 360
        if (int(POSITION[clef][0])!=drone[0] and int(POSITION[clef][1])!=drone[1]):
            angle = -math.acos((int(POSITION[clef][0])-drone[0])/(math.sqrt((int(POSITION[clef][0])-drone[0])**2+(int(POSITION[clef][1])-drone[1])**2)))*180/math.pi+180
        if (drone[1]<int(POSITION[clef][1])):
            angle=360-angle
            angle = 5*(round(angle/5,0))
        POSITION[clef] = POSITION[clef][0],POSITION[clef][1],POSITION[clef][2],angle



DIRECTION = {}
POSITION = {}

# Cette initialisation permet d'initialiser les dictionnaire qui contiennent toute les variables
initialisation()

DIRECTION = {"led1": 0, "led2": 10,"led3": 20,"led4": 30,"led5": 40,"led6": 50,"led7": 60,"led8": 70,"led9": 80,"led10": 90,"led11": 100,"led12": 110,"led13": 120,"led14": 130,"led15": 140,"led16": 150,"led17": 160,"led18": 170,"led19": 180,"led20": 190,"led21": 200,"led22": 210,"led23": 220,"led24": 230,"led25": 240,"led26": 250,"led27": 260,"led28": 270,"led29": 280,"led30": 290,"led31": 300,"led32": 310,"led33": 320,"led34": 330,"led35": 340,"led36": 350, "ledNULL":360}



##### Fonction Main:

drone = [55 , 55]


while 1:
    move(drone)
    calcul_angle(drone)
    verif_distance(drone)
    ecriture()
    time.sleep(1)
    if(drone[0]>1500 and drone[1]>700):
        drone[0]=55
        drone[1]=55
