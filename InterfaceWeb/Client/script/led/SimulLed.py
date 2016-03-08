import time
import random
DIRECTION = ["led1", "led2", "led3", "led4","led5", "led6", "led7","led8","led9", "led10","led11", "led12","led13", "led14", "led15", "led16", "led17", "led18", "led19", "led20", "led21","led22","led23", "led24", "led25", "led26", "led27", "led28", "led29", "led30", "led31", "led32", "led33", "led34", "led35","led36", ]

class SimulLed():
    def __init__(self, nom):
        self.name = nom
        
    def getLed():
        time.sleep(5)
        i =random.random()*100
        if (i>64):
            if (i<65):
                return DIRECTION[0]
            elif (i<66):
                return DIRECTION[1]
            elif (i<67):
                return DIRECTION[2]
            elif (i<68):
                return DIRECTION[3]
            elif (i<69):
                return DIRECTION[4]
            elif (i<70):
                return DIRECTION[5]
            elif (i<71):
                return DIRECTION[6]
            elif (i<72):
                return DIRECTION[7]
            elif (i<73):
                return DIRECTION[8]
            elif (i<74):
                return DIRECTION[9]
            elif (i<75):
                return DIRECTION[10]
            elif (i<76):
                return DIRECTION[11]
            elif (i<77):
                return DIRECTION[12]
            elif (i<78):
                return DIRECTION[13]
            elif (i<79):
                return DIRECTION[14]
            elif (i<80):
                return DIRECTION[15]
            elif (i<81):
                return DIRECTION[16]
            elif (i<82):
                return DIRECTION[17]
            elif (i<83):
                return DIRECTION[18]
            elif (i<84):
                return DIRECTION[19]
            elif (i<85):
                return DIRECTION[20]
            elif (i<86):
                return DIRECTION[21]
            elif (i<87):
                return DIRECTION[22]
            elif (i<88):
                return DIRECTION[23]
            elif (i<89):
                return DIRECTION[24]
            elif (i<90):
                return DIRECTION[25]
            elif (i<91):
                return DIRECTION[26]
            elif (i<92):
                return DIRECTION[27]
            elif (i<93):
                return DIRECTION[28]
            elif (i<94):
                return DIRECTION[29]
            elif (i<95):
                return DIRECTION[30]
            elif (i<96):
                return DIRECTION[31]
            elif (i<97):
                return DIRECTION[32]
            elif (i<98):
                return DIRECTION[33]
            elif (i<99):
                return DIRECTION[34]
            elif (i<100):
                return DIRECTION[35]
        else:
            return DIRECTION[35]







