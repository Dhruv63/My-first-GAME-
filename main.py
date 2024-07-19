# Making rock paper scissors game
# -1 for rock for computer and for user r
# 0 for paper for computer and for user p
# 1 for scissors for computer and for user s
import random

computer = random.choice([-1,0,1])

ch = input("Enter your Choice : ")
youdict ={"r" : -1,"p" : 0,"s" : 1}
yourch = youdict[ch]

disdict = {-1 : "Rock",0 : "Paper",1 : "Scissors"}

print(f"computer chooses {disdict[computer]}")
print(f"You choosed {disdict[yourch]}")


if(computer==yourch):
    print("Its a DRAW!")

else:
    if(computer==-1 and yourch==0):
        print("You Win!")
    elif(computer==-1 and yourch==1):
        print("You Lose!")
    elif(computer==1 and yourch==0):
        print("You Lose!")
    elif(computer==1 and yourch==-1):
        print("You Win!")
    elif(computer==0 and yourch==1):
        print("You Win!")
    elif(computer==0 and yourch==-1):
        print("You Lose!")
