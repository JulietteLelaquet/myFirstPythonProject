from math import *
from random import*

#Declaration of starting variables
money = int(input("How much money do you have? : ")) #The player chooses his           money
continueGame = True #Boolean true as long as we can continue the game

print(f"You sit down at the roulette table with {money} euros")

#As long as the game continues, the player is asked to choose the number on which he will bet
while continueGame:
    betNumber = -1
    while betNumber < 0:
        betNumber = int(input("Choose a number you want to bet on between 0 and 49 inclusive : "))
        if betNumber < 0 or betNumber > 49 :
            print("You have not chosen a valid number, as a reminder your number must be in the range 0, 49 inclusive")
            betNumber = -1

    #We select the amount of money to bet on the chosen number
    bet = -1
    while bet <=0 or bet > money:
        bet = int(input("Enter your bet amount : "))
        if bet <= 0 or bet > money:
            print("Your bet amount must be between 0 and your money value")
            bet = -1

    #We spin the roulette
    winningNumber= randint(0,49)
    print(f"The roulette spins.... and stops on the number {winningNumber}!")

    #The player's winnings are established
    if winningNumber == betNumber:
        print(f"Congratulations ! You get {bet*3} euros")
        money += bet * 3
    elif winningNumber%2 == betNumber %2 : #We simplify by saying that even     numbers are the same color and odd numbers too
        bet = ceil(bet * 0.5)
        print(f"You bet on the right color, you get {bet} euro(s)")
        money += bet
    else:
        print("Sorry, you win nothing on this round")
        money -= bet

    if money <=0:
        print("You have no more money, it's game over")
        continueGame = False
    else:
        print(f"You now have {money} euros")
        match input("Do you want to leave the casino ? (y/n)"):
            case "y" | "Y" :
                print(f"You leave the casino witj {money} euros")
                continueGame = False
            case "n" | "N" :
                continueGame = True