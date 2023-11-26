"""
create the game mastermind in python


set code, take a guess, colour correct and placement correct
"""

import sys 
import random 
# python Mastermind.py InputFile OutputFile [CodeLength] [MaximumGuesses] [AvailableColour]*
# python Mastermind.py InputFile OutputFile [CodeLength] [MaximumGuesses] [AvailableColour]*

class MasterMind:
    def __init__(self, input, output, codeLength, maxTries, colours):
        input = self.input
        output = self.output
        code_length = self.codeLength
        maxTries = self.maxTries
        #["red", "blue", "green", "yellow", "orange "]
        AvailableColours = self.AvailableColour



    def generateCode(self):
        for i in range(code_length):
            code += random.choice(AvailableColours)
        print( str.join(code) )
    
    def validInput(self):
        guess = str.split(line)
        if( guess is None or len(guess) != code_length):
            print("input code is wrong length.")
            return False
        for item in guess : 
            if item not in AvailableColours : 
                print("invalid colour '{}'".format(item) ) 
                return False
        return True
    

    def round(self,line, code):
        if validInput(line) :
            if( guess == code ):
                return True
        return False
        

        

    def play(self):
        code = generateCode()
        attempts = 0
        try:
            while attempts < maxTries:
                if round(self, guess, code): 
                    print("Congratulations! You guessed the code in", attempts, "attempts.")
                    break
                else:            
                    print("Incorrect guess. Try again.")
                
                    attempts += 1
            else:
                print("You ran out of attempts. The code was", code)
        except():
            print("ran into error") 
        


# python Mastermind.py InputFile OutputFile [CodeLength] [MaximumGuesses] [AvailableColour]*
"""
code ...
player human/computer
guesses 

code red blue yellow
player human
red green blue
red red red
blue blue blue yellow
red green green
red blue yellow
red red red
"""
if __name__ == "__main__":
    try:
        #file to read from 
        InputFile = sys.argv[1]
        #file to write to
        OutputFile = sys.argv[2]

        code_length = int(sys.argv[3])
        maxTries = int(sys.argv[4]) 
        colours = int(sys.argv[5])
    except:
        print("error passing from parameters")

    game = MastermindGame(InputFile, OutputFile, code_length, maxTries, colours)
    game.play()