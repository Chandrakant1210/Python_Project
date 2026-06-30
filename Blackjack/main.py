import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def del_cards():
    return random.choice(cards)

def cal_score(card):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(card)


def compare(usr_score,computer_score):
    if usr_score==computer_score:
        return "Draw 🙃"
    elif(usr_score==0):
        return "Win with a Blackjack 😎"
    elif computer_score==0:
        return "Lose, opponent has Blackjack 😱"
    elif usr_score>21:
        return "You went over. You lose 😭"
    elif computer_score>21:
        return "Opponent went over. You win 😁"
    elif usr_score>computer_score:
        return "You Win 😁"
    else:
        return "you Lose 😭"



def play_game():
    print(art.logo)
    usr_card=[]
    computer_card=[]
    usr_score=0
    computer_score=0
    game=True
    for i in range(0,2):
        usr_card.append(del_cards())
        computer_card.append(del_cards())
    while game:
        usr_score=cal_score(usr_card)
        computer_score=cal_score(computer_card)

        print(f"Your cards: {usr_card} and your total score: {usr_score}")
        print(f"Computer's first card: {computer_card[0]}")
        if(usr_score==0 or computer_score==0 or usr_score>21):
            game=False
        else:
            if(input("Do you want to choose another card type for yes 'y'  for no 'n' ").lower() == 'y'):
                usr_card.append(del_cards())
            else:
                game=False
        while computer_score!=0 and computer_score<=17:
            computer_card.append(del_cards())
            computer_score=cal_score(computer_card)
        print(f"your final card in hand is{usr_card} and your total score is {usr_score}")
        print(f"computer's final card: {computer_card} and computer  total score is {computer_score}")

        print(compare(usr_score,computer_score))



while(input("you want too play GAME if yes type 'y' or if NO type 'n' ")=="y"):
    # print("\n" * 20)
    play_game()