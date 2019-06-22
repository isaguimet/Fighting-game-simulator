from Globals import * 
import random

""" 
Version: June 22nd, 2019
The Defender class generates a defense based on the probabilities read in from the file: input.txt
"""

class Defender:
    """
    Function: __init__(). 
    @ 5 Argument types: __init__(self, int, int, int, int)
    @returns (none)
    """
    def __init__(self,probHighDefense,probMediumDefense,probLowDefense, probXLowDefense):
        self.probXLowDefense = probXLowDefense
        self.probLowDefense = probLowDefense
        self.probMediumDefense = probMediumDefense
        self.probHighDefense = probHighDefense
       
        # variables for counting each type of defense
        self.tallyHighDefense = 0
        self.tallyMediumDefense = 0
        self.tallyLowDefense = 0
        self.tallyXLowDefense = 0 
        # Variables for defense
        self.highDefense = 0
        self.mediumDefense = 0 
        self.lowDefense = 0
        self.xLowDefense = 0
        # type of defense for results.txt
        self.defenseType = ""

    """ 
    Function: randomProbabilitiesDefense()
    @ 2 argument types: randomProbabilitiesDefense (self, int)
    @ returns (none) 
    """
    def randomProbabilitiesDefense(self,randomNumber):
        self.xLowDefense = 0
        self.lowDefense = 0
        self.mediumDefense = 0
        self.highDefense = 0
        self.defenseType = ""

        randomNumber = random.randrange(1,101)
        if ((randomNumber >= 1) and (randomNumber <= self.probXLowDefense)):
            self.tallyXLowDefense = self.tallyXLowDefense + 1
            self.xLowDefense = EXTRA_LOW
            self.defenseType = "X-low" 

        elif ((randomNumber > self.probXLowDefense) and (randomNumber <= self.probXLowDefense + self.probLowDefense)):
            self.tallyLowDefense = self.tallyLowDefense + 1
            self.lowDefense = LOW
            self.defenseType = "low"

        elif ((randomNumber > self.probXLowDefense + self.probLowDefense) and (randomNumber <= self.probXLowDefense + self.probLowDefense + self.probMediumDefense)):
            self.tallyMediumDefense = self.tallyMediumDefense + 1
            self.mediumDefense = MED
            self.defenseType = "medium"

        elif ((randomNumber > self.probXLowDefense + self.probLowDefense + self.probMediumDefense) and (randomNumber <= 100)):
            self.tallyHighDefense = self.tallyHighDefense + 1
            self.highDefense = HIGH
            self.defenseType = "high"

