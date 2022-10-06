
"Rock paper scissors game created by Karina Puente "
import numpy as np 
import random as rand


print("Welcome to Rock, Paper, Scissors")

tr = True

while tr: 
    select = str(input("Choose your implementation! 1 = Rock, 2 = Paper, 3= Scissors, 0=Quit "))
    num = int(select)
    randi= rand.randint(1,3)
    Dict = {1: 'Rock', 2: 'Paper', 3:'Scissors', 0: 'Quit'}

    # print("You picked: ",Dict[num], "and the computer picked: ", Dict[randi])

    if num == 0:
        print("Thanks for playing")
        tr = False
    elif num == randi: 
        print("You picked: ",Dict[num], "and the computer picked: ", Dict[randi])
        print("It's a draw!")
    elif num == 1 and randi == 2:
        print("You picked: ",Dict[num], "and the computer picked: ", Dict[randi])
        print("You lose!")

    elif num == 1 and randi == 3:
        print("You picked: ",Dict[num], "and the computer picked: ", Dict[randi])
        print("You win!")
    
    elif num == 2 and randi ==1:
        print("You picked: ",Dict[num], "and the computer picked: ", Dict[randi])
        print("You win!")
    
    elif num ==3 and randi == 1:
        print("You picked: ",Dict[num], "and the computer picked: ", Dict[randi])
        print("You lose!")

    elif num == 2 and randi ==3:
        print("You picked: ",Dict[num], "and the computer picked: ", Dict[randi])
        print("You lose!")

    elif num == 3 and randi ==2:
        print("You picked: ",Dict[num], "and the computer picked: ", Dict[randi])
        print("You lose!")

    else: 
        print("Enter a valid number from the options given")
    






# print("You picked {Dict[1]} and the computer picked: {Dict[randi]}")

# while (num >= 0):

#     if num == 0:
#         print("Thanks for playing!")

#     elif num == 1: 
#         print("You picked {Dict[1]} and the computer picked: {Dict[randi]}")
#         # if randi == 1:
#     else:
#         print ("ok")



# elif num == 2:
#     print("You picked rock and the computer picked: {Dict[2]}")

# elif num == 3:
#     print("You picked rock and the computer picked: {Dict[3]}") 

# else:
#     print("The number you have selected is invalid. Try again.")