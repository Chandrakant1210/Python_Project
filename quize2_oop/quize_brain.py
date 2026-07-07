class Quize_brain_class:
    def __init__(self, q_list):
        self.q_no=0
        self.q_list=q_list
        self.score=0
    
        
    def still_que(self):
        if(self.q_no<len(self.q_list)):
            
            return True
        else:
            return False






    def next_question(self):
        
        curr_que=self.q_list[self.q_no]
        self.q_no+=1
        usr_input=input(f"Q{self.q_no}: {curr_que.que} \"Truee\" OR \"False\" ").lower()
        self.chek_ans(usr_input,curr_que.ans)



    def chek_ans(self,usr,ans):
        if(usr==ans.lower()):
            print("You got it right!")
            self.score+=1
        else:
            print("That's Wrong ")
            print(f"to correct answer was : {ans}")

        print(f"your cureent score is : {self.score}/{self.q_no}")


        