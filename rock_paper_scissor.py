import random
import sys

def main():

    print("This program simulates a 'rock paper scissor' game. \n")
    print("The rules are as follows: rock beats scissor, paper beats rock, and scissor beats paper. \n")

    #get user input
    user_choice = input("Please choose from the following: \n"
                    " 1 for scissor \n"
                    " 2 for rock \n"
                    " 3 for paper. \n")


    #validate user input so only 1, 2, or 3 is entered
    while user_choice != '1' and user_choice != '2' and user_choice != '3':
        user_choice = input("Please enter only '1' for scissor, '2' for rock, or '3' for paper: ")
    
    #convert user input to rock, paper, or scissor
    if user_choice == '1':
        u_choice = 'Scissor'
    elif user_choice == '2':
        u_choice = 'Rock'
    elif user_choice == '3':
        u_choice = 'Paper'

    print("You have chosen " + u_choice, "now we will see what the computer has chosen.")

    #generate random int and convert computer choice to rock, paper, or scissor
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        c_choice = 'Scissor'
    elif comp_choice == 2:
        c_choice = 'Rock'
    elif comp_choice == 3:
        c_choice = 'Paper'

    #output the computer and user choices to the user
    print("The computer chose: " + c_choice, "\n")
    print("We have " + u_choice, "vs " + c_choice, "\n")

    result = ""
    #assign result the value of the winning choice
    if (c_choice == 'Scissor' and u_choice == 'Paper') or (c_choice == 'Paper' and u_choice == 'Scissor'):
        result = 'Scissor'
        print(result, "wins! \n")
    elif (c_choice == 'Paper' and u_choice == 'Rock') or (c_choice == 'Rock' and u_choice == 'Paper'):
        result = 'Paper'
        print(result, "wins! \n")
    elif (c_choice == 'Rock' and u_choice == 'Scissor') or (c_choice == 'Scissor' and u_choice == 'Rock'):
        result = 'Rock'
        print(result, "wins! \n")
    elif (c_choice == 'Scissor' and u_choice == 'Scissor') or (c_choice == 'Rock' and u_choice == 'Rock') or (c_choice == 'Paper' and u_choice == 'Paper'):
        result = c_choice 

    #Check whether the user or computer is the winner and print result
    if result == c_choice and result == u_choice:
        print("It's a tie game!")
    elif result == c_choice:
        print("The computer is the winner!")
    elif result == u_choice:
        print("The user is the winner!")

    #Give user the option to restart the game or exit the program
    retry = input("Would you like to play again? Press 'r' to restart or any other key to quit.").lower()
    if retry == 'r':
        main()
    else:
        exit()

main()




