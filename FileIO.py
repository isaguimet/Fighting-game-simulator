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
        self.totalTurns = self.line

        # Reading second Attacker line in the file                
        line1 = self.inputFile.readline()
        attacker = line1.split(",")
        self.probExtraLowAttack = attacker[1]
        self.probLowAttack = attacker[2]
        self.probMediumAttack = attacker[3]
        self.probHighAttack = attacker[4]
        
        #Reading third defender line in the file 
        line2 = self.inputFile.readline()
        defender = line2.split(",")
        self.probExtraLowDefense = defender[1]
        self.probLowDefense = defender[2] 
        self.probMediumDefense = defender[3] 
        self.probHighDefense = defender[4] 

        self.convertToInteger()

    """
    Function: convertToInteger()
    @ 1 argument type: convertToInteger(self)
    @ returns (none)
    """
    def convertToInteger(self):
        element = ""
        # Converting total turns to an integer
        element = str(self.totalTurns)
        self.totalTurns = int(element)

        # Converting each type of attack to integer
        element = str(self.probExtraLowAttack)
        self.probExtraLowAttack = int(element)
        element = str(self.probLowAttack)
        self.probLowAttack = int(element)
        element = str(self.probMediumAttack)
        self.probMediumAttack = int(element)
        element = str(self.probHighAttack)
        self.probHighAttack = int(element)

        # Converting each type of defense to integer
        element = str(self.probExtraLowDefense)
        self.probExtraLowDefense = int(element)
        element = str(self.probLowDefense)
        self.probLowDefense = int(element)
        element = str(self.probMediumDefense)
        self.probMediumDefense = int(element)
        element = str(self.probHighDefense)
        self.probHighDefense = int(element)

