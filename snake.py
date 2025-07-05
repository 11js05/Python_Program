'''
1 for stone
-1 for paper
0 for scissors
'''
import random
computer = random.choice([-1, 0, 1])
you=input("Enter your choice :")
youdict = {"stone": 1, "paper": -1, "scissors": 0}
younum = youdict[you]
if computer == younum:
    print("It's a draw!")
else:
    if(computer == -1 and younum == 1):
        print("you win!")
    elif(computer==-1 and younum==0):
        print("you lose!")
    elif(computer==1 and younum==-1):
        print("you lose!")
    elif(computer==1 and younum==0):
        print("you win!")
    elif(computer==0 and younum==-1):
        print("you win!")
    elif(computer==0 and younum==1):
        print("you lose!")
    else:
        print("something went wrong")
