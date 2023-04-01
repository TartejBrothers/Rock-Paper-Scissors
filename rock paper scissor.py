import random
print("Choose From Rock, Paper, Scissors")
lst=["rock","paper","scissors"]
score_user=0
score_comp=0
while True:
    a=str(input("Enter Input:"))
    input_user=a.lower()
    input_comp=random.choice(lst)
    if input_user=="rock" and input_comp=="scissors":
        score_user=score_user+1
        print("Computer Selected:",input_comp)
        print("You Won")
        print("Score User=",score_user,"Score Computer",score_comp)
    elif input_user=="paper" and input_comp=="rock":
        print("Computer Selected:",input_comp)
        print("You Won")
        
        score_user=score_user+1
        print("Score User=",score_user,"Score Computer",score_comp)
    elif input_user=="scissors" and input_comp=="paper":
        score_user=score_user+1
        print("Computer Selected:",input_comp)
        print("You Won")
        print("Score User=",score_user,"Score Computer",score_comp)
    elif input_user==input_comp:
        print("Computer Selected:",input_comp)
        print("No Points Given")
        print("Score User=",score_user,"Score Computer",score_comp)
    else:
        score_comp=score_comp+1
        print("Computer Selected:",input_comp)
        print("You Lost")
        print("Score User=",score_user,"Score Computer",score_comp)
    if score_user==10:
        break
    elif score_comp==10:
        break
print("Game Over")
print("Score User=",score_user,"Score Computer",score_comp)
    
