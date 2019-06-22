""" 
Version: June 22nd, 2019
The FileIO class reads the number of total turns and probabilities from the file: input.txt
"""

class FileIO:
    """
    Function: __init__(). 
    @ 1 Argument type: __init__(self)
    @returns (none)
    """
    def __init__(self):
        # attributes for readingFile method
        self.inputFile = ""
        self.line = ""
        self.totalTurns = ""
        # attributes for probabilities of attack types
        self.probExtraLowAttack = 0
        self.probLowAttack = 0
        self.probMediumAttack = 0
        self.probHighAttack = 0
        #attributes for probabilities of defense types
        self.probExtraLowDefense = 0
        self.probLowDefense = 0
        self.probMediumDefense = 0
        self.probHighDefense = 0

    """
    Function: readingFile(). 
    @ 1 Argument type: readingFile(self)
    @returns (none)
    """
    def readingFile(self):
        fileOK = False
        if (fileOK == False):
            fileName = input("Enter name of file: ")
            if (len(fileName) == 0):
                print ("File name cannot be blank")
                self.readingFile()
            else:
                try:
                    self.inputFile = open(fileName, "r")
                    self.line = self.inputFile.readline()
                    if (len(self.line) == 0):
                        print ("File %s is empty" %fileName)
                        self.readingFile()
                    else:
                        self.readingLines()
                        fileOK = True
                        self.inputFile.close()
                except IOError:
                    print ("Error cannot open %s" %fileName)
                    self.readingFile()
                    
    """
    Function: readingLines(). 
    @ 1 Argument type: readingLines(self)
    @returns (none)
    """
    def readingLines(self): 
        # Assigning line0 to new variable
        self.totalTurns = int (self.line)

        # Reading second Attacker line in the file                
        line1 = self.inputFile.readline()
        attacker = line1.split(",")
        self.probExtraLowAttack = int (attacker[1])
        self.probLowAttack = int (attacker[2])
        self.probMediumAttack = int (attacker[3])
        self.probHighAttack = int (attacker[4])
        
        #Reading third defender line in the file 
        line2 = self.inputFile.readline()
        defender = line2.split(",")
        self.probExtraLowDefense = int (defender[1])
        self.probLowDefense = int (defender[2])
        self.probMediumDefense = int (defender[3]) 
        self.probHighDefense = int (defender[4])