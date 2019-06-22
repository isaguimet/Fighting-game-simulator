"""
Version: 14 - June 22nd, 2019. 
Summary of overall features - This program is a simple text-based fight simulator. There are two opponents: 
an attacker (that only launches attacks) and a defender (that can only defend against the attacks). 
There's four types of attacks categorized by height: extra-low, low, medium and high.
Similar to the attacks there are four types of defenses: extra-low, low, medium and high. If the heights 
of the attack-defense match, then the attack is blocked. Otherwise the attack is counted as a 'hit'. 

Program Limitations: This program assumes that any other version of the input file used will have 
the same format and the four probabilities for each of the attacker and defender will sum to 100%.
Program also assumes that the number of turns read in from the file will always be an integer value in the
range of 1-100. 

"""
from Manager import *

def start():
    aManager = Manager()
    aManager.runSimulation()

start()
