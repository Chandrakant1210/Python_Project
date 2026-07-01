import game_data
import random
import art
score= 0
def wrong(score):
    print(f"Wrong!  your score is {score}")

def question():
    return random.choice(game_data.data)

def chek(ans, que_A, que_B):
    if ans=="A":
        if que_A["follower_count"]>que_B["follower_count"]:
            return True
        else:
            return False

def display():
    global score
    print(art.logo)
    que_A=question()
    que_B = question()
    if(score>0):
        print(f"You're right! Current score: {score}.")
    print(f"Compare A: {que_A["name"]} {que_A["description"]}  from {que_A['country']}")
    print(art.vs)
    print(f"Compare A: {que_B["name"]} {que_B["description"]}  from {que_B['country']}")

    ans=input("Who has more followers? Type 'A' or 'B':").upper()
    if chek(ans, que_A, que_B):

        score+=1
        print(f"You're right! Current score: {score}.")
        display()
    else:
        print(f"You're wrong! Current score: {score}.")
        return

display()