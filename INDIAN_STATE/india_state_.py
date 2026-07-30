import turtle 
import pandas as pd 



data=pd.read_csv("india_states.csv")
all_state=data.State.to_list()

screen=turtle.Screen()

screen.title("india_state_game")
image="india_state_.gif"
screen.addshape(image)
turtle.shape(image)
state=[]
while len(state)<29:
    answer_state=screen.textinput(title=f"guess the  state name {len(state)}/ 29 state correct", prompt="enter state name ").title()
    print(answer_state)

    if answer_state in all_state:
        state.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.State==answer_state]
        X=state_data.X.item()
        Y=state_data.Y.item()
        t.goto(X,Y)
        t.write(answer_state)

    





def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
