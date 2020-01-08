#! python3

#ps7b

import random

class Yahtzee(object):

    def __init__(self,num_dice,num_simulation):

        self.num_dice = num_dice
        self.num_simulation = num_simulation
        self.list_of_rolls = []
        self.numYahtzee = 0

    def rollAllDice(self):

        for i in range(self.num_dice):

            self.list_of_rolls.append(random.randint(1,6))

        pass

    def clearDiceRolls(self):

        self.list_of_rolls = []

    def isYahtzee(self):

        for i in range(len(self.list_of_rolls)):

            if self.list_of_rolls[i] != self.list_of_rolls[i-1]:

                return False
            
                break

        return True
            
    def runSimulation(self):


        for i in range(self.num_simulation):

            self.rollAllDice()
            
            if self.isYahtzee():
                self.numYahtzee += 1

            self.clearDiceRolls()

            print('Simulation %s : Current Yahtzee count is at %s' % (i+1,self.numYahtzee))

        
    
