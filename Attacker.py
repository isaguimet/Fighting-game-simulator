from Globals import *
import random

""" 
Version: June 22nd, 2019
The Attacker class generates an attack based on the probabilities read in from the file: input.txt
"""

class Attacker:
    """
    Function: __init__(). 
    @ 5 Argument types: __init__(self, int, int, int, int)
    @returns (none)
    """
    def __init__(self, probHighAttack, probMediumAttack, probLowAttack, probXLowAttack):
        self.probHighAttack = probHighAttack
        self.probMediumAttack = probMediumAttack
        self.probLowAttack = probLowAttack
        self.probXLowAttack = probXLowAttack
        # variables for counting the number of each attack
        self.tallyHighAttack = 0
        self.tallyMediumAttack = 0
        self.tallyLowAttack = 0
        self.tallyXLowAttack = 0
        # variables for attack 
        self.highAttack = 0
        self.mediumAttack = 0 
        self.lowAttack = 0
        self.xLowAttack = 0
        # type of attack for results.txt
        self.attackType = ""

    """
    Function: randomProbabilitiesAttack()
    @ 2 argument types: randomProbabilitiesAttack (self, integer)
    @ returns (none) 
    """
    def randomProbabilitiesAttack (self, randomNumber):
        self.xLowAttack = 0
        self.lowAttack = 0
        self.mediumAttack = 0
        self.highAttack = 0
        self.attackType = ""

        randomNumber = 0
        randomNumber = random.randrange(1,101)
        if (randomNumber >= 1) and (randomNumber <= self.probXLowAttack):
            self.tallyXLowAttack = self.tallyXLowAttack + 1
            self.xLowAttack = EXTRA_LOW
            self.attackType = "X-low"

        elif (randomNumber > self.probXLowAttack) and (randomNumber <= self.probXLowAttack + self.probLowAttack):
            self.tallyLowAttack = self.tallyLowAttack + 1
            self.lowAttack = LOW
            self.attackType = "low"

        elif (randomNumber > self.probXLowAttack + self.probLowAttack) and (randomNumber <= self.probXLowAttack + self.probLowAttack + self.probMediumAttack):
            self.tallyMediumAttack = self.tallyMediumAttack + 1
            self.mediumAttack = MED
            self.attackType = "medium"
        
        elif (randomNumber > self.probXLowAttack + self.probLowAttack + self.probMediumAttack) and (randomNumber <= 100):
            self.tallyHighAttack = self.tallyHighAttack + 1
            self.highAttack = HIGH
            self.attackType = "high"
            