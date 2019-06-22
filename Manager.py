from FileIO import *
from Attacker import *
from Defender import *

""" 
Version: June 22nd, 2019
The Manager class runs the simulation. It checks the attack-defense from a particular round match and records the correct 
result ('hit' or 'blocked'). Finally, it prints the simulation summary.
"""

class Manager:
    """
    Function: __init__(). 
    @ 1 Argument type: __init__(self)
    @returns (none)
    """
    def __init__(self):
        #attribute for total turns from FileIO 
        self.totalTurns = 0

        #attributes for attack and defense types
        self.probXLowAttack = 0
        self.probLowAttack = 0
        self.probMediumAttack = 0
        self.probHighAttack = 0
        self.probXLowDefense = 0
        self.probLowDefense = 0
        self.probMediumDefense = 0
        self.probHighDefense = 0

        # attributes for attack and defense tally types
        self.tallyHighAttack = 0
        self.tallyMediumAttack = 0
        self.tallyLowAttack = 0
        self.tallyXLowAttack = 0 
        self.tallyHighDefense = 0
        self.tallyMediumDefense = 0
        self.tallyLowDefense = 0
        self.tallyXLowDefense = 0

        # attributes for summary of results and turnbyturn
        self.attackType = ""
        self.defenseType = ""
        self.result = ""
        self.num = 1
        self.totalBlocks = 0
        self.totalHits = 0 

        # Manager creates 3 objects and calls the following:
        self.aFileIO = FileIO()
        self.aFileIO.readingFile()
        self.assigningProbabiltiesTurns()
        self.anAttacker = Attacker(self.probHighAttack,self.probMediumAttack, self.probLowAttack, self.probXLowAttack)
        self.aDefender = Defender(self.probHighDefense, self.probMediumDefense, self.probLowDefense, self.probXLowDefense)

    """
    Function: assigningProbabiltiesTurns()
    @ 1 Argument type: assigningProbabiltiesTurns(self)
    @returns (none)

    """
    def assigningProbabiltiesTurns(self):
        # Assigning Attacker Probabilities from FileIO to new variables
        self.probHighAttack = self.aFileIO.probHighAttack
        self.probMediumAttack = self.aFileIO.probMediumAttack
        self.probLowAttack = self.aFileIO.probLowAttack
        self.probXLowAttack = self.aFileIO.probExtraLowAttack
        
        # Assigning Defense Probabilities from FileIO to new variables
        self.probHighDefense = self.aFileIO.probHighDefense
        self.probMediumDefense = self.aFileIO.probMediumDefense
        self.probLowDefense = self.aFileIO.probLowDefense
        self.probXLowDefense = self.aFileIO.probExtraLowDefense

        # Assigning Total Turns from FIleIO to new variable
        self.totalTurns = self.aFileIO.totalTurns
    
    """
    Function: checkingHitBlock()
    @ 1 Argument type: checkingHitBlock(self)
    @returns (string, int, int)
    """
    def checkingHitBlock(self):
        self.result = ""
        if (self.anAttacker.xLowAttack == self.aDefender.xLowDefense) and (self.anAttacker.xLowAttack != 0) and (self.aDefender.xLowDefense != 0):
            self.result = "Blocked"
        
        elif (self.anAttacker.lowAttack == self.aDefender.lowDefense) and (self.anAttacker.lowAttack != 0) and (self.aDefender.lowDefense != 0):
            self.result = "Blocked"
            
        elif (self.anAttacker.mediumAttack == self.aDefender.mediumDefense) and (self.anAttacker.mediumAttack != 0) and (self.aDefender.mediumDefense != 0):
            self.result = "Blocked"
            
        elif (self.anAttacker.highAttack == self.aDefender.highDefense) and (self.anAttacker.highAttack != 0) and (self.aDefender.highDefense != 0):
            self.result = "Blocked"
            
        else:
            self.result = "Hit"
            
        if (self.result == "Blocked"):
            self.totalBlocks = self.totalBlocks + 1
        elif (self.result == "Hit"):
            self.totalHits = self.totalHits + 1
            
        return (self.result, self.totalBlocks, self.totalHits)        

    """
    Function: turnByTurnResults()
    @ 1 Argument type: turnByTurnResults(self, string)
    @returns (none)
    """
    def turnByTurnResults(self,results):
        print ("MK round %s:\t" %self.num,"ATTACK: %s\t, " %self.anAttacker.attackType, "DEFENSE: %s,\t" %self.aDefender.defenseType, ".........", results)
        self.num = self.num + 1 

    """
    Function: simulationSummary()
    @ 1 Argument type: simulationSummary(self, int, int)
    @returns (none)
    """ 
    def simulationSummary(self, totalBlocks, totalHits):
        print ()
        print ("Summary of kombat")
        print ("Total hits: %s" %totalHits, "  Total blocks: %s" %totalBlocks)
        tallyAttacker1 = int ((self.anAttacker.tallyXLowAttack/self.totalTurns)*100)
        tallyAttacker2 = int ((self.anAttacker.tallyLowAttack/self.totalTurns)*100)
        tallyAttacker3 = int ((self.anAttacker.tallyMediumAttack/self.totalTurns)*100)
        tallyAttacker4 = int ((self.anAttacker.tallyHighAttack/self.totalTurns)*100)

        print ("Attacker Proportions: X-Low %s%%," %tallyAttacker1, "Low %s%%, " %tallyAttacker2, end="")
        print ("Medium %s%%," %tallyAttacker3, "High %s%%" %tallyAttacker4)

        tallyDefender1 = int((self.aDefender.tallyXLowDefense/self.totalTurns)*100)
        tallyDefender2 = int((self.aDefender.tallyLowDefense/self.totalTurns)*100)
        tallyDefender3 = int((self.aDefender.tallyMediumDefense/self.totalTurns)*100)
        tallyDefender4 = int((self.aDefender.tallyHighDefense/self.totalTurns)*100)
        
        print ("Defender Proportions: X-Low %s%%," %tallyDefender1, "Low %s%%, " %tallyDefender2, end="")
        print ("Medium %s%%," %tallyDefender3, "High %s%%" %tallyDefender4)

    """
    Function: runSimulation()
    @ 1 Argument type: runSimulation(self)
    @returns (none)
    """ 
    def runSimulation(self):
        turn = 1
        randomNumber = 1
        while (turn <= self.aFileIO.totalTurns):
            self.anAttacker.randomProbabilitiesAttack(randomNumber)
            self.aDefender.randomProbabilitiesDefense(randomNumber)
            results, totalBlocks, totalHits = self.checkingHitBlock()
            self.turnByTurnResults(results)
            turn = turn + 1
        self.simulationSummary(totalBlocks,totalHits)


    
        
            