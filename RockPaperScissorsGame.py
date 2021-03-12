from random import randint
lst = ['Rock','Paper','Scissors']
computer = lst[randint(0,2)]
player = False
while player == False:
    player = input("Rock,Paper, Scissors?")
    if player == computer:
        print("Tie!!!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!!")
        else:
            print("You Win!!!")
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!!!")
        else:
            print("You Win!!!")

    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!!!")
        else:
            print("You Win!!!")
    else:
        print("invalid input")
print("computer's choice was",computer)
