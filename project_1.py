import random
    
def name_to_number(name):
    if name=="rock":
        return 0
    elif name=="Spock":
        return 1
    elif name=="paper":
        return 2
    elif name=="lizard":
        return 3
    elif name=="scissors":
        return 4
    else:
        print("Invalid input")
    pass


def number_to_name(number):
    """
    Given integer number (0, 1, 2, 3, or 4)
    corresponding name from video
    """
    if number==0:
        return "rock"
    elif number==1:
        return "Spock"
    elif number==2:
        return "paper"
    elif number==3:
        return "lizard"
    elif number==4:
        return "scissors"
    pass


def rpsls(player_choice):
    print(" ")
    print("player's choice: ", player_choice)
    player_number=name_to_number(player_choice)
    comp_number=random.randrange(0,4)
    comp_choice=number_to_name(comp_number)
    print("computer's choice: ",comp_choice)


    dif=(player_number-comp_number)%5
    if dif==0:
        print("Tie")
    elif dif==1 or dif==2 :
        print("player wins")
    else:
        print("computer wins")
    pass
     
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



