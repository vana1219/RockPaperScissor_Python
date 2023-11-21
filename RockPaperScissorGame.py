## Van Nguyen



## get random choice function
## Takes no arguments
## Returns one of three strings randomly
## To add more choices, add more strings to choices
import random
def getRandomChoice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)



## get choice from user function
## Input validation
## Takes no arguments
## Takes user input and validates against choices
## Returns ONLY one of choice strings
## To add more choices, add more strings to choices
def getChoice():
    choices = ['rock', 'paper', 'scissors']
    userChoice = ""
    while userChoice not in choices:
        userChoice = input("Choice rock, paper, or scissors: ")
    return userChoice.lower()



## get mode function
## Input validation
## Takes no arguments
## Takes user input and validates against choices
## Returns ONLY one of choice strings
## Continue to prompt for choice until user enters a valid answer
## To add more choices, add more strings to choices
def getMode():
    choices = ['friend', 'computer', 'auto']
    userChoice = ""
    while userChoice.lower() not in choices:
        userChoice = input("Choice friend, computer, or auto: ")
    return userChoice.lower()


    
## get number function
## Input validation
## Error handling
## returns an int between 0 and max number'
## Will not return an unsafe number
## Will not return negative or greater than max number
## Bad user input returns 0
def getNum(max):
    userNumber = input("Enter a number from 0 to " + str(max) + ": ")
    try:
        max = int(max)
        userInt = int (userNumber)
        if userInt > max:
            return max
        elif userInt < 0:
            return 0
        else:
            return userInt
    except ValueError:
        print("Invalid input. Returning zero")
        return 0


    
## get name function
## Input validation
## takes no arguments
## returns user input string
## Must not allow for a blank name
def getName():
    name = ""
    while name == "":
        name = input("player's name: ")
    return name



## get winner function
## Pass in player choices and player names as string arguments
## This function will decide the winner and give output
## Output includes displaying the players names and choices
def getWinner(p1Choice, p2Choice, p1Name, p2Name):
    if p1Choice == p2Choice:
        print("Both choose the choices.It's Tie Game \n")
        
    #Rock>scissors>paper>rock
        
    elif p1Choice == "rock":
        if p2Choice == "scissors":
            print(p1Name + " chose " + p1Choice)
            print(p2Name + " chose " + p2Choice)
            print(p1Name + " Wins")
        elif p2Choice == "paper":
            print(p1Name + " chose " + p1Choice)
            print(p2Name + " chose " + p2Choice)
            print(p2Name + " Wins")
            
    elif p1Choice == "scissors":
        if p2Choice == "paper":
            print(p1Name + " chose " + p1Choice)
            print(p2Name + " chose " + p2Choice)
            print(p1Name + " Wins")
        elif p2Choice == "rock":
            print(p1Name + " chose " + p1Choice)
            print(p2Name + " chose " + p2Choice)
            print(p2Name + " Wins")
            
            
    elif p1Choice == "paper":
        if p2Choice == "rock":
            print(p1Name + " chose " + p1Choice)
            print(p2Name + " chose " + p2Choice)
            print(p1Name + " Wins")
        elif p2Choice == "scissors":
            print(p1Name + " chose " + p1Choice)
            print(p2Name + " chose " + p2Choice)
            print(p2Name + " Wins")
            

    
    
## Main function 
## Prints a banner
## Calls the menu function
def main():
    print("Welcome to the Rock Paper Scissors game Version 1.01")
    menu()
    print("End of Main")
## Menu Function
## Loops on the again flag
## Validates input on prompt
## Case insensitive
## Calls play function on "yes" or "y"
## Breaks loop on "no" or "n"
## Output "invalid input" on anything else
    
def menu():
    answer = ""
    while answer.lower() != "no" or answer.lower() != "n":
        answer = input("Would you like to play? yes or no: ")
        if answer.lower() == "yes" or answer.lower() == "y":
            mode = getMode()
            play(mode)
        elif answer.lower() == "no" or answer.lower() == "n":
            break
            
        else:
    
            print("invalid input")

        
            
            
            
        
    
# Play function
def play(mode):
    if mode.lower() == "computer":
        p1Name = "Computer"
        p2Name = getName()
        p1Choice = getRandomChoice()
        p2Choice = getChoice()
    elif mode.lower() == "friend":
        p1Name = getName()
        p2Name = getName()
        p1Choice = getChoice()
        p2Choice = getChoice()
    elif mode.lower() == "auto":
        p1Name = "Auto P1"
        p2Name = "Auto P2"
        p1Choice = getRandomChoice()
        p2Choice = getRandomChoice()
    else:
        print("Error")
        return
    getWinner(p1Choice,p2Choice,p1Name,p2Name)
    print("Thank you for playing")
# Call main function
main()
